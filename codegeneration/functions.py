"""Codegeneration Functions

This module contains the functions that do the main work of the code
generator.

Examples
--------
    generate_code(output_dir, *[('appname', 'path/to/input/csv'), ... ])

Notes
-----
    generate_models is called like a helper by generate_code
    Flow: Parameters are parsed > CSV file is opened in read mode
    > global dictionaries are collected > models.py and test_models.py are created >
    > test_models.py head is applied

Attributes
----------
    apps_Models: dict
        Dictionary of the form {'appname':['model', ... ]}
    django_model_objects: dict
        Dictionary of the form {'modelname':<class='DjangoModel'>}
    models_docstrings: dict
        Dictionary of the form {'ModelName':"docstring"}
    foreignkeynames_models: dict
        Dictionary of the form {'foreignkeyfieldname':Modelname}

Author
-----
    emilledigital@gmail.com
"""
import os
import csv
from pprint import pprint
from operator import or_
from functools import reduce
from codegeneration.models import *
from codegeneration.helpers import *
from codegeneration.fragments import *

models_Foreignkeys       = {}
apps_Externmodels        = {}
foreignmodels_ParentApps = {}
apps_ViewSets            = {}
apps_Models              = {}
django_model_objects     = {}
models_docstrings        = {}
foreignkeynames_models   = {}

models_fakeDataStr                      = {}
models_nestedObjectPKs                  = {}
models_getForeignkeyObjectExpressions   = {}
models_assertNestedObjectExpressions    = {}
models_newFakeDataStr                   = {}
models_assertNestedObjectCounts         = {}
models_nestedEndpoints                  = {}
nestedModels_fakeDataStr                = {}
nestedModels_fakeDataStr_Test_Models    = {}
nestedModel_setupData                   = {}
nestedModel_PostValidData               = {}
nestedModel_getPK                       = {}

apps_ImportSerializers        = {}
apps_ImportViewSets           = {}
apps_ImportModels             = {}


def build_dict_apps_ViewSets(apps_models_dict):
    listOfApps = apps_Models.keys()

    for app in listOfApps:
        listOfModels = apps_Models[app]
        viewSets = []
        for model in listOfModels:
            viewSets += ["{}ViewSet".format(model)]

        apps_ViewSets[app] = ", ".join(viewSets)


def build_dict_apps_Models(models_dict):
    for v in models_dict.values():
        app = v.djangoapp
        model = v.modelname

        if app not in apps_Models:
            apps_Models[app] = [model]

        if model not in apps_Models[app]:
            apps_Models[app] += [model]


def build_dict_foreignmodels_Parentapps(models_dict):
    for M in models_dict.keys():
        if models_dict[M].isForeignkey:
            foreignmodels_ParentApps[M] = models_dict[M].djangoapp
        else:
            pass


def build_dict_apps_Externmodels(models_dict, apps_models_dict):
    apps_Nestedmodels = {}

    list_of_apps = apps_models_dict.keys()

    for app in list_of_apps:
        list_of_models = apps_Models[app]
        list_of_model_nested_models = [set(list(models_dict[_].foreignkey_names.keys())) for _ in list_of_models]
        set_of_nested_models = reduce(or_, list_of_model_nested_models)
        apps_Nestedmodels[app] = set_of_nested_models

        target_models = {}
        list_of_foreign_models = list(apps_Nestedmodels[app])
        for model in list_of_foreign_models:
            target_app = models_dict[model].djangoapp
            if target_app != app:
                if target_app not in target_models:
                    target_models[target_app] = [model]
                else:
                    target_models[target_app] += [model]

        apps_Externmodels[app] = target_models


def build_dict_models_Foreignkeys(models_dict, app_models_dict):
    listOfApps = app_models_dict.keys()

    for app in listOfApps:
        nestedObjects = None
        models_list = app_models_dict.get(app)
        for model in models_list:
            obj = django_model_objects[model]
            nesteds = list(obj.foreignkey_names.keys())

            if len(nesteds) != 0:
                nestedObjects = nesteds
                models_Foreignkeys[model] = nesteds


def set_up_import_statements(app_models_dict, models_foreignkeys_dict):

    listOfApps = app_models_dict.keys()

    for app in listOfApps:
        serializers = []
        models_list = app_models_dict.get(app)

        m = ', '.join(models_list)
        v = ', '.join(["{}ViewSet".format(_) for _ in models_list])

        for model in models_list:
            if model not in models_foreignkeys_dict:
                serializers.append("{}Serializer".format(model))
            else:
                serializers.append("{a}PostSerializer, {a}GetSerializer".format(a=model))
            #s = ', '.join(["{}Serializer".format(_) for _ in models_list])
            #a = "{a}PostSerializer, {a}GetSerializer".format(a=model)

        s = ', '.join(serializers)

        apps_ImportModels[app] = m
        apps_ImportViewSets[app] = v
        apps_ImportSerializers[app] = s
        #pprint (apps_ImportSerializers)


def build_fake_data_str_for_flat_model(model):
    res = ''
    for f in model.fields.keys():
        df = model.fields[f]
        if df not in ['UUIDField']:
            a = f
            b = f'{df}'
            res += test_api_flat_model_json_key_value.format(field=f, defaultVal=b)
    return res


def build_fake_data_json_for_test_setup(model):
    res = ''
    for f in model.fields.keys():
        df = model.fields[f]
        if df not in ['UUIDField']:
            a = f
            b = f'{df}'
            res += new_test_api_flat_model_json_key_value.format(field=f, defaultVal=b)
    return res


def build_fake_data_str_representations(models_dict):
    """Takes a collection of DjangoModel objects and builds a
    collection of fake data representations for each model to go
    in test_api.py.

    Parameters
    ----------
    models_dict : type
        Description of parameter `models_dict`.
    res_dict : type
        Description of parameter `res_dict`.

    Returns
    -------
    type
        Description of returned object.

    """
    for _ in django_model_objects.keys():
        st = ''
        exp_get_objects = ''
        exp_assert_nested = ''
        exp_nested_objectpk = ''
        exp_nested_fake = ''
        exp_nested_new_fake = ''
        exp_nestedObjectCount = ''
        exp_nestedEndpoint = ''
        exp_test_models_nested_fake = ''
        exp_nested_setup = ''
        exp_nested_post_valid_data = ''
        exp_nested_get_pk = ''

        uuidfield = None
        obj = django_model_objects[_]
        for f in obj.fields.keys():
            df = obj.fields[f]
            if df == 'UUIDField':
                uuidfield = f
            if df not in ['UUIDField']:
                if df != 'ForeignKey':
                    b = f'{df}'
                else:
                    c = foreignkeynames_models[f]
                    b = build_fake_data_str_for_flat_model(models_dict[c])
                    d = build_fake_data_json_for_test_setup(models_dict[c])

                    exp_nested_get_pk += new_test_api_setup_get_pk.format(
                        foreignmodel=helper_remove_underscore(f),
                        ForeignkeyModel=(foreignkeynames_models[f])
                    )

                    exp_nested_post_valid_data += new_test_api_setup_post.format(
                        foreignmodel=helper_remove_underscore(f)
                    )

                    exp_nested_setup += new_test_api_setup_data.format(
                        nested=f,
                        foreignmodel=helper_remove_underscore(f)
                    )

                    exp_test_models_nested_fake += test_api_nested_valid_data.format(
                        nested=f,
                        fields=b
                    )

                    exp_nested_fake += new_test_api_nested_valid_data.format(
                        nested=helper_remove_underscore(f),
                        fields=d
                    )

                    exp_nested_new_fake += test_api_updated_json_key.format(
                        nested=f,
                        fields=b
                    )
                    exp_get_objects += test_api_foreignkey_object_get.format(
                        foreignkey=f,
                        Model=obj.modelname,
                        foreignkeymodel=c.lower()
                    )
                    exp_assert_nested += test_api_assert_nested_object.format(
                        foreignkeymodel=c.lower()
                    )
                    exp_nested_objectpk += test_api_nestedObject_get_pk.format(
                        foreignkey=helper_remove_underscore(f),
                        ForeignkeyModel=c,
                    )
                    exp_nestedObjectCount += test_api_nested_object_count.format(
                        ForeignkeyModel=c
                    )
                    exp_nestedEndpoint += test_api_nested_endpoint.format(
                        nested=helper_remove_underscore(f),
                        plural_nested=helper_remove_underscore(helper_pluralize(f))
                    )

                    nestedModels_fakeDataStr[_] = exp_nested_fake
                    nestedModels_fakeDataStr_Test_Models[_] = exp_test_models_nested_fake

                st += test_api_json_key_value_line.format(field=f, defaultVal=b)

        models_fakeDataStr[_]                     = st
        models_getForeignkeyObjectExpressions[_]  = exp_get_objects
        models_assertNestedObjectExpressions[_]   = exp_assert_nested
        models_nestedObjectPKs[_]                 = exp_nested_objectpk
        models_newFakeDataStr[_]                  = test_api_updated_json_key_value.format(
                                                        model=obj.modelname.lower(),
                                                        modeluuidfield=uuidfield,
                                                        fields=exp_nested_new_fake
                                                    )
        models_assertNestedObjectCounts[_]        = exp_nestedObjectCount
        models_nestedEndpoints[_]                 = exp_nestedEndpoint
        nestedModel_setupData[_]                  = exp_nested_setup
        nestedModel_PostValidData[_]              = exp_nested_post_valid_data
        nestedModel_getPK[_]                      = exp_nested_get_pk


def build_extern_models_serializers(app):
    modelsStr = ""
    serializersStr = ""

    for eapp in list(apps_Externmodels[app].keys()):
        models = apps_Externmodels[app][eapp]

        modelsStr += test_api_head_extern_models.format(
            externapp=eapp,
            Models=', '.join(models)
        )

        serializersStr += test_api_head_extern_serializers.format(
            externapp=eapp,
            Serializers=', '.join(["{a}Serializer".format(a=_) for _ in models])
        )

    return modelsStr, serializersStr


def head_up_test_api_files(output_directory):
    listOfApps = apps_Models.keys()
    models_dict = django_model_objects

    for app in listOfApps:
        filepath = helper_return_filepath('test_api', app, output_directory)

        exp_extern_models = ""
        exp_extern_serializers = ""

        if len(  apps_Externmodels[app].values()  ) != 0:
            exp_extern_models, exp_extern_serializers = build_extern_models_serializers(app)

        helper_append_contents_to_file(
                    test_api_head.format(
                        djangoapp = app,
                        Models = apps_ImportModels[app],
                        Serializers = apps_ImportSerializers[app],
                        externModelsSegment=exp_extern_models,
                        externSerializersSegment=exp_extern_serializers,
                        Views = apps_ImportViewSets[app],
                    ),
                    filepath)


def add_to_docstring_collection(docstring_dict, m, docstring):
    """Builds docstring dictionary.

    Parameters
    ----------
    docstring_dict : dict
        Global docstring dictionary of the form {modelname:docstring}
    m : str
        Name of model
    docstring : str
        Docstring read in from the csv

    Returns
    -------
    None
        Function updates a global dictionary.

    """
    if docstring == None:
        return
    docstring_dict[m] = docstring


def save_to_foreignkey_Model_collection(fkey_model_dict, m):
    """Saves collection of foreignkey model names and their
    corresponding lower cased model field names.

    Parameters
    ----------
    fkey_model_dict : type
        Description of parameter `fkey_model_dict`.
    m : type
        Description of parameter `m`.

    Returns
    -------
    None
        Function updates a global dictionary

    """
    underscored = helper_return_underscore_separated_fieldname(m)
    fkey_model_dict[underscored] = m


def create_object_then_save(models_dict, docstring_dict, m, dapp, dfield, fname):
    """Creates an instance of DjangoModel and saves
    it to a collection.

    Parameters
    ----------
    models_dict : dict
        The global dict of the form {modelname:model}
    docstring_dict : dict
        The global dict of the form {modelname:docstring}
    m : str
        Model name
    dapp : str
        Django app name
    dfield : str
        Django model field eg. IntegerField, CharField etc.
    fname :
        Name of model field eg. created, author etc.

    Returns
    -------
    None
        Function updates some global collections.
    """
    obj = DjangoModel(m, dapp)
    obj.docstring = docstring_dict.get(m)
    obj.add_model_docstring_to_code_fragment()
    models_dict[m] = obj


def generate_test_api_files(models_dict, out_dir):

    head_up_test_api_files(out_dir)

    modelNames = django_model_objects.keys()
    models_foreignkeynames = helper_reverse(foreignkeynames_models)

    for M in modelNames:
        obj = django_model_objects[M]
        nesteds = obj.foreignkey_names.keys()

        if len(nesteds) == 0:
            valid = models_fakeDataStr[M]
            gotForeign = ""
            newfakedata = valid

            setupStr = new_test_api_is_not_nested_setup_segment.format(
                model=M.lower()
            )

            validModelStr = new_test_api_valid_model.format(
                model=helper_remove_underscore(M.lower()),
                validFields=valid
            )

            getStr = test_api_is_not_nested_get.format(
                model=M.lower(),
                Model=M
            )

        elif len(nesteds) != 0:
            valid = nestedModels_fakeDataStr[M]
            newfakedata = models_newFakeDataStr[M]
            gotForeign = valid

            setupStr = new_test_api_is_nested_setup_segment.format(
                postFields=nestedModel_PostValidData[M],
                foreignPKs=nestedModel_getPK[M],
                nestedFields=nestedModel_setupData[M],
                postData=new_test_api_setup_is_nested_post
            )

            validModelStr = ""

            getStr = new_test_api_is_nested_get.format(
                foreignfield=list(nesteds)[0].lower()
            )

        app = django_model_objects[M].djangoapp
        filepath = helper_return_filepath('test_api', app, out_dir)

        helper_append_contents_to_file((new_test_api_view.format(
            Model=M,
            plural_model=helper_pluralize(M.lower()),
            nestedEndpoints=models_nestedEndpoints[M],
            model=M.lower(),
            validModel=validModelStr,
            foreignFakeData=gotForeign,
            setupSegment=setupStr,
            get_foreignkey_objects=models_getForeignkeyObjectExpressions[M],
            assertNestedObjects=models_assertNestedObjectExpressions[M],
            isnestedGetSegment=getStr,
            nestedObject_pks=models_nestedObjectPKs[M],
            new_fields=newfakedata,
            assert_nested_object_counts=models_assertNestedObjectCounts[M],
            deleteRequest=new_test_api_is_delete_instance,
        )),
        filepath)


def generate_urls_files(models_dict, out_dir):
    """Takes a dict containing all the registered models
    and returns a urls.py file for the each app in the project.
    """
    urls_contents = {}
    listOfApps = apps_Models.keys()

    for app in listOfApps:
        st = ""
        listOfModels = apps_Models[app]

        for m in listOfModels:
            st += urls_register_router.format(
                                plural_model=helper_pluralize(m.lower()),
                                Model=m
                            )

        urls_contents[app] = urls_router_skeleton.format(
                                djangoapp=app,
                                ViewSets=apps_ViewSets[app]+'\n',
                                contents=st
                                )

    for app in urls_contents.keys():
        urls_file = helper_return_filepath('urls', app, out_dir)
        helper_append_contents_to_file(urls_contents[app], urls_file)


def generate_api_files(out_dir):
    listOfApps = apps_Models.keys()
    for app in listOfApps:
        serializers_contents = ""
        views_contents = ""
        serializers = helper_return_filepath('serializers', app, out_dir)
        views       = helper_return_filepath('views', app, out_dir)

        exp_extern_models = ""
        exp_extern_serializers = ""

        if len(  apps_Externmodels[app].values()  ) != 0:
            exp_extern_models, exp_extern_serializers = build_extern_models_serializers(app)

        serializers_contents += api_serializers_head.format(
            externModelsSegment=exp_extern_models,
            externSerializersSegment=exp_extern_serializers,
            djangoapp=app,
            Models=apps_ImportModels[app]
        )

        views_contents += api_views_head.format(
            djangoapp=app,
            Models=apps_ImportModels[app],
            Serializers=apps_ImportSerializers[app]
        )

        for obj in apps_Models[app]:
            exp_nested = ""
            exp_create_nested_data = ""
            exp_create_nested_try = ""
            exp_create_nested_instance = ""
            exp_validated_field = ""
            exp_instance_field = ""
            exp_instance_save = ""
            exp_api_field_get = ""
            exp_pk_fields = ""
            exp_nested_pk = ""

            fkey_names_dict = django_model_objects[obj].foreignkey_names
            foreignkey_fields = fkey_names_dict.values()

            if (len(foreignkey_fields)) == 0:
                views_contents += api_views_model_viewset.format(Model=obj)
                serializers_contents += api_serializers.format(Model=obj)

            else:
                views_contents += api_views_model_nested_viewset.format(Model=obj)

                for F in fkey_names_dict.keys():
                    f = fkey_names_dict[F]
                    nestedModelFields = django_model_objects[F].fields.keys()

                    for modelfield in nestedModelFields:
                        exp_api_field_get += api_instance_field_get.format(
                            field=f,
                            attr=modelfield
                        )
                    exp_nested_pk += new_api_serializers_primary_key_field.format(
                        foreignfield=f,
                        Foreignmodel=F
                    )

                    exp_nested += api_serializers_nested_object.format(
                        field=f,
                        Field=F
                    )
                    exp_create_nested_data += api_nested_data_pop.format(
                        field=f,
                        Field=F
                    )
                    exp_create_nested_try += api_nested_try_block.format(
                        field=f,
                        Field=F
                    )
                    exp_create_nested_instance += api_create_with_nested.format(
                        field=f
                    )
                    exp_validated_field += api_validated_field.format(
                        field=f
                    )
                    exp_instance_field += api_instance_field.format(
                        field=f
                    )

                    exp_instance_save += api_instance_save.format(
                        field=f
                    )


                views_contents += new_api_views_override_get_serializer.format(
                    Model=obj
                )

                serializers_contents += new_api_serializers_post_serializer.format(
                    Model=obj,
                    primaryKeyFields=exp_nested_pk
                )

                serializers_contents += api_serializers_nested_objects.format(
                    Model=obj,
                    nestedObjects=exp_nested,
                )

                serializers_contents += api_override_create.format(
                    nestedData=exp_create_nested_data,
                    nestedTryBlocks=exp_create_nested_try,
                    nestedInstances=exp_create_nested_instance,
                    model = obj.lower(),
                    Model= obj,
                )

                serializers_contents += api_override_update.format(
                    validatedData=exp_validated_field,
                    instanceFields=exp_instance_field,
                    instanceFieldGets=exp_api_field_get,
                    instanceSaves=exp_instance_save
                )

        helper_append_contents_to_file(serializers_contents, serializers)
        helper_append_contents_to_file(views_contents, views)


def generate_admin_file(out_dir, apps_models_dict, models_dict):
    listOfApps = apps_Models.keys()
    for app in listOfApps:
        filepath = helper_return_filepath('admin', app, out_dir)
        helper_append_contents_to_file(
            admin_head.format(
                djangoapp=app,
                Models=apps_ImportModels[app]
            ),
            filepath
        )

        listOfModels = apps_Models[app]
        contents = ""
        for _ in listOfModels:
            contents += admin_class.format(Model=_,)

        helper_append_contents_to_file(
            contents,
            filepath
        )


def generate_test_models_files(out_dir, apps_models_dict, models_dict):
    listOfApps = apps_models_dict.keys()

    modelsWithForeignKeys = {}
    for _ in models_dict.keys():
        fieldsDict = models_dict[_].fields
        for f in fieldsDict.keys():
            if fieldsDict[f] == 'ForeignKey':
                if _ not in modelsWithForeignKeys.keys():
                    modelsWithForeignKeys[_] = [f]
                else:
                    modelsWithForeignKeys[_] += [f]

    foreignkeysFields = {}
    for _ in modelsWithForeignKeys.values():
        #print (_)
        for n in _:
            #print ('\t', n)
            N = foreignkeynames_models[n]
            fieldObj = models_dict[N].fields
            fields = fieldObj.keys()
            foreignkeysFields[n] = list(_ for _ in fields if fieldObj[_] != "UUIDField")

    for app in listOfApps:
        filepath = helper_return_filepath('test_models', app, out_dir)

        helper_append_contents_to_file(
            test_models_head.format(
                djangoapp=app,
                Models=apps_ImportModels[app]
            ),
            filepath
        )

        listOfModels = apps_Models[app]

        exp_modelclasses = ""

        for M in listOfModels:
            #print (M)
            obj = models_dict.get(M)
            nesteds = obj.foreignkey_names.keys()

            # We need for each foreignkey, the fields
            # FOR A GIVEN MODEL, get the foreign key fields

            # for each field, we need that many tests build out
            # for eaqch test we need a string built out, consisting of the two fields

            exp_models_lookup_segment = ""
            exp_nested_fields = ""

            exp_setters = ""
            exp_getters = ""

            list_of_foreign_keys_per_model = []

            try:
                list_of_foreign_keys_per_model = modelsWithForeignKeys[M]
            except Exception as e:
                pass
            else:
                list_of_foreign_keys_per_model = modelsWithForeignKeys[M]

                for fld in list_of_foreign_keys_per_model:

                    exp_setters += test_models_set_foreign_field.format(
                        model=M.lower(),
                        field=fld,
                        instance=helper_remove_underscore(fld),
                    )
                    exp_getters += test_models_get_foreign_field.format(
                        Model=helper_return_camel_case_foreign_key_modelname(fld),
                        model=helper_remove_underscore(fld),
                        # TODO: Introspect this instead
                        fuuid='{}_id'.format(helper_remove_underscore(fld))
                    )


                for fld in list_of_foreign_keys_per_model:

                    corresponding_model = foreignkeynames_models[fld]
                    a = corresponding_model

                    fields_for_corresponding_model = models_dict[a].fields.keys()
                    b = list(fields_for_corresponding_model)

                    exp_nested_lookups = ""

                    for attr in b:
                        if models_dict[a].fields[attr] != "UUIDField":
                            exp_nested_lookups += test_models_nested_lookup.format(
                                model=a.lower(),
                                nestedmodel=helper_return_underscore_separated_fieldname(a),
                                field=attr
                            )

                    exp_models_lookup_segment += test_models_nested_lookup_segment.format(
                        model=a.lower(),
                        Model=a,
                        nestedLookups=exp_nested_lookups
                    )

            for fld in list_of_foreign_keys_per_model:
                exp_nested_fields += test_models_test_foreign_fields.format(
                    getForeigns=exp_getters,
                    setForeigns=exp_setters,
                    model=M.lower(),
                    Model=M,
                    field=helper_return_underscore_separated_fieldname(fld),
                    instance=helper_remove_underscore(fld)
                )

            ####################################################

            #print ('===========\n', exp_nested_fields)
            """
            if M == 'ScrapeJobBoard':
                print (exp_nested_fields)
            """
            ####################################################

            exp_fieldtests = ""
            exp_attrs = ""

            fields_types = obj.fields
            listOfFields = fields_types.keys()

            for f in listOfFields:

                field_type = fields_types[f]
                if field_type == 'UUIDField':
                    ufield = f

                if field_type != 'UUIDField':
                    exp_attrs += test_models_set_attr.format(
                        attr=f
                    )

                exp_fieldtests += test_models_test_field.format(
                    model=M.lower(),
                    Model=M,
                    uuidfield=ufield,
                    field=f
                )

            if len(nesteds) == 0:
                testFieldsSegment = exp_fieldtests
                setupStr = test_models_setUp
                valid = models_fakeDataStr[M]
                newfakedata = valid
            else:
                testFieldsSegment = exp_nested_fields
                setupStr = test_models_setUp_nested
                valid = nestedModels_fakeDataStr_Test_Models[M]
                newfakedata = models_newFakeDataStr[M]

            setup = setupStr.format(
                fields=valid,
                Model=M,
                attrs=exp_attrs,
                lookups=exp_models_lookup_segment
            )


            exp_modelclasses += test_models_class.format(
                setUp=setup,
                Model=M,
                testFields=testFieldsSegment
            )

        helper_append_contents_to_file(
            exp_modelclasses,
            filepath
        )


def generate_models_files(out_dir, apps_models_dict, models_dict):
    listOfApps = apps_models_dict.keys()

    for app in listOfApps:
        filepath = helper_return_filepath('models', app, out_dir)

        helper_append_contents_to_file(
            models_head.format(djangoapp=app),
            filepath
            )

        listOfModels = apps_Models[app]
        exp_models = ""
        for M in listOfModels:
            name = 'PLACEHOLDER'
            obj = models_dict.get(M)
            fields_types = obj.fields
            listOfFields = fields_types.keys()
            exp_fields = ""
            for f in listOfFields:
                field_type = fields_types[f]
                if field_type == 'CharField':
                    name = f

                if field_type == 'ForeignKey':
                    fnapp = obj.foreignkey_parent.get(f)
                    fmodel = foreignkeynames_models[f]
                else:
                    fnapp = ''
                    fmodel = ''

                temp = models_model_fields.get(field_type)

                exp_fields += temp.format(
                    field=f,
                    foreignapp=fnapp,
                    foreignmodel=fmodel,
                )

            exp_models += models_model.format(
                docstring=models_docstrings[M],
                Model=M,
                modelFields=exp_fields,
                nameField=name
            )


        helper_append_contents_to_file(
            exp_models,
            filepath
            )


def generate_models(out_dir, app_name_list, filepath_dict, djangoapps_inputfiles):
    """Loops over the csv rows and compiles global and
    temporary collections.

    Parameters
    ----------
    inp : str, Path
        The path to a csv file containing the data for the models.
    djangoapp : str
        Name of the Django app.

    Returns
    -------
    Integer
        Number of models detected in each CSV file.
    """

    for tup in djangoapps_inputfiles:
        appname = tup[0]
        input_csv = tup[1]
        filepath_dict[appname] = helper_return_models_files(appname, out_dir)
        app_name_list.append(appname)

        with open(input_csv) as fd:
            rdr = csv.reader(fd, delimiter=',')
            next(rdr)

            for row in rdr:
                djangofield = row[0]
                fieldname = row[1]
                docstring = row[2]

                if djangofield == 'models.Model':
                    model_name = fieldname

                    add_to_docstring_collection(models_docstrings, model_name, docstring)

                    save_to_foreignkey_Model_collection(foreignkeynames_models, model_name)

                    create_object_then_save(
                        django_model_objects,
                        models_docstrings,
                        model_name,
                        appname,
                        djangofield,
                        fieldname
                    )


                list_of_models = foreignkeynames_models.values()

                if fieldname in list_of_models:
                    curr = django_model_objects.get(fieldname)

                if djangofield == 'ForeignKey':
                    fkey_model_name = foreignkeynames_models.get(fieldname)
                    foreignkeymodel = django_model_objects.get(fkey_model_name)
                    curr.add_foreign_keys(foreignkeymodel)

                if fieldname not in list_of_models:
                    curr.add_field(djangofield, fieldname)

    models_detected = len(django_model_objects.keys())
    return models_detected


def generate_code(output_dir, *djangoapps_inputfiles):
    """Takes a directory and an arbitary number of tuples
    and generates code in appname_models.py and appname_test_models.py.

    Parameters
    ----------
    output_dir : 'str' or Path-like object
        The target directory for saving the output of the code generator.

    *djangoapps_inputfiles : List[tuple]
        tuples of the form ('appname', 'input file')

    Returns
    -------
    Integer
        Number of files generated by generate_code
    """
    appnames = []
    app_modeltestModel = {}

    generate_models(output_dir, appnames, app_modeltestModel, djangoapps_inputfiles)

    build_dict_apps_Models(django_model_objects)

    build_dict_models_Foreignkeys(django_model_objects, apps_Models)

    build_dict_apps_Externmodels(django_model_objects, apps_Models)

    set_up_import_statements(apps_Models, models_Foreignkeys)

    build_dict_apps_ViewSets(apps_Models)

    build_fake_data_str_representations(django_model_objects)

    generate_models_files(output_dir, apps_Models, django_model_objects)

    generate_test_models_files(output_dir, apps_Models, django_model_objects)

    generate_admin_file(output_dir, apps_Models, django_model_objects)

    generate_urls_files(django_model_objects, output_dir)

    generate_api_files(output_dir)

    generate_test_api_files(django_model_objects, output_dir)

    created = len(os.listdir(output_dir))
    return created


if __name__ == '__main__':
    pass

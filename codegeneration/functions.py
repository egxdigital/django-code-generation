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
import pprint
from codegeneration.models import *
from codegeneration.helpers import *
from codegeneration.fragments import *

apps_ViewSets           = {}
apps_Models             = {}
django_model_objects    = {}
models_docstrings       = {}
foreignkeynames_models  = {}

models_fakeDataStr                      = {}
models_nestedObjectPKs                  = {}
models_getForeignkeyObjectExpressions   = {}
models_assertNestedObjectExpressions    = {}
models_newFakeDataStr                   = {}
models_assertNestedObjectCounts         = {}
models_nestedEndpoints                  = {}
nestedModels_fakeDataStr                = {}

apps_ImportSerializers        = {}
apps_ImportViewSets           = {}
apps_ImportModels             = {}


def build_dict_apps_ViewSets(apps_models_dict):
    listOfApps = apps_Models.keys()

    for app in listOfApps:
        listOfModels = apps_Models[app]
        viewSets = []
        for model in listOfModels:
            #print ('\t', model)
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


def set_up_import_statements(app_models_dict):
    listOfApps = apps_Models.keys()
    for app in listOfApps:
        models_list = app_models_dict.get(app)
        m = ', '.join(models_list)
        s = ', '.join(["{}Serializer".format(_) for _ in models_list])
        v = ', '.join(["{}ViewSet".format(_) for _ in models_list])

        apps_ImportModels[app] = m
        apps_ImportSerializers[app] = s
        apps_ImportViewSets[app] = v


def build_fake_data_str_for_flat_model(model):
    res = ''
    for f in model.fields.keys():
        df = model.fields[f]
        if df not in ['UUIDField']:
            a = f
            b = f'{df}'
            res += test_api_flat_model_json_key_value.format(field=f, defaultVal=b)
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
                    exp_nested_fake += test_api_nested_valid_data.format(
                        nested=f,
                        fields=b
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
                        foreignkey=f,
                        ForeignkeyModel=c,
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


def head_up_test_api_files(output_directory):
    listOfApps = apps_Models.keys()

    for app in listOfApps:
        filepath = helper_return_filepath('test_api', app, output_directory)

        helper_append_contents_to_file(
                    test_api_head.format(
                        djangoapp = app,
                        Models = apps_ImportModels[app],
                        Serializers = apps_ImportSerializers[app],
                        Views = apps_ImportViewSets[app],
                    ),
                    filepath)


def write_testcases_to_test_api_files(output_directory):
    modelNames = django_model_objects.keys()

    for M in modelNames:
        obj = django_model_objects[M]
        nesteds = obj.foreignkey_names.keys()

        if len(nesteds) == 0:
            valid = models_fakeDataStr[M]
            newfakedata = valid
        else:
            valid = nestedModels_fakeDataStr[M]
            newfakedata = models_newFakeDataStr[M]

        app = django_model_objects[M].djangoapp
        filepath = helper_return_filepath('test_api', app, output_directory)

        helper_append_contents_to_file((test_api_view.format(
                        model=M.lower(),
                        Model=M,
                        nestedEndpoints=models_nestedEndpoints[M],
                        validFields=valid,
                        get_foreignkey_objects=models_getForeignkeyObjectExpressions[M],
                        assertNestedObjects=models_assertNestedObjectExpressions[M],
                        nestedObject_pks=models_nestedObjectPKs[M],
                        new_fields=newfakedata,
                        plural_model=helper_pluralize(M.lower()),
                        assert_nested_object_counts=models_assertNestedObjectCounts[M],
                    )),
                    filepath)


def build_docstring_collection(docstring_dict, m, docstring):
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
    obj.add_line_to_models_code_fragment(dfield, fname)
    obj.add_line_to_test_models_code_fragment(dfield, fname)
    models_dict[m] = obj


def generate_test_api_files(models_dict, out_dir):

    build_fake_data_str_representations(models_dict)

    head_up_test_api_files(out_dir)

    write_testcases_to_test_api_files(out_dir)


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

        serializers_contents += api_serializers_head.format(djangoapp=app, Models=apps_ImportModels[app])
        views_contents += api_views_head.format(djangoapp=app, Models=apps_ImportModels[app], Serializers=apps_ImportSerializers[app])

        for obj in apps_Models[app]:
            exp_nested = ""
            exp_create_nested_data = ""
            exp_create_nested_try = ""
            exp_create_nested_instance = ""
            exp_validated_field = ""
            exp_instance_field = ""
            exp_instance_save = ""
            exp_api_field_get = ""

            views_contents += api_views_model_viewset.format(Model=obj)

            fkey_names_dict = django_model_objects[obj].foreignkey_names
            foreignkey_fields = fkey_names_dict.values()

            if (len(foreignkey_fields)) == 0:
                serializers_contents += api_serializers.format(Model=obj)

            else:
                for F in fkey_names_dict.keys():
                    f = fkey_names_dict[F]
                    nestedModelFields = django_model_objects[F].fields.keys()

                    for modelfield in nestedModelFields:
                        exp_api_field_get += api_instance_field_get.format(
                            field=f,
                            attr=modelfield
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


def generate_models(inp, djangoapp):
    """Takes a file path and a Django app name and populates
    global data structures django_model_objects and
    foreignkeynames_models

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

    with open(inp) as fd:
        rdr = csv.reader(fd, delimiter=',')
        next(rdr)

        for row in rdr:
            djangofield = row[0]
            fieldname = row[1]
            docstring = row[2]

            if djangofield == 'models.Model':
                model_name = fieldname

                build_docstring_collection(models_docstrings, model_name, docstring)

                save_to_foreignkey_Model_collection(foreignkeynames_models, model_name)

                create_object_then_save(
                    django_model_objects,
                    models_docstrings,
                    model_name,
                    djangoapp,
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

    filepaths = {}
    appnames = []

    for tup in djangoapps_inputfiles:
        appname = tup[0]
        input_csv = tup[1]
        filepaths[appname] = helper_return_models_files(appname, output_dir)
        appnames.append(appname)
        generate_models(input_csv, appname)

    for appname in appnames:
        dest_models = filepaths[appname][0]
        dest_test_models = filepaths[appname][1]
        helper_prepare_models_py(dest_models)

    for model in django_model_objects.keys():
        m = django_model_objects.get(model)

        for appname in appnames:
            if m.djangoapp == appname:
                models_file = filepaths[appname][0]
                test_models_file = filepaths[appname][1]

                helper_append_contents_to_file(m.models_code_fragment, models_file)

                helper_append_contents_to_file(m.test_models_code_fragment, test_models_file)

    # TODO: Refactor
    for appname in appnames:
        models = {}

        for model in django_model_objects.values():
            if model.djangoapp == appname:
                models[helper_return_underscore_separated_fieldname(model.modelname)] = model.modelname

        helper_prepare_test_models_py(appname, models, filepaths[appname][1])

    build_dict_apps_Models(django_model_objects)

    build_dict_apps_ViewSets(apps_Models)

    set_up_import_statements(apps_Models)

    generate_urls_files(django_model_objects, output_dir)

    generate_api_files(output_dir)

    generate_test_api_files(django_model_objects, output_dir)

    created = len(os.listdir(output_dir))
    return created


if __name__ == '__main__':
    pass

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
    apps_models: dict
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
apps_models             = {}
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



def build_fake_data_str_for_flat_model(model):
    res = ''
    for f in model.fields.keys():
        df = model.fields[f]
        if df not in ['UUIDField']:
            a = f
            b = f'{df}'
            res += test_api_flat_model_json_key_value.format(field=f, defaultVal=b)
    return res


def build_fake_data_str_representation(models_dict):
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
                    exp_nested_fake         += test_api_updated_json_key.format(
                                                nested=f,
                                                fields=b)
                    exp_get_objects         += test_api_forignkey_object_get.format(
                                                foreignkey=f,
                                                ForeignkeyModel=c,)
                    exp_assert_nested       += test_api_assert_nested_object.format(
                                                foreignkey=f,
                                                ForeignkeyModel=c,)
                    exp_nested_objectpk     += test_api_nestedObject_get_pk.format(
                                                foreignkey=f,
                                                ForeignkeyModel=c,)
                    exp_nestedObjectCount   += test_api_nested_object_count.format(
                                                ForeignkeyModel=c)
                    exp_nestedEndpoint      += test_api_nested_endpoint.format(
                                                nested=helper_remove_underscore(f),
                                                plural_nested=helper_remove_underscore(helper_pluralize(f)))

                st += test_api_json_key_value_line.format(field=f, defaultVal=b)

        models_fakeDataStr[_]                     = st
        models_getForeignkeyObjectExpressions[_]  = exp_get_objects
        models_assertNestedObjectExpressions[_]   = exp_assert_nested
        models_nestedObjectPKs[_]                 = exp_nested_objectpk
        models_newFakeDataStr[_]                  = test_api_updated_json_key_value.format(
                                                        model=obj.modelname.lower(),
                                                        modeluuidfield=uuidfield,
                                                        fields=exp_nested_fake
                                                    )
        models_assertNestedObjectCounts[_]        = exp_nestedObjectCount
        models_nestedEndpoints[_]                 = exp_nestedEndpoint


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
    build_fake_data_str_representation(models_dict)

    for M in django_model_objects.keys():
        obj = django_model_objects[M]
        nesteds = obj.foreignkey_names.keys()

        if len(nesteds) == 0:
            fakedata = models_fakeDataStr[M]
        else:
            fakedata = models_newFakeDataStr[M]

        app = django_model_objects[M].djangoapp
        filepath = helper_return_filepath('test_api', app, out_dir)

        helper_append_contents_to_file((test_api_view_nested_model.format(
                    model=M.lower(),
                    Model=M,
                    nestedEndpoints=models_nestedEndpoints[M],
                    fields=models_fakeDataStr[M],
                    get_foreignkey_objects=models_getForeignkeyObjectExpressions[M],
                    assertNestedObjects=models_assertNestedObjectExpressions[M],
                    nestedObject_pks=models_nestedObjectPKs[M],
                    new_fields=fakedata,
                    plural_model=helper_pluralize(M.lower()),
                    assert_nested_object_counts=models_assertNestedObjectCounts[M],
                    )),
                    filepath)


def generate_urls_py_files(models_dict, out_dir, skeleton_str, format_str):
    """Takes a dict containing all the registered models
    and returns a urls.py file for the each app in the project.
    """
    urls_contents = {}

    for v in models_dict.values():
        app = v.djangoapp
        model = v.modelname

        if app not in apps_models:
            apps_models[app] = [model]

        if model not in apps_models[app]:
            apps_models[app] += [model]

    listOfApps = apps_models.keys()

    for app in listOfApps:
        #print (app)
        listOfModels = apps_models[app]
        viewSets = []
        for model in listOfModels:
            #print ('\t', model)
            viewSets += ["{}ViewSet".format(model)]

        apps_ViewSets[app] = ", ".join(viewSets)

    for app in listOfApps:
        #print (_)
        st = ""
        listOfModels = apps_models[app]

        for m in listOfModels:
            #print (m)
            st += format_str.format(
                                plural_model=helper_pluralize(m.lower()),
                                Model=m
                            )

        urls_contents[app] = skeleton_str.format(
                                djangoapp=app,
                                ViewSets=apps_ViewSets[app]+'\n',
                                contents=st
                                )

    for app in urls_contents.keys():
        urls_file = helper_return_filepath('urls', app, out_dir)
        helper_append_contents_to_file(urls_contents[app], urls_file)


def generate_api(app_models_dict, out_dir):
    """Takes a list of appnames and generates api/urls.py, api/serializers.py
    and api/views.py"""
    listOfApps = app_models_dict.keys()

    for appname in listOfApps:
        pass

        """
        models_list = app_models_dict.get(appname)
        m = ', '.join(models_list)
        s = ', '.join(["{}Serializer".format(_) for _ in models_list])
        v = ', '.join(["{a}ListCreateAPIView, {a}RetrieveUpdateDestroyAPIView".format(a=_) for _ in models_list])

        file_path = helper_return_filepath('test_api', appname, out_dir)



        with open(file_path, 'a') as serializers:
            serializers.write(test_api_head.format(
                    djangoapp=appname,
                    Models=m,
                    Serializers=s,
                    Views=v,
                    )
                )

            for _ in models_list:
                serializers.write(test_api_list_create.format(
                            models = helper_pluralize(_.lower()),
                            model=_.lower(),
                            Model=_,
                            lookup_field='PLACEHOLDER',
                        ))
                serializers.write(test_api_retrieve_update.format(
                                models = helper_pluralize(_.lower()),
                                model=_.lower(),
                                Model=_,
                                lookup_field='PLACEHOLDER',
                            ))
        """


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

    for appname in appnames:
        models = {}

        for model in django_model_objects.values():
            if model.djangoapp == appname:
                models[helper_return_underscore_separated_fieldname(model.modelname)] = model.modelname

        helper_prepare_test_models_py(appname, models, filepaths[appname][1])

    generate_urls_py_files(django_model_objects, output_dir, urls_router_skeleton, urls_register_router)

    #generate_api(apps_models, output_dir)

    generate_test_api_files(django_model_objects, output_dir)

    created = len(os.listdir(output_dir))
    return created


if __name__ == '__main__':
    pass

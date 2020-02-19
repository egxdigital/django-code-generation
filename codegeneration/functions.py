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


apps_models             = {}
django_model_objects    = {}
models_docstrings       = {}
foreignkeynames_models  = {}


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


def generate_urls_py_files(models_dict, out_dir, skeleton_str, format_str):
    """Takes a dict containing all the registered models
    and returns a urls.py file for the each app in the project.
    """
    for v in models_dict.values():
        app = v.djangoapp
        model = v.modelname

        if app not in apps_models:
            apps_models[app] = [model]

        if model not in apps_models[app]:
            apps_models[app] += [model]

    urls_contents = {}

    for _ in apps_models.keys():
        st = ""
        for m in apps_models[_]:
            st += format_str.format(
                            models = helper_pluralize(m.lower()),
                            model=m.lower(),
                            Model=m,
                            lookup_field="PLACEHOLDER"
                            )

            urls_contents[_] = skeleton_str.format(djangoapp=_, contents=st)

    for app in urls_contents.keys():
        urls_file = helper_return_filepath('urls', app, out_dir)

        helper_append_contents_to_file(urls_contents[app], urls_file)


def generate_api(app_models_dict, out_dir):
    """Takes a list of appnames and generates api/serializers.py
    and api/views.py"""

    for appname in app_models_dict.keys():
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


    generate_urls_py_files(django_model_objects, output_dir, urls_skeleton, urls_url_pattern)

    generate_api(apps_models, output_dir)

    created = len(os.listdir(output_dir))
    return created


if __name__ == '__main__':
    pass

"""Codegeneration Helpers

This module contains helper functions for text processing,
directory and file handling tasks.

Author
-----
    emilledigital@gmail.com
"""

def helper_remove_underscore(inp):
    if '_' in inp:
        return ''.join(inp.split('_'))
    return inp

def helper_pluralize(inp):
    """Takes a string and returns the plural form.
    Assumes that there are only two plural forms
    for all the words to be passed.
    """
    if inp[-1] == 'y':
        return inp[:-1] + 'ies'
    return inp + 's'


def helper_return_underscore_separated_fieldname(inp):
    """Takes a CamelCase or uppercase string and returns an
    underscore separated, lower case version of the string.

    Parameters
    ----------
    inp : str
        the camel case string to be converted to lower case

    Returns
    -------
    String
        Example: 'app_model', 'job_board', 'jobpost'

    """
    import re
    splitted = re.sub(r"([A-Z])", r" \1", inp).split()
    res = '_'.join(splitted)
    return res.lower()


def helper_return_camel_case_foreign_key_modelname(inp):
    """Takes a string of the form 'job_board' and returns a string
    of the form JobBoard

    Parameters
    ----------
    inp : str
        Example: 'job_board'

    Returns
    -------
    String
        Example JobBoard
    """

    if '_' not in inp:
        return inp.capitalize()

    else:
        import re
        splitted = re.sub(r"([A-Z])", r" \1", inp).split('_')
        res = ''.join([_.capitalize() for _ in splitted])
        return res


def helper_append_contents_to_file(contents, file):
    with open(file, 'a') as fd:
        fd.write(contents)


def helper_prepare_models_py(dest):
    """Heads up models.py with standard import statements

    Parameters
    ----------
    dest : type
        Description of parameter `dest`.

    Returns
    -------
    type
        TODO: Lookup how to apply error handling to file I/O operations
    """

    with open(dest, 'w+') as py:
        py.write('from django.db import models\nimport uuid')


def helper_prepare_test_models_py(appname, models, dest):
    """Takes an Django app name, models dictionary of the form
    {job_board:JobBoard} and the target test_models.py and
    re-writes the file with the required imports.

    Parameters
    ----------
    appname : type
        Description of parameter `appname`.
    models : type
        Description of parameter `models`.
    dest : type
        Description of parameter `dest`.

    Returns
    -------
    type
        Description of returned object.

    """

    with open(dest, 'r') as testpy:
        contents = testpy.read()

    with open(dest, 'w') as testpy:
        testpy.write('from django.test import TestCase\nimport datetime\nfrom model_mommy import mommy\n')
        testpy.write('from {}.models import {}\n'.format(appname, ','.join(models.values())))
        testpy.write(contents)


def helper_return_filepath(inp, djangoapp, dir):
    """Takes a file name, a Django app name and an
    output directory path and returns a file path.

    Parameters
    ----------
    inp : str

    djangoapp : type
        Description of parameter `djangoapp`.
    dir : type
        Description of parameter `dir`.

    Returns
    -------
    type
        Description of returned object.

    """
    import os
    filepath = '{}/{}_{}.py'.format(os.path.abspath(dir), djangoapp, inp)
    return filepath


def helper_return_models_files(djangoapp, dir):
    """Takes Django app name and destination directory
    and returns a filepath as a string

    Parameters
    ----------
    djangoapp : str
        Name of the Django app to which the file belongs
    dest_dir : str, Path
        Absolute path to the output directory

    Returns
    -------
    Tuple
        (models.py file path, test_models.py filepath)

    """
    return helper_return_filepath('models', djangoapp, dir), helper_return_filepath('test_models', djangoapp, dir)

"""Codegeneration Helpers

This module contains helper functions for text processing,
directory and file handling tasks.

Author
-----
    emilledigital@gmail.com
"""

def helper_return_underscore_separated_fieldname(str):
    """Takes a CamelCase or uppercase string and returns an
    underscore separated, lower case version of the string.

    Parameters
    ----------
    str : str
        the camel case string to be converted to lower case

    Returns
    -------
    String
        Example: 'app_model', 'job_board', 'jobpost'

    """
    import re
    splitted = re.sub(r"([A-Z])", r" \1", str).split()
    res = '_'.join(splitted)
    return res.lower()


def helper_return_camel_case_foreign_key_modelname(str):
    """Takes a string of the form 'job_board' and returns a string
    of the form JobBoard

    Parameters
    ----------
    str : str
        Example: 'job_board'

    Returns
    -------
    String
        Example JobBoard
    """

    if '_' not in str:
        return str.capitalize()

    else:
        import re
        splitted = re.sub(r"([A-Z])", r" \1", str).split('_')
        res = ''.join([_.capitalize() for _ in splitted])
        return res


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


def helper_return_dest_models_py_filepath(djangoapp, dest_dir):
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

    import os
    output_dir =  os.path.abspath(dest_dir)
    dest_file = '{}/{}_models.py'.format(output_dir, djangoapp)
    dest_test_file = '{}/{}_test_models.py'.format(output_dir, djangoapp)

    return dest_file, dest_test_file

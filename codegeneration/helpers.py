def helper_return_underscore_separated_fieldname(str):
    """Takes a CamelCase string and returns an underscore separated
    lower case version of the string"""
    import re
    splitted = re.sub(r"([A-Z])", r" \1", str).split()
    res = '_'.join(splitted)
    return res.lower()


def helper_return_foreign_key_model(str):
    """Takes a string of the form 'job_board' and returns a string
    of the form JobBoard"""
    if '_' not in str:
        return str.capitalize()

    else:
        import re
        splitted = re.sub(r"([A-Z])", r" \1", str).split('_')
        res = ''.join([_.capitalize() for _ in splitted])
        return res


def helper_prepare_models_py(dest):
    """Heads up models.py including docstring"""

    with open(dest, 'w+') as py:
        py.write('from django.db import models\nimport uuid\n')


def helper_prepare_test_models_py(appname, models, dest):
    """Takes an Django app name, models dictionary of the form
    {job_board:JobBoard} and the target test_models.py and
    re-writes the file with the required imports."""

    with open(dest, 'r') as testpy:
        contents = testpy.read()

    with open(dest, 'w') as testpy:
        testpy.write('from django.test import TestCase\nimport datetime\nfrom model_mommy import mommy\n')
        testpy.write('from {}.models import {}\n'.format(appname, ','.join(models.values())))
        testpy.write(contents)


def helper_return_dest_models_py_filepath(djangoapp, dest_dir):
    """Takes Django app name and destination directory
    and returns a filepath as a string"""
    import os
    output_dir =  os.path.abspath(dest_dir)
    dest_file = '{}/{}_models.py'.format(output_dir, djangoapp)
    dest_test_file = '{}/{}_test_models.py'.format(output_dir, djangoapp)

    return dest_file, dest_test_file

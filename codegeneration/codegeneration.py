"""Codegeneration

This module contains the main function for running the code generator.
You should be able to call this program from the command-line.

Assumptions:
    1. Input CSV files are in a directory called 'data' which is located
    at the top level of the current directory.

    2. The appnames are fed to the program by order of Django model
    parentage. So app2 may import foreign keys from app1 and so on.

    3. ...

Usage
-----
    Command line(coming soon):
        $ python3 -m codegeneration output_dirrectory app1 [app2 app3 ...]

Author
-----
    emilledigital@gmail.com

"""
import pprint
from codegeneration.functions import *


def main(output_dir, djangoappnames:list):
    """Takes a target directory and a list of tuples of and generates
    code in the target directory.

    Parameters
    ----------
    output_dir : 'str' or Path-like object
        The target directory for saving the output of the code generator

    djangoappnames : list
        list of tuples of the form ('appname', 'path/to/input/csv')

    Returns
    -------
    int
        Number of files created by the script

    """

    from os import listdir
    from os.path import isfile, join

    csv_file_names = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]

    if len(djangoappnames) != len(csv_file_names):
        print ('Error: args != number of available csv')
        return

    file_app_names = [os.path.splitext(n)[0] for n in csv_file_names]

    for appname in djangoappnames:
        if appname not in file_app_names:
            print ('Error: corresponding csv for {arg} not available')
            return

    sorted_csv_names = []

    for appname in djangoappnames:
        sorted_csv_names.append(os.path.join(os.path.dirname(__file__), 'data', appname + '.csv'))

    list_of_tuples = [(a,b) for a,b in zip(djangoappnames, sorted_csv_names)]

    try:
        generate_code(output_dir, *list_of_tuples)
    except Exception as e:
        print (e)
    else:
        created = len(listdir(output_dir))
        print ("{} files were created in {}".format(created,output_dir))
        return created

if __name__ == '__main__':
    import os
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    output_dir = os.path.join(os.path.dirname(__file__), 'deleteme')

    main(output_dir, ['jobsdatastore', 'jobsdatabucket'])

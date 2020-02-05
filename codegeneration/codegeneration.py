"""Codegeneration

The entry point for my personal code generator.

Usage
-----
    You should be able to call this program from the command-line.

    The exact I/O requirements are TBD:
        $ python3 -m codegeneration output_dirrectory app1 [app2 app3 ...]

Author
-----
    emilledigital@gmail.com

"""

from codegeneration.functions import *

def main(output_dir, *djangoappnames):
    """CSV files have to be read by order of parentage between
    Django models.

    TODO:
        1. Read the directory
        2. Obtain the filenames and compare them to the arguments
        3. Create an ordered list of tuples of the form ('appname', 'abspath')
    """
    from os import listdir
    from os.path import isfile, join

    csv_file_names = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]
    app_names = [os.path.splitext(n)[0] for n in csv_file_names]
    list_of_tuples = [(a, join(data_dir, n)) for a,n in zip(app_names, csv_file_names)]

    print (listdir(data_dir))
    print (csv_file_names)
    print (app_names)
    #print (list_of_tuples)

    #generate_code(*list_of_tuples)


if __name__ == '__main__':
    import os
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    #print (data_dir)
    #print (output_dir)

    main(data_dir, output_dir)

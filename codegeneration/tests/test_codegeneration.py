"""Test Gen Models OOP

Usage
    $ python3 -m unittest codegeneration.tests.test_gen_models_oop
"""
import unittest
import csv
from codegeneration.codegeneration import *
from codegeneration.functions import *

class TestCodegeneration(unittest.TestCase):
    def test_file_path_methods(self):
        import os
        fil = __file__
        dir = os.path.dirname(fil)
        joi = os.path.join(dir, fil)
        abs = os.path.abspath(joi)

        #print ('dir:',dir)
        #print ('fil:',fil)
        #print ('joi:',joi)
        #print ('abs:',abs)

    def test_create_model_add_fields_from_csv(self):
        import os
        data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'data'))

        src1 = '{}/jobsdatastore.csv'.format(data_dir)
        src2 = '{}/jobsdatabucket.csv'.format(data_dir)

        jobsdatastore = ('jobsdatastore', src1)
        jobsdatabucket = ('jobsdatabucket', src2)

        generate_code(*[jobsdatastore, jobsdatabucket])

        self.assertEqual(len(django_model_objects.keys()),10,"Test data contains 10 models across two Django apps")

    """
    def test_model_foreignkeys(self):
        import os
        data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'data'))

        src1 = '{}/jobsdatastore.csv'.format(data_dir)
        src2 = '{}/jobsdatabucket.csv'.format(data_dir)

        generate_code(('jobsdatastore', src1),('jobsdatabucket', src2))
    """


if __name__ == '__main__':
    unittest.main()

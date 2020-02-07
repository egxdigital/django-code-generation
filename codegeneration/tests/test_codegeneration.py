"""Test Gen Models OOP

Usage
    $ python3 -m unittest codegeneration.tests.test_gen_models_oop
"""
import unittest
import csv
import os
from codegeneration.codegeneration import *
from codegeneration.functions import *

class TestCodegeneration(unittest.TestCase):
    def test_create_model_add_fields_from_csv(self):
        test_data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'data'))
        test_output_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'output'))

        src1 = '{}/jobsdatastore.csv'.format(test_data_dir)
        src2 = '{}/jobsdatabucket.csv'.format(test_data_dir)

        jobsdatastore = ('jobsdatastore', src1)
        jobsdatabucket = ('jobsdatabucket', src2)

        generate_code(test_output_dir, *[jobsdatastore, jobsdatabucket])

        self.assertEqual(len(django_model_objects.keys()),10,"Test data contains 10 models across two Django apps")
        self.assertEqual(len(os.listdir(test_output_dir)),4,"Two files should be generated for each of the two test app csv's")


    def test_model_isForeignkey(self):
        test_data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'data'))
        test_output_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'output'))

        src1 = '{}/jobsdatastore.csv'.format(test_data_dir)
        src2 = '{}/jobsdatabucket.csv'.format(test_data_dir)

        jobsdatastore = ('jobsdatastore', src1)
        jobsdatabucket = ('jobsdatabucket', src2)

        generate_code(test_output_dir, *[jobsdatastore, jobsdatabucket])

        self.assertEqual(
            [(_.modelname, _.isForeignkey) for _ in django_model_objects.values()],
            [('JobBoard', True),
             ('Scrape', True),
             ('JobTitle', True),
             ('JobDescription', True),
             ('Company', True),
             ('ListingTag', True),
             ('Technology', True),
             ('JobPost', True),
             ('JobPostListingTag', False),
             ('JobPostTechnology', False)
             ],
             "8/10 models are a foreign key in another model"
        )

    def test_model_isForeignkeyIn(self):
        test_data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'data'))
        test_output_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'output'))

        src1 = '{}/jobsdatastore.csv'.format(test_data_dir)
        src2 = '{}/jobsdatabucket.csv'.format(test_data_dir)

        jobsdatastore = ('jobsdatastore', src1)
        jobsdatabucket = ('jobsdatabucket', src2)

        generate_code(test_output_dir, *[jobsdatastore, jobsdatabucket])

        self.Diff = None
        self.assertEqual(
            [(_.modelname,_.isForeignkeyIn) for _ in django_model_objects.values()],
            [('JobBoard', ['Scrape', 'ListingTag']),
             ('Scrape', ['JobPost']),
             ('JobTitle', ['JobPost']),
             ('JobDescription', ['JobPost']),
             ('Company', ['JobPost']),
             ('ListingTag', ['JobPostListingTag']),
             ('Technology', ['JobPostTechnology']),
             ('JobPost', ['JobPostListingTag', 'JobPostTechnology']),
             ('JobPostListingTag', []),
             ('JobPostTechnology', [])
             ],
            "8/10 models are foreign keys in other models"
        )

        #from pprint import pprint
        #pprint ([(_.modelname,_.isForeignkeyIn) for _ in django_model_objects.values()])


    def test_model_foreignkey_parents(self):
        test_data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'data'))
        test_output_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'output'))

        src1 = '{}/jobsdatastore.csv'.format(test_data_dir)
        src2 = '{}/jobsdatabucket.csv'.format(test_data_dir)

        jobsdatastore = ('jobsdatastore', src1)
        jobsdatabucket = ('jobsdatabucket', src2)

        generate_code(test_output_dir, *[jobsdatastore, jobsdatabucket])

        self.Diff = None
        self.assertEqual(
            [(_.modelname,_.foreignkey_parent) for _ in django_model_objects.values()],
            [
             ('JobBoard', {}),
             ('Scrape',
                {'job_board': 'jobsdatastore'}
             ),
             ('JobTitle', {}),
             ('JobDescription', {}),
             ('Company', {}),
             ('ListingTag',
                {'job_board': 'jobsdatastore'}
             ),
             ('Technology', {}),
             ('JobPost',
                {
                'company': 'jobsdatastore',
                'job_description': 'jobsdatastore',
                'job_title': 'jobsdatastore',
                'scrape': 'jobsdatastore'
                }
            ),
            ('JobPostListingTag',
                {
                'job_post': 'jobsdatabucket',
                'listing_tag': 'jobsdatastore'
                }
            ),
            ('JobPostTechnology',
                {
                'job_post': 'jobsdatabucket',
                'technology': 'jobsdatastore'}
            )
            ],
            "5/10 models have foreign keys.All the jobsdatabucket apps have foreign keys in jobsdatastore"
        )


if __name__ == '__main__':
    unittest.main()

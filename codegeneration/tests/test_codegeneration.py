"""Test Codegeneration

Usage
    $ python3 -m unittest codegeneration.tests.test_gen_models_oop
"""
import pprint
import unittest
import csv
import os
from os import listdir
from os.path import isfile, join
from codegeneration.codegeneration import *
from codegeneration.functions import *

class TestCodeGeneration(unittest.TestCase):

    def _prepare_output_directory(self):
        """Deletes any existing files in test output"""
        dir = self.test_output_dir
        filepaths = [os.path.join(dir,f) for f in listdir(dir) if isfile(join(dir, f))]

        if len(filepaths) == 0:
            return

        for file in filepaths:
            try:
                os.unlink(file)
            except Exception as e:
                print ("tearDown: {} on\n {}".format(e, file))


    def setUp(self):
        self.Diff = None
        self.current_directory = os.path.dirname( __file__ )
        self.test_data_dir = os.path.abspath(os.path.join(self.current_directory, 'data'))
        self.test_output_dir = os.path.abspath(os.path.join(self.current_directory, 'output'))

        self.src1 = '{}/scraper.csv'.format(self.test_data_dir)
        self.src2 = '{}/jobsdatastore.csv'.format(self.test_data_dir)
        self.src3 = '{}/jobsdatabucket.csv'.format(self.test_data_dir)

        self.scraper = ('scraper', self.src1)
        self.jobsdatastore = ('jobsdatastore', self.src2)
        self.jobsdatabucket = ('jobsdatabucket', self.src3)

        self._prepare_outpudef _prepare_output_directory(self):
        """Deletes any existing files in test output"""
        dir = self.test_output_dir
        filepatt_directory()
        generate_code(self.test_output_dir, *[self.scraper, self.jobsdatastore, self.jobsdatabucket])


    def tearDown(self):
        self._prepare_output_directory()


    def test_create_models_add_fields_from_csv(self):
        """Tests for the corrrect number of models and files generated"""

        self.assertEqual(len(django_model_objects.keys()),13,"Test data contains 13 models across three Django apps")
        self.assertEqual(len(os.listdir(self.test_output_dir)),6,"Six files should be generated for the three test app csv's")


    def test_models_isForeignkey(self):
        """Tests for the correct value of the model's isForeignkey attribute."""

        self.Diff = None
        self.assertEqual(
            [(_.modelname, _.isForeignkey) for _ in django_model_objects.values()],
            [('JobBoard', True),
             ('ListingTag', True),
             ('Scrape', True),
             ('ScrapeJobBoard', False),
             ('JobBoardListingTag', False),
             ('Company', True),
             ('Technology', True),
             ('CompanyTechnology', False),
             ('JobPost', True),
             ('JobPostCompany', False),
             ('JobPostListingTag', False),
             ('JobPostScrape', False),
             ('JobPostTechnology', False)
             ],
             "6 of 13 models are a foreign key in another model across the three apps"
        )


    def test_model_isForeignkeyIn(self):
        """Tests for the correct value of the isForeignkeyIn attribute."""

        self.Diff = None
        self.assertEqual(
            [(_.modelname,_.isForeignkeyIn) for _ in django_model_objects.values()],
            [('JobBoard', ['ScrapeJobBoard', 'JobBoardListingTag']),
             ('ListingTag', ['JobBoardListingTag', 'JobPostListingTag']),
             ('Scrape', ['ScrapeJobBoard', 'JobPostScrape']),
             ('ScrapeJobBoard', []),
             ('JobBoardListingTag', []),
             ('Company', ['CompanyTechnology', 'JobPostCompany']),
             ('Technology', ['CompanyTechnology', 'JobPostTechnology']),
             ('CompanyTechnology', []),
             ('JobPost',
              ['JobPostCompany',
               'JobPostListingTag',
               'JobPostScrape',
               'JobPostTechnology']),
             ('JobPostCompany', []),
             ('JobPostListingTag', []),
             ('JobPostScrape', []),
             ('JobPostTechnology', [])
             ],
            "5/13 models are foreign keys in other models"
        )


    def test_models_foreignkeys_parents(self):
        """Tests whether foreign keys are imported from the correct app"""

        self.Diff = None
        self.assertEqual(
            [(_.modelname,_.foreignkey_parent) for _ in django_model_objects.values()],
            [('JobBoard', {}),
             ('ListingTag', {}),
             ('Scrape', {}),
             ('ScrapeJobBoard', {'job_board': 'scraper', 'scrape': 'scraper'}),
             ('JobBoardListingTag', {'job_board': 'scraper', 'listing_tag': 'scraper'}),
             ('Company', {}),
             ('Technology', {}),
             ('CompanyTechnology',{'company': 'jobsdatastore', 'technology': 'jobsdatastore'}),
             ('JobPost', {}),
             ('JobPostCompany', {'company': 'jobsdatastore', 'job_post': 'jobsdatabucket'}),
             ('JobPostListingTag', {'job_post': 'jobsdatabucket', 'listing_tag': 'scraper'}),
             ('JobPostScrape', {'job_post': 'jobsdatabucket', 'scrape': 'scraper'}),
             ('JobPostTechnology', {'job_post': 'jobsdatabucket', 'technology': 'jobsdatastore'})
             ],
             "7 of 13 models have foreign keys. 3 have foreign keys in scraper; 3 have foreign keys in jobsdatastore and 3 have foreign keys in jobsdatabucket"
            )


if __name__ == '__main__':
    unittest.main()

"""Test Functions

Usage
    $ python3 -m unittest codegeneration.tests.test_functions
"""
import os
from os import listdir
from os.path import isfile, join
import sys
import csv
import unittest
from codegeneration.models import *
from codegeneration.fragments import *
from codegeneration.helpers import *
from codegeneration.functions import *

class TestGenerateUrls(unittest.TestCase):

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
        tech_fields = {'technology_name': 'CharField'}
        company_fields = {'company_name': 'CharField'}
        model_fields = {'date':'DateField','duration':'DurationField','entries_made':'IntegerField','success':'BooleanField'}

        self.valid_string = (
            ""
        )

        self.valid_apps_models = {
            'scraper': ['Scrape'],
            'jobsdatastore': ['Technology', 'Company']
        }

        self.current_directory = os.path.dirname( __file__ )
        self.test_data_dir = os.path.abspath(os.path.join(self.current_directory, 'data'))
        self.test_output_dir = os.path.abspath(os.path.join(self.current_directory, 'output'))

        self.models = {}
        self.m = DjangoModel('Scrape', 'scraper', **model_fields)
        self.v = DjangoModel('Technology', 'jobsdatastore', **tech_fields)
        self.h = DjangoModel('Company', 'jobsdatastore', **company_fields)

        self.models[self.m.modelname] = self.m
        self.models[self.v.modelname] = self.v
        self.models[self.h.modelname] = self.h

    def test_apps_models(self):
        self._prepare_output_directory()
        generate_urls_py_files(self.models, self.test_output_dir, urls_skeleton, urls_url_pattern)
        self.assertEqual(apps_models, self.valid_apps_models)

    def test_generate_api(self):
        self._prepare_output_directory()
        generate_api(self.valid_apps_models, self.test_output_dir)


if __name__ == '__main__':
    unittest.main()

"""Test Functions

Usage
    $ python3 -m unittest codegeneration.tests.test_functions
"""
import os, sys
from os import listdir
from os.path import isfile, join
import csv, json, pprint
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
        self.current_directory = os.path.dirname( __file__ )
        self.test_data_dir = os.path.abspath(os.path.join(self.current_directory, 'data'))
        self.test_output_dir = os.path.abspath(os.path.join(self.current_directory, 'output'))

        tech_fields = {'technology_name': 'CharField'}
        company_fields = {'company_name': 'CharField'}
        jobboard_fields = {'jobboard_name':'CharField', 'home_page':'URLField', 'search_page':'URLField'}
        scrape_fields = {'date':'DateField','duration':'DurationField','entries_made':'IntegerField','success':'BooleanField'}
        scrapejobboard_fields = {'scrape':'ForeignKey', 'job_board':'ForeignKey'}

        self.valid_apps_models = {
            'scraper': ['Scrape'],
            'jobsdatastore': ['Technology', 'Company']
        }

        self.models = {}
        self.m = DjangoModel('Scrape', 'scraper', **scrape_fields)
        self.v = DjangoModel('Technology', 'jobsdatastore', **tech_fields)
        self.h = DjangoModel('Company', 'jobsdatastore', **company_fields)

        self.models[self.m.modelname] = self.m
        self.models[self.v.modelname] = self.v
        self.models[self.h.modelname] = self.h

        self.src1 = '{}/scraper.csv'.format(self.test_data_dir)
        self.src2 = '{}/jobsdatastore.csv'.format(self.test_data_dir)
        self.src3 = '{}/jobsdatabucket.csv'.format(self.test_data_dir)

        self.scraper = ('scraper', self.src1)
        self.jobsdatastore = ('jobsdatastore', self.src2)
        self.jobsdatabucket = ('jobsdatabucket', self.src3)

    def test_viewset_builder(self):
        for app in apps_Models.keys():
            #print (app)
            listOfModels = apps_Models[app]
            viewSets = []
            for model in listOfModels:
                #print ('\t', model)
                viewSets += ["{}ViewSet".format(model)]

            apps_ViewSets[app] = ", ".join(viewSets)

    def test_print_dict(self):
        self._prepare_output_directory()
        dir = self.test_output_dir
        generate_code(dir, *[self.scraper, self.jobsdatastore, self.jobsdatabucket])
        generate_models_files(self.test_output_dir, apps_Models, django_model_objects)
        generate_test_models_files(self.test_output_dir, apps_Models, django_model_objects)

    def test_build_dict_app_externmodels(self):
        self._prepare_output_directory()
        dir = self.test_output_dir
        generate_code(dir, *[self.scraper, self.jobsdatastore, self.jobsdatabucket])
        build_dict_apps_Externmodels(django_model_objects, apps_Models)
        pprint.pprint(apps_Externmodels)
        print (list(apps_Externmodels.keys()))

if __name__ == '__main__':
    unittest.main()

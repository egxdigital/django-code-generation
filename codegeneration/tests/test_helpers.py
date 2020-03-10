"""Test Helpers

Usage
    $ python3 -m unittest codegeneration.tests.test_helpers
"""
import os
import sys
import csv
import unittest
from codegeneration.models import *
from codegeneration.fragments import *
from codegeneration.helpers import *
from codegeneration.functions import *

class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.models = {
        'JobBoard':'jobboard_name',
        'Scrape':'scrape_name',
        'ListingTag':'listingtag_name'
        }

        self.current_directory = os.path.dirname( __file__ )
        self.test_output_dir = os.path.abspath(os.path.join(self.current_directory, 'output'))

        self.valid_filepath = "/home/engineer/source/python/projects/django_code_generation/codegeneration/tests/output/jobsdatastore_models.py"

    def test_trim_dosctring(self):
        pass

    def test_pluralize(self):
        s = helper_pluralize('jobboard')
        t = helper_pluralize('technology')

        self.assertEqual(s, 'jobboards')
        self.assertEqual(t, 'technologies')

    def test_helper_return_filepath(self):
        f = helper_return_filepath('models', 'jobsdatastore', self.test_output_dir)
        self.assertEqual(f, self.valid_filepath)

    def helper_write_contents_to_file(self):
        print (self.test_output_dir)
        print (self.current_directory)

        filepath = helper_return_filepath('models', 'app', self.test_output_dir)

        helper_append_contents_to_file(
            "Contents",
            filepath
        )

if __name__ == '__main__':
    unittest.main()

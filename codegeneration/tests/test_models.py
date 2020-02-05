"""Test Gen Models OOP

Usage
    $ python3 -m unittest codegeneration.tests.test_gen_models_oop
"""
import unittest
import csv
from codegeneration.models import *

class TestCodegeneration(unittest.TestCase):
    def setUp(self):
        global model_fields
        global foreignkey_fields

        model_fields = {
            'date':'DateField',
            'duration':'DurationField',
            'entries_made':'IntegerField',
            'success':'BooleanField'
        }

        foreignkey_fields = {
            'fkeyfieldname':'jobboard',
            'name':'CharField',
            'home_page_link':'URLField',
            'search_page_link':'URLField'
        }


    def test_create_model_with_dict_of_fields(self):
        m = DjangoModel(modelname='Scrape', djangoapp='jobsdatastore', **model_fields)

        self.assertEqual(m.modelname,'Scrape', 'Incorrect model name')
        self.assertEqual(m.djangoapp,'jobsdatastore', 'Incorrect django app')
        self.assertFalse(m.isForeignkey, 'Model is not a foreign key in any other model')
        self.assertEqual(m.fkeyfieldname, None, 'Model is not a foreign key, should not have a foreign key fieldname')
        self.assertEqual(len(m.foreignkey_names.values()),0,'Model does not have any foreign keys at the moment')


    def test_create_model_field(self):
        f = ModelField(fieldname='Date',djangofield='DateField')
        self.assertTrue(hasattr(f,'fieldname'), 'Field should have a fieldname attribute')
        self.assertTrue(hasattr(f, 'djangofield'), 'Field should have a djangofield attribute')
        self.assertEqual(f.fieldname, 'Date', 'Incorrect fieldname')
        self.assertEqual(f.djangofield, 'DateField', 'Incorrect djangofield')



if __name__ == '__main__':
    unittest.main()

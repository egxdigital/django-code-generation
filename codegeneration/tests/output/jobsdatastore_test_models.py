"""Test Models - jobsdatastore

This module contains the tests for the jobsdatastore models.

Example
    python manage.py test --pattern="test_*" jobsdatastore.tests.test_models
"""
import uuid
import pytz
import datetime
from django.db import models
from django.test import TestCase
from model_mommy import mommy
from jobsdatastore.models import Company, Technology, CompanyTechnology


class CompanyTestCase(TestCase):
    def setUp (self):
        self.data = {
            "company_name":"CharField",
            "hiring_from":"CharField",
        }

        self.instance = mommy.make(
           Company,
           company_name = self.data['company_name'],
           hiring_from = self.data['hiring_from'],
        )

    def test_is_instance(self):
        thing = Company()
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_company_id(self):
        record = Company.objects.get(company_id=self.instance.pk)
        self.assertEqual(record.company_id, self.instance.company_id)

    def test_fields_company_company_name(self):
        record = Company.objects.get(company_id=self.instance.pk)
        self.assertEqual(record.company_name, self.instance.company_name)

    def test_fields_company_hiring_from(self):
        record = Company.objects.get(company_id=self.instance.pk)
        self.assertEqual(record.hiring_from, self.instance.hiring_from)


class TechnologyTestCase(TestCase):
    def setUp (self):
        self.data = {
            "technology_name":"CharField",
        }

        self.instance = mommy.make(
           Technology,
           technology_name = self.data['technology_name'],
        )

    def test_is_instance(self):
        thing = Technology()
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_technology_id(self):
        record = Technology.objects.get(technology_id=self.instance.pk)
        self.assertEqual(record.technology_id, self.instance.technology_id)

    def test_fields_technology_technology_name(self):
        record = Technology.objects.get(technology_id=self.instance.pk)
        self.assertEqual(record.technology_name, self.instance.technology_name)


class CompanyTechnologyTestCase(TestCase):
    def setUp (self):
        self.data = {
            "company":{                
                "company_name":"CharField",
                "hiring_from":"CharField",
            },
            "technology":{                
                "technology_name":"CharField",
            },
        }

        self.company = Company()
        self.company.company_name = self.data['company']['company_name']
        self.company.hiring_from = self.data['company']['hiring_from']

        self.company.save()

        self.technology = Technology()
        self.technology.technology_name = self.data['technology']['technology_name']

        self.technology.save()


    def test_is_instance(self):
        thing = CompanyTechnology()
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_company(self):
        <placeholder> = Company.objects.get(company_id=self.company.pk)
        <placeholder> = Technology.objects.get(technology_id=self.technology.pk)

        companytechnology = CompanyTechnology()
        companytechnology.company = self.company
        companytechnology.technology = self.technology
        companytechnology.save()

        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, self.company)

    def test_fields_technology(self):
        <placeholder> = Company.objects.get(company_id=self.company.pk)
        <placeholder> = Technology.objects.get(technology_id=self.technology.pk)

        companytechnology = CompanyTechnology()
        companytechnology.company = self.company
        companytechnology.technology = self.technology
        companytechnology.save()

        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, self.technology)


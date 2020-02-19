from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology


class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)


"""Test API
This module cointains the test cases for the API views of the jobsdatastore
Django application.

Examples
    python manage.py test --pattern="test_*" jobsdatastore.tests

"""
import pprint, time, pytz, json, datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient, APIClient
from jobsdatastore.models import Company, Technology, CompanyTechnology
from jobsdatastore.api.serializers import CompanySerializer, TechnologySerializer, CompanyTechnologySerializer
from jobsdatastore.api.views import CompanyViewSet, TechnologyViewSet, CompanyTechnologyViewSet

client = RequestsClient()

class TestCompanyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CompanyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/companies/')

        self.valid_company = {
            "company_name":"CharField",
            "hiring_from":"CharField",
        }

    def test_create_company(self):
        response = self.client.post(self.url, self.valid_company, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)


    def test_update_company(self):
        post = self.client.post(self.url, self.valid_company, format='json')
        self.assertEqual(Company.objects.get().<field>.<attr>, "<before_value>")

        company_pk = str(Company.objects.get().company_id)

        data = {
            "company_name":"CharField",
            "hiring_from":"CharField",
        }

        request = self.factory.put('api/companies/', data, format='json')
        response = self.view(request, pk=company_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().<field>.<attr>, "<after value>")


class TestTechnologyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TechnologyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/technologies/')

        self.valid_technology = {
            "technology_name":"CharField",
        }

    def test_create_technology(self):
        response = self.client.post(self.url, self.valid_technology, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Technology.objects.count(), 1)


    def test_update_technology(self):
        post = self.client.post(self.url, self.valid_technology, format='json')
        self.assertEqual(Technology.objects.get().<field>.<attr>, "<before_value>")

        technology_pk = str(Technology.objects.get().technology_id)

        data = {
            "technology_name":"CharField",
        }

        request = self.factory.put('api/technologies/', data, format='json')
        response = self.view(request, pk=technology_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Technology.objects.count(), 1)
        self.assertEqual(Technology.objects.get().<field>.<attr>, "<after value>")


class TestCompanyTechnologyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CompanyTechnologyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/companytechnologies/')
        self.company_endpoint = ('http://127.0.0.1:8000/api/companies/')
        self.technology_endpoint = ('http://127.0.0.1:8000/api/technologies/')

        self.valid_companytechnology = {
            "company":{                
                "company_name":"CharField",
                "hiring_from":"CharField",
               },
            "technology":{                
                "technology_name":"CharField",
               },
        }

    def test_create_companytechnology(self):
        response = self.client.post(self.url, self.valid_companytechnology, format='json')
        company = str(CompanyTechnology.objects.get().company)
        technology = str(CompanyTechnology.objects.get().technology)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CompanyTechnology.objects.count(), 1)
        self.assertEqual(company, '<model __str__ value>')
        self.assertEqual(technology, '<model __str__ value>')


    def test_update_companytechnology(self):
        post = self.client.post(self.url, self.valid_companytechnology, format='json')
        self.assertEqual(CompanyTechnology.objects.get().<field>.<attr>, "<before_value>")

        companytechnology_pk = str(CompanyTechnology.objects.get().companytechnology_id)
        company_pk = str(Company.objects.get().company_id)
        technology_pk = str(Technology.objects.get().technology_id)

        data = {
            "companytechnology_id":companytechnology_pk,
            "company":{                
                "company_name":"CharField",
                "hiring_from":"CharField",
               },
            "technology":{                
                "technology_name":"CharField",
               },
        }

        request = self.factory.put('api/companytechnologies/', data, format='json')
        response = self.view(request, pk=companytechnology_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Technology.objects.count(), 1)
        self.assertEqual(CompanyTechnology.objects.count(), 1)
        self.assertEqual(CompanyTechnology.objects.get().<field>.<attr>, "<after value>")



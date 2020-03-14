"""Test API - jobsdatastore

This module cointains the test cases for the API views of the jobsdatastore
Django application.

Examples
    python manage.py test --pattern="test_*" jobsdatastore.tests
"""
import pprint, time, pytz, json, datetime
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient, APIClient
from rest_framework.test import force_authenticate
from jobsdatastore.models import Company, Technology, CompanyTechnology
from jobsdatastore.api.serializers import CompanySerializer, TechnologySerializer, CompanyTechnologySerializer
from jobsdatastore.api.views import CompanyViewSet, TechnologyViewSet, CompanyTechnologyViewSet

client = RequestsClient()

class TestCompanyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CompanyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/companies/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)


        self.valid_company = {
            "company_name":"CharField",
            "hiring_from":"CharField",
        }

    def test_create_company(self):
        response = self.client.post(self.url, self.valid_company, format='json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

    def test_get_single_company(self):
        post_response = self.client.post(self.url, self.valid_company, format='json', HTTP_AUTHORIZATION=self.token)

        valid_value = self.valid_company['<attr>']
        instance = Company.objects.get(<field>=valid_value)

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, <field>=instance.<field>)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_company(self):
        post = self.client.post(self.url, self.valid_company, format='json', HTTP_AUTHORIZATION=self.token)
        before_valid_value = self.valid_company['<attr>']
        self.assertEqual(Company.objects.get().<attr>, before_valid_value)

        company_pk = str(Company.objects.get().company_id)

        data = {
            "company_name":"CharField",
            "hiring_from":"CharField",
        }

        request = self.factory.put('api/companies/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=company_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().<attr>, data['<attr_after>'])

    def test_delete_company(self):
        post = self.client.post(self.url, self.valid_company, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(Company.objects.count(), 1)

        valid_value = self.valid_company['<attr>']
        instance = Company.objects.get(<attr>=valid_value)

        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={'<field>':valid_value}, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.count(), 0)


class TestTechnologyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TechnologyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/technologies/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)


        self.valid_technology = {
            "technology_name":"CharField",
        }

    def test_create_technology(self):
        response = self.client.post(self.url, self.valid_technology, format='json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Technology.objects.count(), 1)

    def test_get_single_technology(self):
        post_response = self.client.post(self.url, self.valid_technology, format='json', HTTP_AUTHORIZATION=self.token)

        valid_value = self.valid_technology['<attr>']
        instance = Technology.objects.get(<field>=valid_value)

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, <field>=instance.<field>)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_technology(self):
        post = self.client.post(self.url, self.valid_technology, format='json', HTTP_AUTHORIZATION=self.token)
        before_valid_value = self.valid_technology['<attr>']
        self.assertEqual(Technology.objects.get().<attr>, before_valid_value)

        technology_pk = str(Technology.objects.get().technology_id)

        data = {
            "technology_name":"CharField",
        }

        request = self.factory.put('api/technologies/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=technology_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Technology.objects.count(), 1)
        self.assertEqual(Technology.objects.get().<attr>, data['<attr_after>'])

    def test_delete_technology(self):
        post = self.client.post(self.url, self.valid_technology, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(Technology.objects.count(), 1)

        valid_value = self.valid_technology['<attr>']
        instance = Technology.objects.get(<attr>=valid_value)

        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={'<field>':valid_value}, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Technology.objects.count(), 0)


class TestCompanyTechnologyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CompanyTechnologyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/companytechnologies/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

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
        response = self.client.post(self.url, self.valid_companytechnology, format='json', HTTP_AUTHORIZATION=self.token)
        company = str(CompanyTechnology.objects.get().company)
        technology = str(CompanyTechnology.objects.get().technology)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CompanyTechnology.objects.count(), 1)
        self.assertEqual(company, '<model __str__ value>')
        self.assertEqual(technology, '<model __str__ value>')

    def test_get_single_companytechnology(self):
        post_response = self.client.post(self.url, self.valid_companytechnology, format='json', HTTP_AUTHORIZATION=self.token)
        company_pk = str(Company.objects.get().company_id)
        technology_pk = str(Technology.objects.get().technology_id)

        valid_value = company_pk
        instance = CompanyTechnology.objects.get(company=valid_value)

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, company=instance.pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_companytechnology(self):
        post = self.client.post(self.url, self.valid_companytechnology, format='json', HTTP_AUTHORIZATION=self.token)
        before_valid_value = self.valid_companytechnology['<attr>']
        self.assertEqual(CompanyTechnology.objects.get().<attr>, before_valid_value)

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
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=companytechnology_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Technology.objects.count(), 1)
        self.assertEqual(CompanyTechnology.objects.count(), 1)
        self.assertEqual(CompanyTechnology.objects.get().<attr>, data['<attr_after>'])

    def test_delete_companytechnology(self):
        post = self.client.post(self.url, self.valid_companytechnology, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(CompanyTechnology.objects.count(), 1)
        company_pk = str(Company.objects.get().company_id)
        technology_pk = str(Technology.objects.get().technology_id)

        valid_value = company_pk
        instance = CompanyTechnology.objects.get(company=valid_value)

        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={'company':valid_value}, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CompanyTechnology.objects.count(), 0)



"""Test API

This module cointains the test cases for the API views of the jobsdatastore
Django application.

Examples
    python manage.py test --pattern="test_*" jobsdatastore.tests

"""
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient
from jobsdatastore.models import Company, Technology, CompanyTechnology
from jobsdatastore.api.serializers import CompanySerializer, TechnologySerializer, CompanyTechnologySerializer
from jobsdatastore.api.views import CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView, TechnologyListCreateAPIView, TechnologyRetrieveUpdateDestroyAPIView, CompanyTechnologyListCreateAPIView, CompanyTechnologyRetrieveUpdateDestroyAPIView

client = RequestsClient()

class TestCompanyListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('company-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_companies(self):
        """Tests the company-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_company(self):
        """Tests the company-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestCompanyRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = CompanyRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_company(self):
         """Tests the company-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('company-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = Company.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('company-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_company(self):
        """Tests the company-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('company-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = Company.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('company-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_company(self):
        """Tests the company-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('company-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = Company.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('company-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.count(), 0)


class TestTechnologyListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('technology-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_technologies(self):
        """Tests the technology-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(Technology.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_technology(self):
        """Tests the technology-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Technology.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestTechnologyRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = TechnologyRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_technology(self):
         """Tests the technology-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('technology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = Technology.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('technology-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_technology(self):
        """Tests the technology-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('technology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = Technology.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('technology-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_technology(self):
        """Tests the technology-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('technology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = Technology.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('technology-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Technology.objects.count(), 0)


class TestCompanyTechnologyListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('companytechnology-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_companytechnologies(self):
        """Tests the companytechnology-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(CompanyTechnology.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_companytechnology(self):
        """Tests the companytechnology-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CompanyTechnology.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestCompanyTechnologyRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = CompanyTechnologyRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_companytechnology(self):
         """Tests the companytechnology-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('companytechnology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = CompanyTechnology.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('companytechnology-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_companytechnology(self):
        """Tests the companytechnology-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('companytechnology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = CompanyTechnology.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('companytechnology-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_companytechnology(self):
        """Tests the companytechnology-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('companytechnology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = CompanyTechnology.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('companytechnology-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CompanyTechnology.objects.count(), 0)



"""Test API

This module cointains the test cases for the API views of the jobsdatabucket
Django application.

Examples
    python manage.py test --pattern="test_*" jobsdatabucket.tests

"""
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient
from jobsdatabucket.models import JobPost, JobPostCompany, JobPostListingTag, JobPostScrape, JobPostTechnology
from jobsdatabucket.api.serializers import JobPostSerializer, JobPostCompanySerializer, JobPostListingTagSerializer, JobPostScrapeSerializer, JobPostTechnologySerializer
from jobsdatabucket.api.views import JobPostListCreateAPIView, JobPostRetrieveUpdateDestroyAPIView, JobPostCompanyListCreateAPIView, JobPostCompanyRetrieveUpdateDestroyAPIView, JobPostListingTagListCreateAPIView, JobPostListingTagRetrieveUpdateDestroyAPIView, JobPostScrapeListCreateAPIView, JobPostScrapeRetrieveUpdateDestroyAPIView, JobPostTechnologyListCreateAPIView, JobPostTechnologyRetrieveUpdateDestroyAPIView

client = RequestsClient()

class TestJobPostListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('jobpost-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_jobposts(self):
        """Tests the jobpost-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_jobpost(self):
        """Tests the jobpost-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPost.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestJobPostRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = JobPostRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_jobpost(self):
         """Tests the jobpost-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('jobpost-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPost.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('jobpost-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_jobpost(self):
        """Tests the jobpost-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('jobpost-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = JobPost.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('jobpost-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_jobpost(self):
        """Tests the jobpost-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('jobpost-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPost.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('jobpost-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPost.objects.count(), 0)


class TestJobPostCompanyListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('jobpostcompany-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_jobpostcompanies(self):
        """Tests the jobpostcompany-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(JobPostCompany.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_jobpostcompany(self):
        """Tests the jobpostcompany-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPostCompany.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestJobPostCompanyRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = JobPostCompanyRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_jobpostcompany(self):
         """Tests the jobpostcompany-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('jobpostcompany-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPostCompany.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('jobpostcompany-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_jobpostcompany(self):
        """Tests the jobpostcompany-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('jobpostcompany-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = JobPostCompany.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('jobpostcompany-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_jobpostcompany(self):
        """Tests the jobpostcompany-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('jobpostcompany-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPostCompany.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('jobpostcompany-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPostCompany.objects.count(), 0)


class TestJobPostListingTagListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('jobpostlistingtag-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_jobpostlistingtags(self):
        """Tests the jobpostlistingtag-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(JobPostListingTag.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_jobpostlistingtag(self):
        """Tests the jobpostlistingtag-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPostListingTag.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestJobPostListingTagRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = JobPostListingTagRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_jobpostlistingtag(self):
         """Tests the jobpostlistingtag-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('jobpostlistingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPostListingTag.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('jobpostlistingtag-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_jobpostlistingtag(self):
        """Tests the jobpostlistingtag-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('jobpostlistingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = JobPostListingTag.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('jobpostlistingtag-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_jobpostlistingtag(self):
        """Tests the jobpostlistingtag-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('jobpostlistingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPostListingTag.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('jobpostlistingtag-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPostListingTag.objects.count(), 0)


class TestJobPostScrapeListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('jobpostscrape-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_jobpostscrapes(self):
        """Tests the jobpostscrape-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(JobPostScrape.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_jobpostscrape(self):
        """Tests the jobpostscrape-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPostScrape.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestJobPostScrapeRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = JobPostScrapeRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_jobpostscrape(self):
         """Tests the jobpostscrape-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('jobpostscrape-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPostScrape.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('jobpostscrape-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_jobpostscrape(self):
        """Tests the jobpostscrape-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('jobpostscrape-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = JobPostScrape.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('jobpostscrape-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_jobpostscrape(self):
        """Tests the jobpostscrape-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('jobpostscrape-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPostScrape.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('jobpostscrape-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPostScrape.objects.count(), 0)


class TestJobPostTechnologyListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('jobposttechnology-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_jobposttechnologies(self):
        """Tests the jobposttechnology-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(JobPostTechnology.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_jobposttechnology(self):
        """Tests the jobposttechnology-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPostTechnology.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestJobPostTechnologyRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = JobPostTechnologyRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_jobposttechnology(self):
         """Tests the jobposttechnology-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('jobposttechnology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPostTechnology.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('jobposttechnology-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_jobposttechnology(self):
        """Tests the jobposttechnology-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('jobposttechnology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = JobPostTechnology.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('jobposttechnology-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_jobposttechnology(self):
        """Tests the jobposttechnology-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('jobposttechnology-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobPostTechnology.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('jobposttechnology-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPostTechnology.objects.count(), 0)



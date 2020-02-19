"""Test API

This module cointains the test cases for the API views of the scraper
Django application.

Examples
    python manage.py test --pattern="test_*" scraper.tests

"""
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient
from scraper.models import JobBoard, ListingTag, Scrape, ScrapeJobBoard, JobBoardListingTag
from scraper.api.serializers import JobBoardSerializer, ListingTagSerializer, ScrapeSerializer, ScrapeJobBoardSerializer, JobBoardListingTagSerializer
from scraper.api.views import JobBoardListCreateAPIView, JobBoardRetrieveUpdateDestroyAPIView, ListingTagListCreateAPIView, ListingTagRetrieveUpdateDestroyAPIView, ScrapeListCreateAPIView, ScrapeRetrieveUpdateDestroyAPIView, ScrapeJobBoardListCreateAPIView, ScrapeJobBoardRetrieveUpdateDestroyAPIView, JobBoardListingTagListCreateAPIView, JobBoardListingTagRetrieveUpdateDestroyAPIView

client = RequestsClient()

class TestJobBoardListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('jobboard-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_jobboards(self):
        """Tests the jobboard-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(JobBoard.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_jobboard(self):
        """Tests the jobboard-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobBoard.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestJobBoardRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = JobBoardRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_jobboard(self):
         """Tests the jobboard-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('jobboard-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobBoard.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('jobboard-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_jobboard(self):
        """Tests the jobboard-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('jobboard-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = JobBoard.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('jobboard-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_jobboard(self):
        """Tests the jobboard-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('jobboard-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobBoard.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('jobboard-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobBoard.objects.count(), 0)


class TestListingTagListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('listingtag-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_listingtags(self):
        """Tests the listingtag-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(ListingTag.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_listingtag(self):
        """Tests the listingtag-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ListingTag.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestListingTagRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = ListingTagRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_listingtag(self):
         """Tests the listingtag-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('listingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = ListingTag.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('listingtag-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_listingtag(self):
        """Tests the listingtag-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('listingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = ListingTag.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('listingtag-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_listingtag(self):
        """Tests the listingtag-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('listingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = ListingTag.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('listingtag-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ListingTag.objects.count(), 0)


class TestScrapeListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('scrape-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_scrapes(self):
        """Tests the scrape-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(Scrape.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_scrape(self):
        """Tests the scrape-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Scrape.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestScrapeRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = ScrapeRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_scrape(self):
         """Tests the scrape-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('scrape-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = Scrape.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('scrape-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_scrape(self):
        """Tests the scrape-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('scrape-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = Scrape.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('scrape-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_scrape(self):
        """Tests the scrape-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('scrape-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = Scrape.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('scrape-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Scrape.objects.count(), 0)


class TestScrapeJobBoardListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('scrapejobboard-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_scrapejobboards(self):
        """Tests the scrapejobboard-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(ScrapeJobBoard.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_scrapejobboard(self):
        """Tests the scrapejobboard-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ScrapeJobBoard.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestScrapeJobBoardRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = ScrapeJobBoardRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_scrapejobboard(self):
         """Tests the scrapejobboard-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('scrapejobboard-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = ScrapeJobBoard.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('scrapejobboard-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_scrapejobboard(self):
        """Tests the scrapejobboard-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('scrapejobboard-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = ScrapeJobBoard.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('scrapejobboard-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_scrapejobboard(self):
        """Tests the scrapejobboard-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('scrapejobboard-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = ScrapeJobBoard.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('scrapejobboard-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ScrapeJobBoard.objects.count(), 0)


class TestJobBoardListingTagListCreateAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('jobboardlistingtag-list')
        """<ADD DATA INSTANCES HERE>"""

    def test_create_jobboardlistingtags(self):
        """Tests the jobboardlistingtag-list endpoint for the creation of
        a multiple entries using the POST method.
        """
        response = self.client.post(self.url,self.<placeholder>,format='json')

        self.assertEqual(JobBoardListingTag.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_jobboardlistingtag(self):
        """Tests the jobboardlistingtag-list endpoint for the creation of
        a single entry using the POST method.
        """
        response = self.client.post(self.url, self.<placeholder>, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobBoardListingTag.objects.get().PLACEHOLDER, self.<placeholder>['PLACEHOLDER'])


class TestJobBoardListingTagRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
       self.factory = APIRequestFactory()
       self.view = JobBoardListingTagRetrieveUpdateDestroyAPIView.as_view()

    def test_get_single_jobboardlistingtag(self):
         """Tests the jobboardlistingtag-list endpoint for the retrieval of
        a single entry using the GET method.
        """
        post_url = reverse('jobboardlistingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobBoardListingTag.objects.get(PLACEHOLDER='<placeholder>')

        request = self.factory.get('jobboardlistingtag-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_update_jobboardlistingtag(self):
        """Tests the jobboardlistingtag-detail endpoint for the update of
        a single entry using the PUT method.
        """
        post_url = reverse('jobboardlistingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        saved = JobBoardListingTag.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        edited = <placeholder>
        put_url = reverse('jobboardlistingtag-detail', <kwargs=PLACEHOLDER: saved.PLACEHOLDER>)
        response = self.client.put(put_url, edited)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<PLACEHOLDER STR REPRESENTATION OF DICT>')

    def test_delete_jobboardlistingtag(self):
        """Tests the jobboardlistingtag-detail endpoint for the deletion of
        a single entry using the DELETE method.
        """
        post_url = reverse('jobboardlistingtag-list')
        post_request = self.client.post(post_url, self.<placeholder>, format='json')
        a = JobBoardListingTag.objects.get(PLACEHOLDER=self.<placeholder>['PLACEHOLDER'])
        request = self.factory.delete('jobboardlistingtag-detail')
        response = self.view(request, PLACEHOLDER=a.PLACEHOLDER)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobBoardListingTag.objects.count(), 0)



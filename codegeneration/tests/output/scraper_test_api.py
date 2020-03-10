"""Test API
This module cointains the test cases for the API views of the scraper
Django application.

Examples
    python manage.py test --pattern="test_*" scraper.tests

"""
import pprint, time, pytz, json, datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient, APIClient
from scraper.models import JobBoard, ListingTag, Scrape, ScrapeJobBoard, JobBoardListingTag
from scraper.api.serializers import JobBoardSerializer, ListingTagSerializer, ScrapeSerializer, ScrapeJobBoardSerializer, JobBoardListingTagSerializer
from scraper.api.views import JobBoardViewSet, ListingTagViewSet, ScrapeViewSet, ScrapeJobBoardViewSet, JobBoardListingTagViewSet

client = RequestsClient()

class TestJobBoardAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobBoardViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobboards/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)


        self.valid_jobboard = {
            "jobboard_name":"CharField",
            "home_page":"URLField",
            "search_page":"URLField",
        }

    def test_create_jobboard(self):
        response = self.client.post(self.url, self.valid_jobboard, format='json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobBoard.objects.count(), 1)

    def test_get_single_jobboard(self):
        post_response = self.client.post(self.url, self.valid_jobboard, format='json', HTTP_AUTHORIZATION=self.token)

        instance = JobBoard.objects.get(<field>='<value>')

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, <field>=instance.<field>)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_jobboard(self):
        post = self.client.post(self.url, self.valid_jobboard, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(JobBoard.objects.get().<field>.<attr>, "<before_value>")

        jobboard_pk = str(JobBoard.objects.get().jobboard_id)

        data = {
            "jobboard_name":"CharField",
            "home_page":"URLField",
            "search_page":"URLField",
        }

        request = self.factory.put('api/jobboards/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=jobboard_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobBoard.objects.count(), 1)
        self.assertEqual(JobBoard.objects.get().<field>.<attr>, "<after value>")

    def test_delete_jobboard(self):
        post = self.client.post(self.url, self.valid_jobboard, format='json', HTTP_AUTHORIZATION=self.token)

        instance = JobBoard.objects.get(<nestedObject>=<value>)

        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={'<field>':'<value>'}, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobBoard.objects.count(), 0)


class TestListingTagAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ListingTagViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/listingtags/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)


        self.valid_listingtag = {
            "listingtag_name":"CharField",
        }

    def test_create_listingtag(self):
        response = self.client.post(self.url, self.valid_listingtag, format='json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ListingTag.objects.count(), 1)

    def test_get_single_listingtag(self):
        post_response = self.client.post(self.url, self.valid_listingtag, format='json', HTTP_AUTHORIZATION=self.token)

        instance = ListingTag.objects.get(<field>='<value>')

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, <field>=instance.<field>)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_listingtag(self):
        post = self.client.post(self.url, self.valid_listingtag, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(ListingTag.objects.get().<field>.<attr>, "<before_value>")

        listingtag_pk = str(ListingTag.objects.get().listingtag_id)

        data = {
            "listingtag_name":"CharField",
        }

        request = self.factory.put('api/listingtags/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=listingtag_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ListingTag.objects.count(), 1)
        self.assertEqual(ListingTag.objects.get().<field>.<attr>, "<after value>")

    def test_delete_listingtag(self):
        post = self.client.post(self.url, self.valid_listingtag, format='json', HTTP_AUTHORIZATION=self.token)

        instance = ListingTag.objects.get(<nestedObject>=<value>)

        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={'<field>':'<value>'}, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ListingTag.objects.count(), 0)


class TestScrapeAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ScrapeViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/scrapes/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)


        self.valid_scrape = {
            "scrape_date":"DateField",
            "entries_scraped":"IntegerField",
            "scrape_duration":"DurationField",
            "scrape_success":"BooleanField",
        }

    def test_create_scrape(self):
        response = self.client.post(self.url, self.valid_scrape, format='json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Scrape.objects.count(), 1)

    def test_get_single_scrape(self):
        post_response = self.client.post(self.url, self.valid_scrape, format='json', HTTP_AUTHORIZATION=self.token)

        instance = Scrape.objects.get(<field>='<value>')

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, <field>=instance.<field>)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_scrape(self):
        post = self.client.post(self.url, self.valid_scrape, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(Scrape.objects.get().<field>.<attr>, "<before_value>")

        scrape_pk = str(Scrape.objects.get().scrape_id)

        data = {
            "scrape_date":"DateField",
            "entries_scraped":"IntegerField",
            "scrape_duration":"DurationField",
            "scrape_success":"BooleanField",
        }

        request = self.factory.put('api/scrapes/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=scrape_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Scrape.objects.count(), 1)
        self.assertEqual(Scrape.objects.get().<field>.<attr>, "<after value>")

    def test_delete_scrape(self):
        post = self.client.post(self.url, self.valid_scrape, format='json', HTTP_AUTHORIZATION=self.token)

        instance = Scrape.objects.get(<nestedObject>=<value>)

        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={'<field>':'<value>'}, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Scrape.objects.count(), 0)


class TestScrapeJobBoardAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ScrapeJobBoardViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/scrapejobboards/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.scrape_endpoint = ('http://127.0.0.1:8000/api/scrapes/')
        self.jobboard_endpoint = ('http://127.0.0.1:8000/api/jobboards/')

        self.valid_scrapejobboard = {
            "scrape":{                
                "scrape_date":"DateField",
                "entries_scraped":"IntegerField",
                "scrape_duration":"DurationField",
                "scrape_success":"BooleanField",
               },
            "job_board":{                
                "jobboard_name":"CharField",
                "home_page":"URLField",
                "search_page":"URLField",
               },
        }

    def test_create_scrapejobboard(self):
        response = self.client.post(self.url, self.valid_scrapejobboard, format='json', HTTP_AUTHORIZATION=self.token)
        scrape = str(ScrapeJobBoard.objects.get().scrape)
        job_board = str(ScrapeJobBoard.objects.get().job_board)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ScrapeJobBoard.objects.count(), 1)
        self.assertEqual(scrape, '<model __str__ value>')
        self.assertEqual(job_board, '<model __str__ value>')

    def test_get_single_scrapejobboard(self):
        post_response = self.client.post(self.url, self.valid_scrapejobboard, format='json', HTTP_AUTHORIZATION=self.token)
        scrape_pk = str(Scrape.objects.get().scrape_id)
        jobboard_pk = str(JobBoard.objects.get().jobboard_id)

        instance = ScrapeJobBoard.objects.get(<field>='<value>')

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, <field>=instance.<field>)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_scrapejobboard(self):
        post = self.client.post(self.url, self.valid_scrapejobboard, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(ScrapeJobBoard.objects.get().<field>.<attr>, "<before_value>")

        scrapejobboard_pk = str(ScrapeJobBoard.objects.get().scrapejobboard_id)
        scrape_pk = str(Scrape.objects.get().scrape_id)
        jobboard_pk = str(JobBoard.objects.get().jobboard_id)

        data = {
            "scrapejobboard_id":scrapejobboard_pk,
            "scrape":{                
                "scrape_date":"DateField",
                "entries_scraped":"IntegerField",
                "scrape_duration":"DurationField",
                "scrape_success":"BooleanField",
               },
            "job_board":{                
                "jobboard_name":"CharField",
                "home_page":"URLField",
                "search_page":"URLField",
               },
        }

        request = self.factory.put('api/scrapejobboards/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=scrapejobboard_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Scrape.objects.count(), 1)
        self.assertEqual(JobBoard.objects.count(), 1)
        self.assertEqual(ScrapeJobBoard.objects.count(), 1)
        self.assertEqual(ScrapeJobBoard.objects.get().<field>.<attr>, "<after value>")

    def test_delete_scrapejobboard(self):
        post = self.client.post(self.url, self.valid_scrapejobboard, format='json', HTTP_AUTHORIZATION=self.token)
        scrape_pk = str(Scrape.objects.get().scrape_id)
        jobboard_pk = str(JobBoard.objects.get().jobboard_id)

        instance = ScrapeJobBoard.objects.get(<nestedObject>=<value>)

        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={'<field>':'<value>'}, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ScrapeJobBoard.objects.count(), 0)


class TestJobBoardListingTagAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobBoardListingTagViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobboardlistingtags/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.jobboard_endpoint = ('http://127.0.0.1:8000/api/jobboards/')
        self.listingtag_endpoint = ('http://127.0.0.1:8000/api/listingtags/')

        self.valid_jobboardlistingtag = {
            "job_board":{                
                "jobboard_name":"CharField",
                "home_page":"URLField",
                "search_page":"URLField",
               },
            "listing_tag":{                
                "listingtag_name":"CharField",
               },
        }

    def test_create_jobboardlistingtag(self):
        response = self.client.post(self.url, self.valid_jobboardlistingtag, format='json', HTTP_AUTHORIZATION=self.token)
        job_board = str(JobBoardListingTag.objects.get().job_board)
        listing_tag = str(JobBoardListingTag.objects.get().listing_tag)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobBoardListingTag.objects.count(), 1)
        self.assertEqual(job_board, '<model __str__ value>')
        self.assertEqual(listing_tag, '<model __str__ value>')

    def test_get_single_jobboardlistingtag(self):
        post_response = self.client.post(self.url, self.valid_jobboardlistingtag, format='json', HTTP_AUTHORIZATION=self.token)
        jobboard_pk = str(JobBoard.objects.get().jobboard_id)
        listingtag_pk = str(ListingTag.objects.get().listingtag_id)

        instance = JobBoardListingTag.objects.get(<field>='<value>')

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, <field>=instance.<field>)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_jobboardlistingtag(self):
        post = self.client.post(self.url, self.valid_jobboardlistingtag, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(JobBoardListingTag.objects.get().<field>.<attr>, "<before_value>")

        jobboardlistingtag_pk = str(JobBoardListingTag.objects.get().jobboardlistingtag_id)
        jobboard_pk = str(JobBoard.objects.get().jobboard_id)
        listingtag_pk = str(ListingTag.objects.get().listingtag_id)

        data = {
            "jobboardlistingtag_id":jobboardlistingtag_pk,
            "job_board":{                
                "jobboard_name":"CharField",
                "home_page":"URLField",
                "search_page":"URLField",
               },
            "listing_tag":{                
                "listingtag_name":"CharField",
               },
        }

        request = self.factory.put('api/jobboardlistingtags/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=jobboardlistingtag_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobBoard.objects.count(), 1)
        self.assertEqual(ListingTag.objects.count(), 1)
        self.assertEqual(JobBoardListingTag.objects.count(), 1)
        self.assertEqual(JobBoardListingTag.objects.get().<field>.<attr>, "<after value>")

    def test_delete_jobboardlistingtag(self):
        post = self.client.post(self.url, self.valid_jobboardlistingtag, format='json', HTTP_AUTHORIZATION=self.token)
        jobboard_pk = str(JobBoard.objects.get().jobboard_id)
        listingtag_pk = str(ListingTag.objects.get().listingtag_id)

        instance = JobBoardListingTag.objects.get(<nestedObject>=<value>)

        request = self.client.delete(self.url+str(instance.pk)+'/', kwargs={'<field>':'<value>'}, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobBoardListingTag.objects.count(), 0)



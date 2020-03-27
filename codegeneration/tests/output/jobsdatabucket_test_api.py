"""Test API - jobsdatabucket

This module cointains the test cases for the API views of the jobsdatabucket
Django application.

Examples
    python manage.py test --pattern="test_*" jobsdatabucket.tests
"""
import pprint, time, pytz, json, datetime
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient, APIClient
from rest_framework.test import force_authenticate
from jobsdatastore.models import Technology, Company
from scraper.models import Scrape, ListingTag
from jobsdatastore.api.serializers import TechnologySerializer, CompanySerializer
from scraper.api.serializers import ScrapeSerializer, ListingTagSerializer
from jobsdatabucket.models import JobPost, JobPostCompany, JobPostListingTag, JobPostScrape, JobPostTechnology
from jobsdatabucket.api.serializers import JobPostSerializer, JobPostCompanyPostSerializer, JobPostCompanyGetSerializer, JobPostListingTagPostSerializer, JobPostListingTagGetSerializer, JobPostScrapePostSerializer, JobPostScrapeGetSerializer, JobPostTechnologyPostSerializer, JobPostTechnologyGetSerializer
from jobsdatabucket.api.views import JobPostViewSet, JobPostCompanyViewSet, JobPostListingTagViewSet, JobPostScrapeViewSet, JobPostTechnologyViewSet

client = RequestsClient()

class TestJobPostAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobposts/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)


        self.valid_jobpost = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

        post_response = self.client.post(self.url, self.valid_jobpost, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

    def test_create_jobpost(self):
        self.assertEqual(JobPost.objects.count(), 1)

    def test_get_single_jobpost(self):
        instance = JobPost.objects.get()

        request = self.factory.get(self.url+str(instance.pk), HTTP_AUTHORIZATION=self.token)
        force_authenticate(request, user=self.user)
        response = self.view(request, <field>=instance.<field>)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_jobpost(self):
        self.assertEqual(JobPost.objects.get().<attr>, <before_valid_value>)

        jobpost_pk = str(JobPost.objects.get().jobpost_id)

        data = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

        request = self.factory.put('api/jobposts/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=jobpost_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(JobPost.objects.get().<attr>, data['<attr_after>'])

    def test_delete_jobpost(self):
        self.assertEqual(JobPost.objects.count(), 1)
        instance = JobPost.objects.get()

        request = self.client.delete(self.url+str(instance.pk)+'/', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPost.objects.count(), 0)


class TestJobPostCompanyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostCompanyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobpostcompanies/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.jobpost_endpoint = ('http://127.0.0.1:8000/api/jobposts/')
        self.company_endpoint = ('http://127.0.0.1:8000/api/companies/')

        self.valid_jobpost = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

        self.valid_company = {
            "company_name":"CharField",
            "hiring_from":"CharField",
        }

        resp_jobpost = self.client.post(self.jobpost_endpoint, self.valid_jobpost, format='json', HTTP_AUTHORIZATION=self.token)
        resp_company = self.client.post(self.company_endpoint, self.valid_company, format='json', HTTP_AUTHORIZATION=self.token)

        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        company_pk = str(Company.objects.get().company_id)

        data = {
            "job_post":jobpost_pk,
            "company":company_pk,
        }

        post_response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

    def test_create_jobpostcompany(self):
        jobpost = str(JobPostCompany.objects.get().job_post)
        company = str(JobPostCompany.objects.get().company)
        self.assertEqual(JobPostCompany.objects.count(), 1)
        self.assertEqual(jobpost, '<model __str__ value>')
        self.assertEqual(company, '<model __str__ value>')

    def test_get_single_jobpostcompany(self):
        instance = JobPostCompany.objects.get()

        request = self.factory.get(self.url+str(instance.pk))
        force_authenticate(request, user=self.user)
        response = self.view(request, jobpost=instance)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_jobpostcompany(self):
        self.assertEqual(JobPostCompany.objects.get().<attr>, <before_valid_value>)

        jobpostcompany_pk = str(JobPostCompany.objects.get().jobpostcompany_id)
        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        company_pk = str(Company.objects.get().company_id)

        data = {
            "jobpostcompany_id":jobpostcompany_pk,
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "company":{                
                "company_name":"CharField",
                "hiring_from":"CharField",
               },
        }

        request = self.factory.put('api/jobpostcompanies/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=jobpostcompany_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(JobPostCompany.objects.count(), 1)
        self.assertEqual(JobPostCompany.objects.get().<attr>, data['<attr_after>'])

    def test_delete_jobpostcompany(self):
        self.assertEqual(JobPostCompany.objects.count(), 1)
        instance = JobPostCompany.objects.get()

        request = self.client.delete(self.url+str(instance.pk)+'/', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPostCompany.objects.count(), 0)


class TestJobPostListingTagAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostListingTagViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobpostlistingtags/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.jobpost_endpoint = ('http://127.0.0.1:8000/api/jobposts/')
        self.listingtag_endpoint = ('http://127.0.0.1:8000/api/listingtags/')

        self.valid_jobpost = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

        self.valid_listingtag = {
            "listingtag_name":"CharField",
        }

        resp_jobpost = self.client.post(self.jobpost_endpoint, self.valid_jobpost, format='json', HTTP_AUTHORIZATION=self.token)
        resp_listingtag = self.client.post(self.listingtag_endpoint, self.valid_listingtag, format='json', HTTP_AUTHORIZATION=self.token)

        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        listingtag_pk = str(ListingTag.objects.get().listingtag_id)

        data = {
            "job_post":jobpost_pk,
            "listing_tag":listingtag_pk,
        }

        post_response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

    def test_create_jobpostlistingtag(self):
        jobpost = str(JobPostListingTag.objects.get().job_post)
        listingtag = str(JobPostListingTag.objects.get().listing_tag)
        self.assertEqual(JobPostListingTag.objects.count(), 1)
        self.assertEqual(jobpost, '<model __str__ value>')
        self.assertEqual(listingtag, '<model __str__ value>')

    def test_get_single_jobpostlistingtag(self):
        instance = JobPostListingTag.objects.get()

        request = self.factory.get(self.url+str(instance.pk))
        force_authenticate(request, user=self.user)
        response = self.view(request, jobpost=instance)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_jobpostlistingtag(self):
        self.assertEqual(JobPostListingTag.objects.get().<attr>, <before_valid_value>)

        jobpostlistingtag_pk = str(JobPostListingTag.objects.get().jobpostlistingtag_id)
        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        listingtag_pk = str(ListingTag.objects.get().listingtag_id)

        data = {
            "jobpostlistingtag_id":jobpostlistingtag_pk,
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "listing_tag":{                
                "listingtag_name":"CharField",
               },
        }

        request = self.factory.put('api/jobpostlistingtags/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=jobpostlistingtag_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(ListingTag.objects.count(), 1)
        self.assertEqual(JobPostListingTag.objects.count(), 1)
        self.assertEqual(JobPostListingTag.objects.get().<attr>, data['<attr_after>'])

    def test_delete_jobpostlistingtag(self):
        self.assertEqual(JobPostListingTag.objects.count(), 1)
        instance = JobPostListingTag.objects.get()

        request = self.client.delete(self.url+str(instance.pk)+'/', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPostListingTag.objects.count(), 0)


class TestJobPostScrapeAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostScrapeViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobpostscrapes/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.jobpost_endpoint = ('http://127.0.0.1:8000/api/jobposts/')
        self.scrape_endpoint = ('http://127.0.0.1:8000/api/scrapes/')

        self.valid_jobpost = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

        self.valid_scrape = {
            "scrape_datetime":"DateTimeField",
            "entries_scraped":"IntegerField",
            "scrape_duration":"DurationField",
            "scrape_success":"BooleanField",
        }

        resp_jobpost = self.client.post(self.jobpost_endpoint, self.valid_jobpost, format='json', HTTP_AUTHORIZATION=self.token)
        resp_scrape = self.client.post(self.scrape_endpoint, self.valid_scrape, format='json', HTTP_AUTHORIZATION=self.token)

        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        scrape_pk = str(Scrape.objects.get().scrape_id)

        data = {
            "job_post":jobpost_pk,
            "scrape":scrape_pk,
        }

        post_response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

    def test_create_jobpostscrape(self):
        jobpost = str(JobPostScrape.objects.get().job_post)
        scrape = str(JobPostScrape.objects.get().scrape)
        self.assertEqual(JobPostScrape.objects.count(), 1)
        self.assertEqual(jobpost, '<model __str__ value>')
        self.assertEqual(scrape, '<model __str__ value>')

    def test_get_single_jobpostscrape(self):
        instance = JobPostScrape.objects.get()

        request = self.factory.get(self.url+str(instance.pk))
        force_authenticate(request, user=self.user)
        response = self.view(request, jobpost=instance)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_jobpostscrape(self):
        self.assertEqual(JobPostScrape.objects.get().<attr>, <before_valid_value>)

        jobpostscrape_pk = str(JobPostScrape.objects.get().jobpostscrape_id)
        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        scrape_pk = str(Scrape.objects.get().scrape_id)

        data = {
            "jobpostscrape_id":jobpostscrape_pk,
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "scrape":{                
                "scrape_datetime":"DateTimeField",
                "entries_scraped":"IntegerField",
                "scrape_duration":"DurationField",
                "scrape_success":"BooleanField",
               },
        }

        request = self.factory.put('api/jobpostscrapes/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=jobpostscrape_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(Scrape.objects.count(), 1)
        self.assertEqual(JobPostScrape.objects.count(), 1)
        self.assertEqual(JobPostScrape.objects.get().<attr>, data['<attr_after>'])

    def test_delete_jobpostscrape(self):
        self.assertEqual(JobPostScrape.objects.count(), 1)
        instance = JobPostScrape.objects.get()

        request = self.client.delete(self.url+str(instance.pk)+'/', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPostScrape.objects.count(), 0)


class TestJobPostTechnologyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostTechnologyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobposttechnologies/')

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.jobpost_endpoint = ('http://127.0.0.1:8000/api/jobposts/')
        self.technology_endpoint = ('http://127.0.0.1:8000/api/technologies/')

        self.valid_jobpost = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

        self.valid_technology = {
            "technology_name":"CharField",
        }

        resp_jobpost = self.client.post(self.jobpost_endpoint, self.valid_jobpost, format='json', HTTP_AUTHORIZATION=self.token)
        resp_technology = self.client.post(self.technology_endpoint, self.valid_technology, format='json', HTTP_AUTHORIZATION=self.token)

        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        technology_pk = str(Technology.objects.get().technology_id)

        data = {
            "job_post":jobpost_pk,
            "technology":technology_pk,
        }

        post_response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

    def test_create_jobposttechnology(self):
        jobpost = str(JobPostTechnology.objects.get().job_post)
        technology = str(JobPostTechnology.objects.get().technology)
        self.assertEqual(JobPostTechnology.objects.count(), 1)
        self.assertEqual(jobpost, '<model __str__ value>')
        self.assertEqual(technology, '<model __str__ value>')

    def test_get_single_jobposttechnology(self):
        instance = JobPostTechnology.objects.get()

        request = self.factory.get(self.url+str(instance.pk))
        force_authenticate(request, user=self.user)
        response = self.view(request, jobpost=instance)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '<placeholder>'.format(instance.pk))

    def test_update_jobposttechnology(self):
        self.assertEqual(JobPostTechnology.objects.get().<attr>, <before_valid_value>)

        jobposttechnology_pk = str(JobPostTechnology.objects.get().jobposttechnology_id)
        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        technology_pk = str(Technology.objects.get().technology_id)

        data = {
            "jobposttechnology_id":jobposttechnology_pk,
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "technology":{                
                "technology_name":"CharField",
               },
        }

        request = self.factory.put('api/jobposttechnologies/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=jobposttechnology_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(Technology.objects.count(), 1)
        self.assertEqual(JobPostTechnology.objects.count(), 1)
        self.assertEqual(JobPostTechnology.objects.get().<attr>, data['<attr_after>'])

    def test_delete_jobposttechnology(self):
        self.assertEqual(JobPostTechnology.objects.count(), 1)
        instance = JobPostTechnology.objects.get()

        request = self.client.delete(self.url+str(instance.pk)+'/', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPostTechnology.objects.count(), 0)



"""Test Models - jobsdatabucket

This module contains the tests for the jobsdatabucket models.

Example
    python manage.py test --pattern="test_*" jobsdatabucket.tests.test_models
"""
import uuid
import pytz
import datetime
import time
from time import strftime
from django.db import models
from django.test import TestCase
from model_mommy import mommy
from scraper.models import Scrape, ListingTag
from jobsdatastore.models import Technology, Company
from jobsdatabucket.models import JobPost, JobPostCompany, JobPostListingTag, JobPostScrape, JobPostTechnology


class JobPostTestCase(TestCase):
    def setUp (self):
        self.data = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

        self.instance = mommy.make(
           JobPost,
           job_title = self.data['job_title'],
           date_posted = self.data['date_posted'],
           apply_link = self.data['apply_link'],
           job_description = self.data['job_description'],
        )

    def test_is_instance(self):
        thing = JobPost()
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_jobpost_id(self):
        record = JobPost.objects.get(jobpost_id=self.instance.pk)
        self.assertEqual(record.jobpost_id, self.instance.jobpost_id)

    def test_fields_jobpost_job_title(self):
        record = JobPost.objects.get(jobpost_id=self.instance.pk)
        self.assertEqual(record.job_title, self.instance.job_title)

    def test_fields_jobpost_date_posted(self):
        record = JobPost.objects.get(jobpost_id=self.instance.pk)
        self.assertEqual(record.date_posted, self.instance.date_posted)

    def test_fields_jobpost_apply_link(self):
        record = JobPost.objects.get(jobpost_id=self.instance.pk)
        self.assertEqual(record.apply_link, self.instance.apply_link)

    def test_fields_jobpost_job_description(self):
        record = JobPost.objects.get(jobpost_id=self.instance.pk)
        self.assertEqual(record.job_description, self.instance.job_description)


class JobPostCompanyTestCase(TestCase):
    def setUp (self):
        self.data = {
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

        self.jobpost = JobPost()
        self.jobpost.job_title = self.data['job_post']['job_title']
        self.jobpost.date_posted = self.data['job_post']['date_posted']
        self.jobpost.apply_link = self.data['job_post']['apply_link']
        self.jobpost.job_description = self.data['job_post']['job_description']

        self.jobpost.save()

        self.company = Company()
        self.company.company_name = self.data['company']['company_name']
        self.company.hiring_from = self.data['company']['hiring_from']

        self.company.save()


    def test_is_instance(self):
        thing = JobPostCompany()
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_job_post(self):
        <placeholder> = JobPost.objects.get(jobpost_id=self.jobpost.pk)
        <placeholder> = Company.objects.get(company_id=self.company.pk)

        jobpostcompany = JobPostCompany()
        jobpostcompany.job_post = self.jobpost
        jobpostcompany.company = self.company
        jobpostcompany.save()

        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, self.jobpost)

    def test_fields_company(self):
        <placeholder> = JobPost.objects.get(jobpost_id=self.jobpost.pk)
        <placeholder> = Company.objects.get(company_id=self.company.pk)

        jobpostcompany = JobPostCompany()
        jobpostcompany.job_post = self.jobpost
        jobpostcompany.company = self.company
        jobpostcompany.save()

        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, self.company)


class JobPostListingTagTestCase(TestCase):
    def setUp (self):
        self.data = {
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

        self.jobpost = JobPost()
        self.jobpost.job_title = self.data['job_post']['job_title']
        self.jobpost.date_posted = self.data['job_post']['date_posted']
        self.jobpost.apply_link = self.data['job_post']['apply_link']
        self.jobpost.job_description = self.data['job_post']['job_description']

        self.jobpost.save()

        self.listingtag = ListingTag()
        self.listingtag.listingtag_name = self.data['listing_tag']['listingtag_name']

        self.listingtag.save()


    def test_is_instance(self):
        thing = JobPostListingTag()
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_job_post(self):
        <placeholder> = JobPost.objects.get(jobpost_id=self.jobpost.pk)
        <placeholder> = ListingTag.objects.get(listingtag_id=self.listingtag.pk)

        jobpostlistingtag = JobPostListingTag()
        jobpostlistingtag.job_post = self.jobpost
        jobpostlistingtag.listing_tag = self.listingtag
        jobpostlistingtag.save()

        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, self.jobpost)

    def test_fields_listing_tag(self):
        <placeholder> = JobPost.objects.get(jobpost_id=self.jobpost.pk)
        <placeholder> = ListingTag.objects.get(listingtag_id=self.listingtag.pk)

        jobpostlistingtag = JobPostListingTag()
        jobpostlistingtag.job_post = self.jobpost
        jobpostlistingtag.listing_tag = self.listingtag
        jobpostlistingtag.save()

        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, self.listingtag)


class JobPostScrapeTestCase(TestCase):
    def setUp (self):
        self.data = {
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

        self.jobpost = JobPost()
        self.jobpost.job_title = self.data['job_post']['job_title']
        self.jobpost.date_posted = self.data['job_post']['date_posted']
        self.jobpost.apply_link = self.data['job_post']['apply_link']
        self.jobpost.job_description = self.data['job_post']['job_description']

        self.jobpost.save()

        self.scrape = Scrape()
        self.scrape.scrape_datetime = self.data['scrape']['scrape_datetime']
        self.scrape.entries_scraped = self.data['scrape']['entries_scraped']
        self.scrape.scrape_duration = self.data['scrape']['scrape_duration']
        self.scrape.scrape_success = self.data['scrape']['scrape_success']

        self.scrape.save()


    def test_is_instance(self):
        thing = JobPostScrape()
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_job_post(self):
        <placeholder> = JobPost.objects.get(jobpost_id=self.jobpost.pk)
        <placeholder> = Scrape.objects.get(scrape_id=self.scrape.pk)

        jobpostscrape = JobPostScrape()
        jobpostscrape.job_post = self.jobpost
        jobpostscrape.scrape = self.scrape
        jobpostscrape.save()

        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, self.jobpost)

    def test_fields_scrape(self):
        <placeholder> = JobPost.objects.get(jobpost_id=self.jobpost.pk)
        <placeholder> = Scrape.objects.get(scrape_id=self.scrape.pk)

        jobpostscrape = JobPostScrape()
        jobpostscrape.job_post = self.jobpost
        jobpostscrape.scrape = self.scrape
        jobpostscrape.save()

        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, self.scrape)


class JobPostTechnologyTestCase(TestCase):
    def setUp (self):
        self.data = {
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

        self.jobpost = JobPost()
        self.jobpost.job_title = self.data['job_post']['job_title']
        self.jobpost.date_posted = self.data['job_post']['date_posted']
        self.jobpost.apply_link = self.data['job_post']['apply_link']
        self.jobpost.job_description = self.data['job_post']['job_description']

        self.jobpost.save()

        self.technology = Technology()
        self.technology.technology_name = self.data['technology']['technology_name']

        self.technology.save()


    def test_is_instance(self):
        thing = JobPostTechnology()
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_job_post(self):
        <placeholder> = JobPost.objects.get(jobpost_id=self.jobpost.pk)
        <placeholder> = Technology.objects.get(technology_id=self.technology.pk)

        jobposttechnology = JobPostTechnology()
        jobposttechnology.job_post = self.jobpost
        jobposttechnology.technology = self.technology
        jobposttechnology.save()

        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, self.jobpost)

    def test_fields_technology(self):
        <placeholder> = JobPost.objects.get(jobpost_id=self.jobpost.pk)
        <placeholder> = Technology.objects.get(technology_id=self.technology.pk)

        jobposttechnology = JobPostTechnology()
        jobposttechnology.job_post = self.jobpost
        jobposttechnology.technology = self.technology
        jobposttechnology.save()

        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, self.technology)

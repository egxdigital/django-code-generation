"""Test Models - scraper

This module contains the tests for the scraper models.
"""
import uuid
import datetime
from django.db import models
from model_mommy import mommy
from scraper.models import JobBoard, ListingTag, Scrape, ScrapeJobBoard, JobBoardListingTag


class JobBoardTestCase(TestCase):
    def setUp (self):
        self.data = {
            "jobboard_name":"CharField",
            "home_page":"URLField",
            "search_page":"URLField",
        }

        self.instance = mommy.make(
           JobBoard,
           jobboard_id = self.data['jobboard_id']
           jobboard_name = self.data['jobboard_name']
           home_page = self.data['home_page']
           search_page = self.data['search_page']
        )

    def test_is_instance(self):
        self.assertTrue(isinstance(self.instance, JobBoard))

    def test_fields_jobboard_jobboard_id(self):
        record = JobBoard.objects.get(jobboard_id=self.jobboard.pk)
        self.assertEqual(record.jobboard_id, self.instance.jobboard_id)

    def test_fields_jobboard_jobboard_name(self):
        record = JobBoard.objects.get(jobboard_id=self.jobboard.pk)
        self.assertEqual(record.jobboard_name, self.instance.jobboard_name)

    def test_fields_jobboard_home_page(self):
        record = JobBoard.objects.get(jobboard_id=self.jobboard.pk)
        self.assertEqual(record.home_page, self.instance.home_page)

    def test_fields_jobboard_search_page(self):
        record = JobBoard.objects.get(jobboard_id=self.jobboard.pk)
        self.assertEqual(record.search_page, self.instance.search_page)


class ListingTagTestCase(TestCase):
    def setUp (self):
        self.data = {
            "listingtag_name":"CharField",
        }

        self.instance = mommy.make(
           ListingTag,
           listingtag_id = self.data['listingtag_id']
           listingtag_name = self.data['listingtag_name']
        )

    def test_is_instance(self):
        self.assertTrue(isinstance(self.instance, ListingTag))

    def test_fields_listingtag_listingtag_id(self):
        record = ListingTag.objects.get(listingtag_id=self.listingtag.pk)
        self.assertEqual(record.listingtag_id, self.instance.listingtag_id)

    def test_fields_listingtag_listingtag_name(self):
        record = ListingTag.objects.get(listingtag_id=self.listingtag.pk)
        self.assertEqual(record.listingtag_name, self.instance.listingtag_name)


class ScrapeTestCase(TestCase):
    def setUp (self):
        self.data = {
            "scrape_date":"DateField",
            "entries_scraped":"IntegerField",
            "scrape_duration":"DurationField",
            "scrape_success":"BooleanField",
        }

        self.instance = mommy.make(
           Scrape,
           scrape_id = self.data['scrape_id']
           scrape_date = self.data['scrape_date']
           entries_scraped = self.data['entries_scraped']
           scrape_duration = self.data['scrape_duration']
           scrape_success = self.data['scrape_success']
        )

    def test_is_instance(self):
        self.assertTrue(isinstance(self.instance, Scrape))

    def test_fields_scrape_scrape_id(self):
        record = Scrape.objects.get(scrape_id=self.scrape.pk)
        self.assertEqual(record.scrape_id, self.instance.scrape_id)

    def test_fields_scrape_scrape_date(self):
        record = Scrape.objects.get(scrape_id=self.scrape.pk)
        self.assertEqual(record.scrape_date, self.instance.scrape_date)

    def test_fields_scrape_entries_scraped(self):
        record = Scrape.objects.get(scrape_id=self.scrape.pk)
        self.assertEqual(record.entries_scraped, self.instance.entries_scraped)

    def test_fields_scrape_scrape_duration(self):
        record = Scrape.objects.get(scrape_id=self.scrape.pk)
        self.assertEqual(record.scrape_duration, self.instance.scrape_duration)

    def test_fields_scrape_scrape_success(self):
        record = Scrape.objects.get(scrape_id=self.scrape.pk)
        self.assertEqual(record.scrape_success, self.instance.scrape_success)


class ScrapeJobBoardTestCase(TestCase):
    def setUp (self):
        self.data = {
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

        self.scrape = Scrape()
        self.scrape.scrape_date = self.data['scrape']['scrape_date']
        self.scrape.entries_scraped = self.data['scrape']['entries_scraped']
        self.scrape.scrape_duration = self.data['scrape']['scrape_duration']
        self.scrape.scrape_success = self.data['scrape']['scrape_success']

        self.scrape.save()

        self.jobboard = JobBoard()
        self.jobboard.jobboard_name = self.data['job_board']['jobboard_name']
        self.jobboard.home_page = self.data['job_board']['home_page']
        self.jobboard.search_page = self.data['job_board']['search_page']

        self.jobboard.save()


    def test_is_instance(self):
        self.assertTrue(isinstance(self.instance, ScrapeJobBoard))

    def test_fields_scrape(self):
        <placeholder> = Scrape.objects.get(scrape_id=self.scrape.pk)
        <placeholder> = JobBoard.objects.get(jobboard_id=self.jobboard.pk)

        scrapejobboard = ScrapeJobBoard()
        scrapejobboard.scrape = self.scrape
        scrapejobboard.job_board = self.jobboard
        scrapejobboard.save()

        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, self.scrape)

    def test_fields_jobboard(self):
        <placeholder> = Scrape.objects.get(scrape_id=self.scrape.pk)
        <placeholder> = JobBoard.objects.get(jobboard_id=self.jobboard.pk)

        scrapejobboard = ScrapeJobBoard()
        scrapejobboard.scrape = self.scrape
        scrapejobboard.job_board = self.jobboard
        scrapejobboard.save()

        record = ScrapeJobBoard.objects.get(jobboard=<placeholder>)
        self.assertEqual(record.jobboard, self.jobboard)


class JobBoardListingTagTestCase(TestCase):
    def setUp (self):
        self.data = {
            "job_board":{                
                "jobboard_name":"CharField",
                "home_page":"URLField",
                "search_page":"URLField",
               },
            "listing_tag":{                
                "listingtag_name":"CharField",
               },
        }

        self.jobboard = JobBoard()
        self.jobboard.jobboard_name = self.data['job_board']['jobboard_name']
        self.jobboard.home_page = self.data['job_board']['home_page']
        self.jobboard.search_page = self.data['job_board']['search_page']

        self.jobboard.save()

        self.listingtag = ListingTag()
        self.listingtag.listingtag_name = self.data['listing_tag']['listingtag_name']

        self.listingtag.save()


    def test_is_instance(self):
        self.assertTrue(isinstance(self.instance, JobBoardListingTag))

    def test_fields_jobboard(self):
        <placeholder> = JobBoard.objects.get(jobboard_id=self.jobboard.pk)
        <placeholder> = ListingTag.objects.get(listingtag_id=self.listingtag.pk)

        jobboardlistingtag = JobBoardListingTag()
        jobboardlistingtag.job_board = self.jobboard
        jobboardlistingtag.listing_tag = self.listingtag
        jobboardlistingtag.save()

        record = JobBoardListingTag.objects.get(jobboard=<placeholder>)
        self.assertEqual(record.jobboard, self.jobboard)

    def test_fields_listingtag(self):
        <placeholder> = JobBoard.objects.get(jobboard_id=self.jobboard.pk)
        <placeholder> = ListingTag.objects.get(listingtag_id=self.listingtag.pk)

        jobboardlistingtag = JobBoardListingTag()
        jobboardlistingtag.job_board = self.jobboard
        jobboardlistingtag.listing_tag = self.listingtag
        jobboardlistingtag.save()

        record = JobBoardListingTag.objects.get(listingtag=<placeholder>)
        self.assertEqual(record.listingtag, self.listingtag)


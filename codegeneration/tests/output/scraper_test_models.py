from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag
from django.test import TestCase
import datetime
from model_mommy import mommy
from scraper.models import JobBoard,ListingTag,Scrape,ScrapeJobBoard,JobBoardListingTag


class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_jobboard_id(self):
        pass

    def test_fields_jobboard_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.jobboard_name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(jobboard_name=<placeholder>)
        self.assertEqual(record.jobboard_name, <placeholder>)

    def test_fields_home_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page=<placeholder>)
        self.assertEqual(record.home_page, <placeholder>)

    def test_fields_search_page(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page=<placeholder>)
        self.assertEqual(record.search_page, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_listingtag_id(self):
        pass

    def test_fields_listingtag_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.listingtag_name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(listingtag_name=<placeholder>)
        self.assertEqual(record.listingtag_name, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_scrape_id(self):
        pass

    def test_fields_scrape_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_date=<placeholder>)
        self.assertEqual(record.scrape_date, <placeholder>)

    def test_fields_entries_scraped(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_scraped = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_scraped=<placeholder>)
        self.assertEqual(record.entries_scraped, <placeholder>)

    def test_fields_scrape_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_duration=<placeholder>)
        self.assertEqual(record.scrape_duration, <placeholder>)

    def test_fields_scrape_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.scrape_success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(scrape_success=<placeholder>)
        self.assertEqual(record.scrape_success, <placeholder>)



class ScrapeJobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ScrapeJobBoard)
        self.assertTrue(isinstance(thing, ScrapeJobBoard))

    def test_fields_scrapejobboard_id(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ScrapeJobBoard()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ScrapeJobBoard.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)



class JobBoardListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoardListingTag)
        self.assertTrue(isinstance(thing, JobBoardListingTag))

    def test_fields_jobboardlistingtag_id(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobBoardListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobBoardListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)


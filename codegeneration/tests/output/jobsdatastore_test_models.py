from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import Company,Technology,CompanyTechnology


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



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_company_id(self):
        pass

    def test_fields_company_name(self):
        company = Company()
        <placeholder>
        company.company_name = <placeholder>
        company.save()
        record = Company.objects.get(company_name=<placeholder>)
        self.assertEqual(record.company_name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_technology_id(self):
        pass

    def test_fields_technology_name(self):
        technology = Technology()
        <placeholder>
        technology.technology_name = <placeholder>
        technology.save()
        record = Technology.objects.get(technology_name=<placeholder>)
        self.assertEqual(record.technology_name, <placeholder>)



class CompanyTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(CompanyTechnology)
        self.assertTrue(isinstance(thing, CompanyTechnology))

    def test_fields_companytechnology_id(self):
        pass

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = CompanyTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = CompanyTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)

    def test_fields_companytechnology_date_created(self):
        companytechnology = CompanyTechnology()
        <placeholder>
        companytechnology.companytechnology_date_created = <placeholder>
        companytechnology.save()
        record = CompanyTechnology.objects.get(companytechnology_date_created=<placeholder>)
        self.assertEqual(record.companytechnology_date_created, <placeholder>)


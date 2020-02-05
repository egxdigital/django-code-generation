from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import JobBoard,Scrape,JobTitle,JobDescription,Company,ListingTag,Technology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import JobBoard,Scrape,JobTitle,JobDescription,Company,ListingTag,Technology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import JobBoard,Scrape,JobTitle,JobDescription,Company,ListingTag,Technology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import JobBoard,Scrape,JobTitle,JobDescription,Company,ListingTag,Technology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatastore.models import JobBoard,Scrape,JobTitle,JobDescription,Company,ListingTag,Technology


class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_id_job_board(self):
        pass

    def test_fields_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_home_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page_link=<placeholder>)
        self.assertEqual(record.home_page_link, <placeholder>)

    def test_fields_search_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page_link=<placeholder>)
        self.assertEqual(record.search_page_link, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_id_scrape(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = Scrape()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = Scrape.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(date=<placeholder>)
        self.assertEqual(record.date, <placeholder>)

    def test_fields_entries_made(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_made = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_made=<placeholder>)
        self.assertEqual(record.entries_made, <placeholder>)

    def test_fields_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(duration=<placeholder>)
        self.assertEqual(record.duration, <placeholder>)

    def test_fields_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(success=<placeholder>)
        self.assertEqual(record.success, <placeholder>)



class JobTitleTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobTitle)
        self.assertTrue(isinstance(thing, JobTitle))

    def test_fields_id_job_title(self):
        pass

    def test_fields_name(self):
        jobtitle = JobTitle()
        <placeholder>
        jobtitle.name = <placeholder>
        jobtitle.save()
        record = JobTitle.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobDescriptionTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobDescription)
        self.assertTrue(isinstance(thing, JobDescription))

    def test_fields_id_job_description(self):
        pass

    def test_fields_text(self):
        jobdescription = JobDescription()
        <placeholder>
        jobdescription.text = <placeholder>
        jobdescription.save()
        record = JobDescription.objects.get(text=<placeholder>)
        self.assertEqual(record.text, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_id_company(self):
        pass

    def test_fields_name(self):
        company = Company()
        <placeholder>
        company.name = <placeholder>
        company.save()
        record = Company.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_id_listing_tag(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_id_technology(self):
        pass

    def test_fields_name(self):
        technology = Technology()
        <placeholder>
        technology.name = <placeholder>
        technology.save()
        record = Technology.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_id_job_board(self):
        pass

    def test_fields_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_home_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page_link=<placeholder>)
        self.assertEqual(record.home_page_link, <placeholder>)

    def test_fields_search_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page_link=<placeholder>)
        self.assertEqual(record.search_page_link, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_id_scrape(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = Scrape()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = Scrape.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(date=<placeholder>)
        self.assertEqual(record.date, <placeholder>)

    def test_fields_entries_made(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_made = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_made=<placeholder>)
        self.assertEqual(record.entries_made, <placeholder>)

    def test_fields_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(duration=<placeholder>)
        self.assertEqual(record.duration, <placeholder>)

    def test_fields_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(success=<placeholder>)
        self.assertEqual(record.success, <placeholder>)



class JobTitleTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobTitle)
        self.assertTrue(isinstance(thing, JobTitle))

    def test_fields_id_job_title(self):
        pass

    def test_fields_name(self):
        jobtitle = JobTitle()
        <placeholder>
        jobtitle.name = <placeholder>
        jobtitle.save()
        record = JobTitle.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobDescriptionTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobDescription)
        self.assertTrue(isinstance(thing, JobDescription))

    def test_fields_id_job_description(self):
        pass

    def test_fields_text(self):
        jobdescription = JobDescription()
        <placeholder>
        jobdescription.text = <placeholder>
        jobdescription.save()
        record = JobDescription.objects.get(text=<placeholder>)
        self.assertEqual(record.text, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_id_company(self):
        pass

    def test_fields_name(self):
        company = Company()
        <placeholder>
        company.name = <placeholder>
        company.save()
        record = Company.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_id_listing_tag(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_id_technology(self):
        pass

    def test_fields_name(self):
        technology = Technology()
        <placeholder>
        technology.name = <placeholder>
        technology.save()
        record = Technology.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_id_job_board(self):
        pass

    def test_fields_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_home_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page_link=<placeholder>)
        self.assertEqual(record.home_page_link, <placeholder>)

    def test_fields_search_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page_link=<placeholder>)
        self.assertEqual(record.search_page_link, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_id_scrape(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = Scrape()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = Scrape.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(date=<placeholder>)
        self.assertEqual(record.date, <placeholder>)

    def test_fields_entries_made(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_made = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_made=<placeholder>)
        self.assertEqual(record.entries_made, <placeholder>)

    def test_fields_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(duration=<placeholder>)
        self.assertEqual(record.duration, <placeholder>)

    def test_fields_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(success=<placeholder>)
        self.assertEqual(record.success, <placeholder>)



class JobTitleTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobTitle)
        self.assertTrue(isinstance(thing, JobTitle))

    def test_fields_id_job_title(self):
        pass

    def test_fields_name(self):
        jobtitle = JobTitle()
        <placeholder>
        jobtitle.name = <placeholder>
        jobtitle.save()
        record = JobTitle.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobDescriptionTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobDescription)
        self.assertTrue(isinstance(thing, JobDescription))

    def test_fields_id_job_description(self):
        pass

    def test_fields_text(self):
        jobdescription = JobDescription()
        <placeholder>
        jobdescription.text = <placeholder>
        jobdescription.save()
        record = JobDescription.objects.get(text=<placeholder>)
        self.assertEqual(record.text, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_id_company(self):
        pass

    def test_fields_name(self):
        company = Company()
        <placeholder>
        company.name = <placeholder>
        company.save()
        record = Company.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_id_listing_tag(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_id_technology(self):
        pass

    def test_fields_name(self):
        technology = Technology()
        <placeholder>
        technology.name = <placeholder>
        technology.save()
        record = Technology.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_id_job_board(self):
        pass

    def test_fields_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_home_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page_link=<placeholder>)
        self.assertEqual(record.home_page_link, <placeholder>)

    def test_fields_search_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page_link=<placeholder>)
        self.assertEqual(record.search_page_link, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_id_scrape(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = Scrape()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = Scrape.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(date=<placeholder>)
        self.assertEqual(record.date, <placeholder>)

    def test_fields_entries_made(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_made = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_made=<placeholder>)
        self.assertEqual(record.entries_made, <placeholder>)

    def test_fields_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(duration=<placeholder>)
        self.assertEqual(record.duration, <placeholder>)

    def test_fields_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(success=<placeholder>)
        self.assertEqual(record.success, <placeholder>)



class JobTitleTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobTitle)
        self.assertTrue(isinstance(thing, JobTitle))

    def test_fields_id_job_title(self):
        pass

    def test_fields_name(self):
        jobtitle = JobTitle()
        <placeholder>
        jobtitle.name = <placeholder>
        jobtitle.save()
        record = JobTitle.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobDescriptionTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobDescription)
        self.assertTrue(isinstance(thing, JobDescription))

    def test_fields_id_job_description(self):
        pass

    def test_fields_text(self):
        jobdescription = JobDescription()
        <placeholder>
        jobdescription.text = <placeholder>
        jobdescription.save()
        record = JobDescription.objects.get(text=<placeholder>)
        self.assertEqual(record.text, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_id_company(self):
        pass

    def test_fields_name(self):
        company = Company()
        <placeholder>
        company.name = <placeholder>
        company.save()
        record = Company.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_id_listing_tag(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_id_technology(self):
        pass

    def test_fields_name(self):
        technology = Technology()
        <placeholder>
        technology.name = <placeholder>
        technology.save()
        record = Technology.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobBoardTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobBoard)
        self.assertTrue(isinstance(thing, JobBoard))

    def test_fields_id_job_board(self):
        pass

    def test_fields_name(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.name = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_home_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.home_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(home_page_link=<placeholder>)
        self.assertEqual(record.home_page_link, <placeholder>)

    def test_fields_search_page_link(self):
        jobboard = JobBoard()
        <placeholder>
        jobboard.search_page_link = <placeholder>
        jobboard.save()
        record = JobBoard.objects.get(search_page_link=<placeholder>)
        self.assertEqual(record.search_page_link, <placeholder>)



class ScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Scrape)
        self.assertTrue(isinstance(thing, Scrape))

    def test_fields_id_scrape(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = Scrape()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = Scrape.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_date(self):
        scrape = Scrape()
        <placeholder>
        scrape.date = <placeholder>
        scrape.save()
        record = Scrape.objects.get(date=<placeholder>)
        self.assertEqual(record.date, <placeholder>)

    def test_fields_entries_made(self):
        scrape = Scrape()
        <placeholder>
        scrape.entries_made = <placeholder>
        scrape.save()
        record = Scrape.objects.get(entries_made=<placeholder>)
        self.assertEqual(record.entries_made, <placeholder>)

    def test_fields_duration(self):
        scrape = Scrape()
        <placeholder>
        scrape.duration = <placeholder>
        scrape.save()
        record = Scrape.objects.get(duration=<placeholder>)
        self.assertEqual(record.duration, <placeholder>)

    def test_fields_success(self):
        scrape = Scrape()
        <placeholder>
        scrape.success = <placeholder>
        scrape.save()
        record = Scrape.objects.get(success=<placeholder>)
        self.assertEqual(record.success, <placeholder>)



class JobTitleTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobTitle)
        self.assertTrue(isinstance(thing, JobTitle))

    def test_fields_id_job_title(self):
        pass

    def test_fields_name(self):
        jobtitle = JobTitle()
        <placeholder>
        jobtitle.name = <placeholder>
        jobtitle.save()
        record = JobTitle.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class JobDescriptionTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobDescription)
        self.assertTrue(isinstance(thing, JobDescription))

    def test_fields_id_job_description(self):
        pass

    def test_fields_text(self):
        jobdescription = JobDescription()
        <placeholder>
        jobdescription.text = <placeholder>
        jobdescription.save()
        record = JobDescription.objects.get(text=<placeholder>)
        self.assertEqual(record.text, <placeholder>)



class CompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Company)
        self.assertTrue(isinstance(thing, Company))

    def test_fields_id_company(self):
        pass

    def test_fields_name(self):
        company = Company()
        <placeholder>
        company.name = <placeholder>
        company.save()
        record = Company.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)

    def test_fields_hiring_from(self):
        company = Company()
        <placeholder>
        company.hiring_from = <placeholder>
        company.save()
        record = Company.objects.get(hiring_from=<placeholder>)
        self.assertEqual(record.hiring_from, <placeholder>)



class ListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(ListingTag)
        self.assertTrue(isinstance(thing, ListingTag))

    def test_fields_id_listing_tag(self):
        pass

    def test_fields_job_board(self):
        job_board = None()
        job_board.<placeholder> = <placeholder>
        job_board.save()
        <placeholder>
        <placeholder> = ListingTag()
        <placeholder>.job_board = job_board
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = ListingTag.objects.get(job_board=<placeholder>)
        self.assertEqual(record.job_board, <placeholder>)

    def test_fields_name(self):
        listingtag = ListingTag()
        <placeholder>
        listingtag.name = <placeholder>
        listingtag.save()
        record = ListingTag.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)



class TechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(Technology)
        self.assertTrue(isinstance(thing, Technology))

    def test_fields_id_technology(self):
        pass

    def test_fields_name(self):
        technology = Technology()
        <placeholder>
        technology.name = <placeholder>
        technology.save()
        record = Technology.objects.get(name=<placeholder>)
        self.assertEqual(record.name, <placeholder>)


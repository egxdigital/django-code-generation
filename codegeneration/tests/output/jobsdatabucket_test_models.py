from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostCompany,JobPostListingTag,JobPostScrape,JobPostTechnology


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



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)



class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_jobpost_id(self):
        pass

    def test_fields_job_title(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_title = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_date_posted(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.date_posted = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(date_posted=<placeholder>)
        self.assertEqual(record.date_posted, <placeholder>)

    def test_fields_apply_link(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.apply_link = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(apply_link=<placeholder>)
        self.assertEqual(record.apply_link, <placeholder>)

    def test_fields_job_description(self):
        jobpost = JobPost()
        <placeholder>
        jobpost.job_description = <placeholder>
        jobpost.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)



class JobPostCompanyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostCompany)
        self.assertTrue(isinstance(thing, JobPostCompany))

    def test_fields_jobpostcompany_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPostCompany()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostCompany.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_jobpostlistingtag_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_listing_tag(self):
        listing_tag = None()
        listing_tag.<placeholder> = <placeholder>
        listing_tag.save()
        <placeholder>
        <placeholder> = JobPostListingTag()
        <placeholder>.listing_tag = listing_tag
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostListingTag.objects.get(listing_tag=<placeholder>)
        self.assertEqual(record.listing_tag, <placeholder>)



class JobPostScrapeTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostScrape)
        self.assertTrue(isinstance(thing, JobPostScrape))

    def test_fields_jobpostscrape_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPostScrape()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostScrape.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_jobposttechnology_id(self):
        pass

    def test_fields_job_post(self):
        job_post = None()
        job_post.<placeholder> = <placeholder>
        job_post.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.job_post = job_post
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(job_post=<placeholder>)
        self.assertEqual(record.job_post, <placeholder>)

    def test_fields_technology(self):
        technology = None()
        technology.<placeholder> = <placeholder>
        technology.save()
        <placeholder>
        <placeholder> = JobPostTechnology()
        <placeholder>.technology = technology
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPostTechnology.objects.get(technology=<placeholder>)
        self.assertEqual(record.technology, <placeholder>)


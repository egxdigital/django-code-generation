from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostListingTag,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostListingTag,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostListingTag,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostListingTag,JobPostTechnology
from django.test import TestCase
import datetime
from model_mommy import mommy
from jobsdatabucket.models import JobPost,JobPostListingTag,JobPostTechnology


class JobPostTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPost)
        self.assertTrue(isinstance(thing, JobPost))

    def test_fields_id_job_post(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_title(self):
        job_title = None()
        job_title.<placeholder> = <placeholder>
        job_title.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_title = job_title
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_job_description(self):
        job_description = None()
        job_description.<placeholder> = <placeholder>
        job_description.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_description = job_description
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

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



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_id_job_post_listing_tag(self):
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



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_id_job_post_technology(self):
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

    def test_fields_id_job_post(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_title(self):
        job_title = None()
        job_title.<placeholder> = <placeholder>
        job_title.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_title = job_title
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_job_description(self):
        job_description = None()
        job_description.<placeholder> = <placeholder>
        job_description.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_description = job_description
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

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



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_id_job_post_listing_tag(self):
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



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_id_job_post_technology(self):
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

    def test_fields_id_job_post(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_title(self):
        job_title = None()
        job_title.<placeholder> = <placeholder>
        job_title.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_title = job_title
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_job_description(self):
        job_description = None()
        job_description.<placeholder> = <placeholder>
        job_description.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_description = job_description
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

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



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_id_job_post_listing_tag(self):
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



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_id_job_post_technology(self):
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

    def test_fields_id_job_post(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_title(self):
        job_title = None()
        job_title.<placeholder> = <placeholder>
        job_title.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_title = job_title
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_job_description(self):
        job_description = None()
        job_description.<placeholder> = <placeholder>
        job_description.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_description = job_description
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

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



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_id_job_post_listing_tag(self):
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



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_id_job_post_technology(self):
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

    def test_fields_id_job_post(self):
        pass

    def test_fields_scrape(self):
        scrape = None()
        scrape.<placeholder> = <placeholder>
        scrape.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.scrape = scrape
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(scrape=<placeholder>)
        self.assertEqual(record.scrape, <placeholder>)

    def test_fields_job_title(self):
        job_title = None()
        job_title.<placeholder> = <placeholder>
        job_title.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_title = job_title
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_title=<placeholder>)
        self.assertEqual(record.job_title, <placeholder>)

    def test_fields_job_description(self):
        job_description = None()
        job_description.<placeholder> = <placeholder>
        job_description.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.job_description = job_description
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(job_description=<placeholder>)
        self.assertEqual(record.job_description, <placeholder>)

    def test_fields_company(self):
        company = None()
        company.<placeholder> = <placeholder>
        company.save()
        <placeholder>
        <placeholder> = JobPost()
        <placeholder>.company = company
        <placeholder>.<placeholder> = <placeholder>
        <placeholder>.save()
        record = JobPost.objects.get(company=<placeholder>)
        self.assertEqual(record.company, <placeholder>)

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



class JobPostListingTagTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostListingTag)
        self.assertTrue(isinstance(thing, JobPostListingTag))

    def test_fields_id_job_post_listing_tag(self):
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



class JobPostTechnologyTestCase(TestCase):
    def test_is_instance(self):
        thing = mommy.make(JobPostTechnology)
        self.assertTrue(isinstance(thing, JobPostTechnology))

    def test_fields_id_job_post_technology(self):
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


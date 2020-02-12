from django.db import models
import uuid

class JobPost(models.Model):
    jobpost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=250)
    date_posted = models.DateField(auto_now=False, auto_now_add=False)
    apply_link = models.URLField(null=True)
    job_description = models.CharField(max_length=250)


class JobPostCompany(models.Model):
    jobpostcompany_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    company = models.ForeignKey('jobsdatastore.Company',on_delete=models.CASCADE,)


class JobPostListingTag(models.Model):
    jobpostlistingtag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    listing_tag = models.ForeignKey('scraper.ListingTag',on_delete=models.CASCADE,)


class JobPostScrape(models.Model):
    jobpostscrape_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    scrape = models.ForeignKey('scraper.Scrape',on_delete=models.CASCADE,)


class JobPostTechnology(models.Model):
    jobposttechnology_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    technology = models.ForeignKey('jobsdatastore.Technology',on_delete=models.CASCADE,)

from django.db import models
import uuid

class JobPost(models.Model):
    """A job post is an advertisement for an open position."""
    jobpost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=250)
    date_posted = models.DateField(auto_now=False, auto_now_add=False)
    apply_link = models.URLField(null=True)
    job_description = models.CharField(max_length=250)


class JobPostCompany(models.Model):
    """Companies advertise for an open position more than once and post multiple job posts for different positions."""
    jobpostcompany_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    company = models.ForeignKey('jobsdatastore.Company',on_delete=models.CASCADE,)


class JobPostListingTag(models.Model):
    """A job post can contain multiple listing tags and a given listing tag can appear on any number of job posts."""
    jobpostlistingtag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    listing_tag = models.ForeignKey('scraper.ListingTag',on_delete=models.CASCADE,)


class JobPostScrape(models.Model):
    """A job post can appear in multiple scrapes and scrapes pull many job posts."""
    jobpostscrape_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    scrape = models.ForeignKey('scraper.Scrape',on_delete=models.CASCADE,)


class JobPostTechnology(models.Model):
    """A job post can contain multiple technologies and a given technology can appear on any number of job posts."""
    jobposttechnology_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    technology = models.ForeignKey('jobsdatastore.Technology',on_delete=models.CASCADE,)

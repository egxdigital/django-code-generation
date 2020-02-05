from django.db import models
import uuid


class JobPost(models.Model):
    id_job_post = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scrape = models.ForeignKey('jobsdatastore.Scrape',on_delete=models.CASCADE,)
    job_title = models.ForeignKey('jobsdatastore.JobTitle',on_delete=models.CASCADE,)
    job_description = models.ForeignKey('jobsdatastore.JobDescription',on_delete=models.CASCADE,)
    company = models.ForeignKey('jobsdatastore.Company',on_delete=models.CASCADE,)
    date_posted = models.DateField(auto_now=False, auto_now_add=False)
    apply_link = models.URLField(null=True)


class JobPostListingTag(models.Model):
    id_job_post_listing_tag = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    listing_tag = models.ForeignKey('jobsdatastore.ListingTag',on_delete=models.CASCADE,)


class JobPostTechnology(models.Model):
    id_job_post_technology = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_post = models.ForeignKey('jobsdatabucket.JobPost',on_delete=models.CASCADE,)
    technology = models.ForeignKey('jobsdatastore.Technology',on_delete=models.CASCADE,)

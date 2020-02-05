from django.db import models
import uuid


class JobBoard(models.Model):
    id_job_board = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    home_page_link = models.URLField(null=True)
    search_page_link = models.URLField(null=True)


class Scrape(models.Model):
    id_scrape = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_board = models.ForeignKey('jobsdatastore.JobBoard',on_delete=models.CASCADE,)
    date = models.DateField(auto_now=False, auto_now_add=False)
    entries_made = models.IntegerField(null=True)
    duration = models.DurationField(null=True)
    success = models.BooleanField()


class JobTitle(models.Model):
    id_job_title = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)


class JobDescription(models.Model):
    id_job_description = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()

class Company(models.Model):
    id_company = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    hiring_from = models.CharField(max_length=250)


class ListingTag(models.Model):
    id_listing_tag = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_board = models.ForeignKey('jobsdatastore.JobBoard',on_delete=models.CASCADE,)
    name = models.CharField(max_length=250)


class Technology(models.Model):
    id_technology = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

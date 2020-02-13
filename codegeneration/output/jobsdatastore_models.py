from django.db import models
import uuid

class Company(models.Model):
    """A company is an entity that posts for open positions on job boards."""
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=250)
    hiring_from = models.CharField(max_length=250)


class Technology(models.Model):
    """A technology is a tool accepted by industry and a skill required by a position advertised as a job post."""
    technology_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    technology_name = models.CharField(max_length=250)


class CompanyTechnology(models.Model):
    """A technology is associated with a company once the company advertises an open position for which the technology is required."""
    companytechnology_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('jobsdatastore.Company',on_delete=models.CASCADE,)
    technology = models.ForeignKey('jobsdatastore.Technology',on_delete=models.CASCADE,)
    companytechnology_date_created = models.DateField(auto_now=False, auto_now_add=False)

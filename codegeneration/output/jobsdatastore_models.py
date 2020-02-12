from django.db import models
import uuid

class Company(models.Model):
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=250)
    hiring_from = models.CharField(max_length=250)


class Technology(models.Model):
    technology_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    technology_name = models.CharField(max_length=250)


class CompanyTechnology(models.Model):
    companytechnology_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('jobsdatastore.Company',on_delete=models.CASCADE,)
    technology = models.ForeignKey('jobsdatastore.Technology',on_delete=models.CASCADE,)
    companytechnology_date_created = models.DateField(auto_now=False, auto_now_add=False)

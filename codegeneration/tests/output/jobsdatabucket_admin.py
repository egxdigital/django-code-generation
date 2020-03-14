"""Admin - jobsdatabucket

This module contains the configuration for the Django admin site
"""
from django.contrib import admin
from jobsdatabucket.models import JobPost, JobPostCompany, JobPostListingTag, JobPostScrape, JobPostTechnology

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    pass

@admin.register(JobPostCompany)
class JobPostCompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(JobPostListingTag)
class JobPostListingTagAdmin(admin.ModelAdmin):
    pass

@admin.register(JobPostScrape)
class JobPostScrapeAdmin(admin.ModelAdmin):
    pass

@admin.register(JobPostTechnology)
class JobPostTechnologyAdmin(admin.ModelAdmin):
    pass


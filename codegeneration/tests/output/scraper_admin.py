"""Admin - scraper

This module contains the admin configuration for the Django admin site
"""
from django.contrib import admin
from scraper.models import JobBoard, ListingTag, Scrape, ScrapeJobBoard, JobBoardListingTag

@admin.register(JobBoard)
class JobBoardAdmin(admin.ModelAdmin):
    pass

@admin.register(ListingTag)
class ListingTagAdmin(admin.ModelAdmin):
    pass

@admin.register(Scrape)
class ScrapeAdmin(admin.ModelAdmin):
    pass

@admin.register(ScrapeJobBoard)
class ScrapeJobBoardAdmin(admin.ModelAdmin):
    pass

@admin.register(JobBoardListingTag)
class JobBoardListingTagAdmin(admin.ModelAdmin):
    pass


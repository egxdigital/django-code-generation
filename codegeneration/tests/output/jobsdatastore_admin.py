"""Admin - jobsdatastore

This module contains the configuration for the Django admin site
"""
from django.contrib import admin
from jobsdatastore.models import Company, Technology, CompanyTechnology

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass

@admin.register(CompanyTechnology)
class CompanyTechnologyAdmin(admin.ModelAdmin):
    pass


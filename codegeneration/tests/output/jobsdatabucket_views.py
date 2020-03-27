"""Views - jobsdatabucket

This module contains the views for the jobsdatabucket application.

"""
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from jobsdatabucket.models import JobPost, JobPostCompany, JobPostListingTag, JobPostScrape, JobPostTechnology
from jobsdatabucket.api.serializers import JobPostSerializer, JobPostCompanyPostSerializer, JobPostCompanyGetSerializer, JobPostListingTagPostSerializer, JobPostListingTagGetSerializer, JobPostScrapePostSerializer, JobPostScrapeGetSerializer, JobPostTechnologyPostSerializer, JobPostTechnologyGetSerializer


class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class JobPostCompanyViewSet(viewsets.ModelViewSet):
    queryset = JobPostCompany.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
             return JobPostCompanyPostSerializer
        return JobPostCompanyGetSerializer


class JobPostListingTagViewSet(viewsets.ModelViewSet):
    queryset = JobPostListingTag.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
             return JobPostListingTagPostSerializer
        return JobPostListingTagGetSerializer


class JobPostScrapeViewSet(viewsets.ModelViewSet):
    queryset = JobPostScrape.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
             return JobPostScrapePostSerializer
        return JobPostScrapeGetSerializer


class JobPostTechnologyViewSet(viewsets.ModelViewSet):
    queryset = JobPostTechnology.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
             return JobPostTechnologyPostSerializer
        return JobPostTechnologyGetSerializer


"""Views - jobsdatabucket

This module contains the views for the jobsdatabucket application.

"""
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from jobsdatabucket.models import JobPost, JobPostCompany, JobPostListingTag, JobPostScrape, JobPostTechnology
from jobsdatabucket.api.serializers import JobPostSerializer, JobPostCompanySerializer, JobPostListingTagSerializer, JobPostScrapeSerializer, JobPostTechnologySerializer

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class JobPostCompanyViewSet(viewsets.ModelViewSet):
    queryset = JobPostCompany.objects.all()
    serializer_class = JobPostCompanySerializer


class JobPostListingTagViewSet(viewsets.ModelViewSet):
    queryset = JobPostListingTag.objects.all()
    serializer_class = JobPostListingTagSerializer


class JobPostScrapeViewSet(viewsets.ModelViewSet):
    queryset = JobPostScrape.objects.all()
    serializer_class = JobPostScrapeSerializer


class JobPostTechnologyViewSet(viewsets.ModelViewSet):
    queryset = JobPostTechnology.objects.all()
    serializer_class = JobPostTechnologySerializer



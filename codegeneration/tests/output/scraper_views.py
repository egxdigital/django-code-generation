"""Views - scraper

This module contains the views for the scraper application.

"""
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from scraper.models import JobBoard, ListingTag, Scrape, ScrapeJobBoard, JobBoardListingTag
from scraper.api.serializers import JobBoardSerializer, ListingTagSerializer, ScrapeSerializer, ScrapeJobBoardSerializer, JobBoardListingTagSerializer

class JobBoardViewSet(viewsets.ModelViewSet):
    queryset = JobBoard.objects.all()
    serializer_class = JobBoardSerializer


class ListingTagViewSet(viewsets.ModelViewSet):
    queryset = ListingTag.objects.all()
    serializer_class = ListingTagSerializer


class ScrapeViewSet(viewsets.ModelViewSet):
    queryset = Scrape.objects.all()
    serializer_class = ScrapeSerializer


class ScrapeJobBoardViewSet(viewsets.ModelViewSet):
    queryset = ScrapeJobBoard.objects.all()
    serializer_class = ScrapeJobBoardSerializer


class JobBoardListingTagViewSet(viewsets.ModelViewSet):
    queryset = JobBoardListingTag.objects.all()
    serializer_class = JobBoardListingTagSerializer



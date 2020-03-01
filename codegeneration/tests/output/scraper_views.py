"""Views - scraper
This module contains the views for the scraper application.

"""
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from scraper.models import JobBoard, ListingTag, Scrape, ScrapeJobBoard, JobBoardListingTag
from scraper.api.serializers import JobBoardSerializer, ListingTagSerializer, ScrapeSerializer, ScrapeJobBoardSerializer, JobBoardListingTagSerializer

@permission_classes((AllowAny, ))
class JobBoardViewSet(viewsets.ModelViewSet):
    queryset = JobBoard.objects.all()
    serializer_class = JobBoardSerializer


@permission_classes((AllowAny, ))
class ListingTagViewSet(viewsets.ModelViewSet):
    queryset = ListingTag.objects.all()
    serializer_class = ListingTagSerializer


@permission_classes((AllowAny, ))
class ScrapeViewSet(viewsets.ModelViewSet):
    queryset = Scrape.objects.all()
    serializer_class = ScrapeSerializer


@permission_classes((AllowAny, ))
class ScrapeJobBoardViewSet(viewsets.ModelViewSet):
    queryset = ScrapeJobBoard.objects.all()
    serializer_class = ScrapeJobBoardSerializer


@permission_classes((AllowAny, ))
class JobBoardListingTagViewSet(viewsets.ModelViewSet):
    queryset = JobBoardListingTag.objects.all()
    serializer_class = JobBoardListingTagSerializer



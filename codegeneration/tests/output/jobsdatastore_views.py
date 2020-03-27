"""Views - jobsdatastore

This module contains the views for the jobsdatastore application.

"""
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from jobsdatastore.models import Company, Technology, CompanyTechnology
from jobsdatastore.api.serializers import CompanySerializer, TechnologySerializer, CompanyTechnologyPostSerializer, CompanyTechnologyGetSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class CompanyTechnologyViewSet(viewsets.ModelViewSet):
    queryset = CompanyTechnology.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
             return CompanyTechnologyPostSerializer
        return CompanyTechnologyGetSerializer


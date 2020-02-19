from django.urls import path
from jobsdatastore.api import views

urlpatterns = [
    path('api/companies/',
        views.CompanyListCreateAPIView.as_view(),
        name='company-list'),

    path('api/company/<PLACEHOLDER>/',
        views.CompanyRetrieveUpdateDestroyAPIView.as_view(),
        name='company-detail'),

    path('api/technologies/',
        views.TechnologyListCreateAPIView.as_view(),
        name='technology-list'),

    path('api/technology/<PLACEHOLDER>/',
        views.TechnologyRetrieveUpdateDestroyAPIView.as_view(),
        name='technology-detail'),

    path('api/companytechnologies/',
        views.CompanyTechnologyListCreateAPIView.as_view(),
        name='companytechnology-list'),

    path('api/companytechnology/<PLACEHOLDER>/',
        views.CompanyTechnologyRetrieveUpdateDestroyAPIView.as_view(),
        name='companytechnology-detail'),

]

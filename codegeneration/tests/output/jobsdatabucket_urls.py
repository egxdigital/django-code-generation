from django.urls import path
from jobsdatabucket.api import views

urlpatterns = [
    path('api/jobposts/',
        views.JobPostListCreateAPIView.as_view(),
        name='jobpost-list'),

    path('api/jobpost/<PLACEHOLDER>/',
        views.JobPostRetrieveUpdateDestroyAPIView.as_view(),
        name='jobpost-detail'),

    path('api/jobpostcompanies/',
        views.JobPostCompanyListCreateAPIView.as_view(),
        name='jobpostcompany-list'),

    path('api/jobpostcompany/<PLACEHOLDER>/',
        views.JobPostCompanyRetrieveUpdateDestroyAPIView.as_view(),
        name='jobpostcompany-detail'),

    path('api/jobpostlistingtags/',
        views.JobPostListingTagListCreateAPIView.as_view(),
        name='jobpostlistingtag-list'),

    path('api/jobpostlistingtag/<PLACEHOLDER>/',
        views.JobPostListingTagRetrieveUpdateDestroyAPIView.as_view(),
        name='jobpostlistingtag-detail'),

    path('api/jobpostscrapes/',
        views.JobPostScrapeListCreateAPIView.as_view(),
        name='jobpostscrape-list'),

    path('api/jobpostscrape/<PLACEHOLDER>/',
        views.JobPostScrapeRetrieveUpdateDestroyAPIView.as_view(),
        name='jobpostscrape-detail'),

    path('api/jobposttechnologies/',
        views.JobPostTechnologyListCreateAPIView.as_view(),
        name='jobposttechnology-list'),

    path('api/jobposttechnology/<PLACEHOLDER>/',
        views.JobPostTechnologyRetrieveUpdateDestroyAPIView.as_view(),
        name='jobposttechnology-detail'),

]

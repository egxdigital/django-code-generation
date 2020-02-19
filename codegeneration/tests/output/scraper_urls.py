from django.urls import path
from scraper.api import views

urlpatterns = [
    path('api/jobboards/',
        views.JobBoardListCreateAPIView.as_view(),
        name='jobboard-list'),

    path('api/jobboard/<PLACEHOLDER>/',
        views.JobBoardRetrieveUpdateDestroyAPIView.as_view(),
        name='jobboard-detail'),

    path('api/listingtags/',
        views.ListingTagListCreateAPIView.as_view(),
        name='listingtag-list'),

    path('api/listingtag/<PLACEHOLDER>/',
        views.ListingTagRetrieveUpdateDestroyAPIView.as_view(),
        name='listingtag-detail'),

    path('api/scrapes/',
        views.ScrapeListCreateAPIView.as_view(),
        name='scrape-list'),

    path('api/scrape/<PLACEHOLDER>/',
        views.ScrapeRetrieveUpdateDestroyAPIView.as_view(),
        name='scrape-detail'),

    path('api/scrapejobboards/',
        views.ScrapeJobBoardListCreateAPIView.as_view(),
        name='scrapejobboard-list'),

    path('api/scrapejobboard/<PLACEHOLDER>/',
        views.ScrapeJobBoardRetrieveUpdateDestroyAPIView.as_view(),
        name='scrapejobboard-detail'),

    path('api/jobboardlistingtags/',
        views.JobBoardListingTagListCreateAPIView.as_view(),
        name='jobboardlistingtag-list'),

    path('api/jobboardlistingtag/<PLACEHOLDER>/',
        views.JobBoardListingTagRetrieveUpdateDestroyAPIView.as_view(),
        name='jobboardlistingtag-detail'),

]

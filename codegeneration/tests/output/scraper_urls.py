from django.urls import path
from rest_framework.routers import SimpleRouter
from scraper.api.views import JobBoardViewSet, ListingTagViewSet, ScrapeViewSet, ScrapeJobBoardViewSet, JobBoardListingTagViewSet


router = SimpleRouter()
router.register('api/jobboards', JobBoardViewSet)
router.register('api/listingtags', ListingTagViewSet)
router.register('api/scrapes', ScrapeViewSet)
router.register('api/scrapejobboards', ScrapeJobBoardViewSet)
router.register('api/jobboardlistingtags', JobBoardListingTagViewSet)

urlpatterns = router.urls
from django.urls import path
from rest_framework.routers import SimpleRouter
from jobsdatabucket.api.views import JobPostViewSet, JobPostCompanyViewSet, JobPostListingTagViewSet, JobPostScrapeViewSet, JobPostTechnologyViewSet


router = SimpleRouter()
router.register('api/jobposts', JobPostViewSet)
router.register('api/jobpostcompanies', JobPostCompanyViewSet)
router.register('api/jobpostlistingtags', JobPostListingTagViewSet)
router.register('api/jobpostscrapes', JobPostScrapeViewSet)
router.register('api/jobposttechnologies', JobPostTechnologyViewSet)

urlpatterns = router.urls
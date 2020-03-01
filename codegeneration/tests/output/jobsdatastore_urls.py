from django.urls import path
from rest_framework.routers import SimpleRouter
from jobsdatastore.api.views import CompanyViewSet, TechnologyViewSet, CompanyTechnologyViewSet


router = SimpleRouter()
router.register('api/companies', CompanyViewSet)
router.register('api/technologies', TechnologyViewSet)
router.register('api/companytechnologies', CompanyTechnologyViewSet)

urlpatterns = router.urls
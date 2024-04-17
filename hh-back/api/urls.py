from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import CompanyViewSet, VacancyViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'vacancies', VacancyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

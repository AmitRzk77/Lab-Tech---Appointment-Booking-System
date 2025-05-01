from rest_framework.routers import DefaultRouter
from ..viewsets.services_viewsets import ServiceViewsets

router = DefaultRouter()

router.register('services', ServiceViewsets, basename = 'ServicesViewsets')
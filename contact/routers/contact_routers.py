from rest_framework.routers import DefaultRouter
from ..viewsets.contact_viewsets import contactViewsets

router = DefaultRouter()

router.register('contact', contactViewsets, basename = 'contactViewsets')
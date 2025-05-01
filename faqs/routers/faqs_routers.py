from rest_framework.routers import DefaultRouter
from ..viewsets.faqs_viewsets import faqsViewsets

router = DefaultRouter()

router.register('appointments', faqsViewsets, basename = 'faqsViewsets')
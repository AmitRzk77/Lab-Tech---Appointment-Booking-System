from rest_framework.routers import DefaultRouter
from ..viewsets.social_viewsets import socialmediaViewsets

router = DefaultRouter()

router.register('social', socialmediaViewsets, basename = 'socialmediaViewsets')
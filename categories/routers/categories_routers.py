from rest_framework.routers import DefaultRouter
from ..viewsets.categories_viewsets import categoriesViewsets

router = DefaultRouter()

router.register('categories', categoriesViewsets, basename = 'categoriesViewsets')
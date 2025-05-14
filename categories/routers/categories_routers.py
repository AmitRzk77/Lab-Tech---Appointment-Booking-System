from rest_framework.routers import DefaultRouter
from ..viewsets.categories_viewsets import CategoryViewSet

router = DefaultRouter()


router.register('categories', CategoryViewSet, basename = 'categoriesViewsets')
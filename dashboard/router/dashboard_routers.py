from rest_framework.routers import DefaultRouter
from ..viewsets.dashboard_viewsets import dashboardViewSet

router = DefaultRouter()

router.register('dashboard', dashboardViewSet, basename = 'dashboardViewsets')
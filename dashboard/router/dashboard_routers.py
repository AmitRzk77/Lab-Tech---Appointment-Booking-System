from rest_framework.routers import DefaultRouter
from ..viewsets.dashboard_viewsets import dashboardViewSet

from django.urls import path, include
from ..views import dashboard_page

router = DefaultRouter()

router.register('dashboard', dashboardViewSet, basename = 'dashboardViewsets')

urlpatterns = [
    path('', include(router.urls)),  # All API endpoints (like /api/dashboard/)
    path('dashboard-page/', dashboard_page, name='dashboard-page'),  # For HTML page
]


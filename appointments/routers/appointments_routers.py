from rest_framework.routers import DefaultRouter
from ..viewsets.appointments_viewsets import appointmentsViewsets

router = DefaultRouter()

router.register('appointments', appointmentsViewsets, basename = 'appointmentsViewsets')
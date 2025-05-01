from rest_framework.routers import DefaultRouter
from ..viewsets.account_viewsets import adminPasswordResetViewSet

router = DefaultRouter()

router.register('account', adminPasswordResetViewSet , basename = 'adminPasswordResetViewset')
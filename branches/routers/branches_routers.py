from rest_framework.routers import DefaultRouter
from ..viewsets.branch_viewsets import branchesViewsets

router = DefaultRouter()

router.register('branches', branchesViewsets, basename = 'branchesViewsets')
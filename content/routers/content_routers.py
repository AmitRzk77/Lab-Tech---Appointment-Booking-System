from rest_framework.routers import DefaultRouter
from ..viewsets.content_viewsets import BannerViewSet
from ..viewsets.content_viewsets import GalleryViewSet
from ..viewsets.content_viewsets import PopUpViewSet
from ..viewsets.content_viewsets import TeamViewSet


router = DefaultRouter()


router.register('banners', BannerViewSet, basename='banners')
router.register('gallery', GalleryViewSet, basename='gallery')
router.register('popups', PopUpViewSet, basename='popups')
router.register('team', TeamViewSet, basename='team')

urlpatterns = router.urls

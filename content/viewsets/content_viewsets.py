from rest_framework import viewsets
from ..models import Banner, Gallery, PopUp, Team
from ..serializers.content_serializers import  BannerSerializer, TeamListSerializer, TeamRetrieveSerializer, TeamWriteSerializer, GallerySerializer,   PopUpListSerializer, PopUpRetrieveSerializer, PopUpWriteSerializer,GalleryImageSerializer


class BannerViewSet(viewsets.ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all().order_by('-id')

    def create(self, request, *args, **kwargs):
        old_banner = Banner.objects.first()
        if old_banner:
            old_banner.delete()
 
        return super().create(request, *args, **kwargs)
   
    def update(self, request, *args, **kwargs):
        Banner.objects.exclude(pk=kwargs['pk']).delete()
        
        return super().update(request, *args, **kwargs)

    
class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    
    
class PopUpViewSet(viewsets.ModelViewSet):
    serializer_class = PopUpListSerializer
    queryset = PopUp.objects.all().order_by('-id')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PopUpWriteSerializer
        elif self.action == 'retrieve':
            return PopUpRetrieveSerializer
        return super().get_serializer_class()
    
class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamListSerializer
    queryset = Team.objects.all().order_by('-id')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TeamWriteSerializer
        elif self.action == 'retrieve':
            return TeamRetrieveSerializer
        return super().get_serializer_class()
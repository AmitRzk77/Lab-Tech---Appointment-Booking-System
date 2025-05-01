from rest_framework import viewsets
from ..serializers.social_serializers import SocialMediaListSerializers, SocialMediaRetriveSerializers, SocialMediaWriteSerializers
from ..models import SocialMedia
#from ..utilities.pagination import MyPagenumberPagination
#from rest_framework.permissions import IsAuthenticated


class socialmediaViewsets(viewsets.ModelViewSet):
    serializer_class = SocialMediaListSerializers
    queryset = SocialMedia.objects.all().order_by('-id')
    #pagination_class = MyPagenumberPagination
   # permission_classes = [IsAuthenticated]


def get_queryset(self):
    queryset = super().get_queryset()  #here we can apply authorization for data
    return queryset

def get_serializer_class(self):
    if self.action in ['create', 'update', 'partial_update']:
        return SocialMediaWriteSerializers
    elif self.action == 'retrieve':
        return SocialMediaRetriveSerializers
    return super().get_serializer_class()

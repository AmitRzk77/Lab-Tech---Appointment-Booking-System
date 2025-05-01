from rest_framework import viewsets
from ..serializers.contact_serializers import ContactListSerializers, ContactRetriveSerializers, ConatctWriteSerializers
from ..models import Contact
#from ..utilities.pagination import MyPagenumberPagination
#from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter


class contactViewsets(viewsets.ModelViewSet):
    serializer_class = ContactListSerializers
    queryset = Contact.objects.all().order_by('-id')
    #pagination_class = MyPagenumberPagination
   # permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ["name", "email", "phone"]


def get_queryset(self):
    queryset = super().get_queryset()  #here we can apply authorization for data
    return queryset

def get_serializer_class(self):
    if self.action in ['create', 'update', 'partial_update']:
        return ConatctWriteSerializers
    elif self.action == 'retrieve':
        return ContactRetriveSerializers
    return super().get_serializer_class()

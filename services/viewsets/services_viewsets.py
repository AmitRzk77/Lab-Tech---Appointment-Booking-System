# services/views.py

from rest_framework import viewsets
from ..serializers.services_serializers import ServiceListSerializers, ServiceRetriveSerializers, ServiceWriteSerializers
from ..models import Service
# from ..utilities.pagination import MyPagenumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from ..utilities.pagination import MyPagenumberPagination

class ServiceViewsets(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('-id')
    serializer_class = ServiceListSerializers
    pagination_class = MyPagenumberPagination
    # permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ["name", "price", "category__category"]


    def get_queryset(self):
        queryset = super().get_queryset()
        category_filter = self.request.query_params.get('category', None)
        subcategory_filter = self.request.query_params.get('sub_category', None)

        if category_filter:
            queryset = queryset.filter(category_id=category_filter)

        if subcategory_filter:
            queryset = queryset.filter(sub_category_id=subcategory_filter)

        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ServiceWriteSerializers
        elif self.action == 'retrieve':
            return ServiceRetriveSerializers
        return ServiceListSerializers

from rest_framework import viewsets
from ..serializers.appointments_serializers import (
    AppointmentListSerializers, 
    AppointmentsRetriveSerializers,
    AppointmentsWriteSerializers
)
from ..models import Appointments
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# from ..utilities.pagination import MyPagenumberPagination
# from rest_framework.permissions import IsAuthenticated




class appointmentsViewsets(viewsets.ModelViewSet):
    serializer_class = AppointmentListSerializers
    queryset = Appointments.objects.all().order_by('-id')
    # pagination_class = MyPagenumberPagination
    # permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ["name", "email", "phone"]
    filterset_fields = ['service', 'payment_option']

    def get_queryset(self):
        queryset = super().get_queryset()  # Here you can apply authorization or dynamic filtering
        
        category_filter = self.request.query_params.get('category', None)
        subcategory_filter = self.request.query_params.get('sub_category', None)
        service_filter = self.request.query_params.get('service', None)

        if category_filter:
            queryset = queryset.filter(category_id=category_filter)

        if subcategory_filter:
            queryset = queryset.filter(sub_category_id=subcategory_filter)

        if service_filter:
            queryset = queryset.filter(service_id=service_filter)

        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AppointmentsWriteSerializers
        elif self.action == 'retrieve':
            return AppointmentsRetriveSerializers
        return super().get_serializer_class()

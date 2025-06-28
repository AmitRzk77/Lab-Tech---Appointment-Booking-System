from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from ..models import Appointments
from ..serializers.appointments_serializers import (
    AppointmentListSerializers,
    AppointmentsRetriveSerializers,
    AppointmentsWriteSerializers
)

class appointmentsViewsets(viewsets.ModelViewSet):
    queryset = Appointments.objects.all().order_by('-id')
    serializer_class = AppointmentListSerializers

    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ["name", "email", "phone_number"]
    filterset_fields = ['service', 'payment_option']

    @action(detail=True, methods=['post'], url_path='approve')
    def approve(self, request, pk=None):
        appointment = self.get_object()
        appointment.status = 'APPROVED'
        appointment.save()

        if not appointment.email:
            return Response({'message': 'Appointment approved, but no email provided.'}, status=status.HTTP_200_OK)

        appt_date = appointment.date.strftime('%Y-%m-%d %H:%M') if appointment.date else 'N/A'
        subject = 'Appointment Approved'
        message = (
            f"Dear {appointment.name},\n\n"
            f"Your appointment scheduled on {appt_date} has been approved.\n\n"
            "Thank you for choosing our service."
        )

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [appointment.email],
                fail_silently=False,
            )
            print("Email sent to:", appointment.email)
        except Exception as e:
            print("Email error:", e)
            return Response(
                {'message': 'Appointment approved, but failed to send email.', 'error': str(e)},
                status=status.HTTP_200_OK
            )

        return Response({'message': 'Appointment approved and email sent.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='reject')
    def reject(self, request, pk=None):
        appointment = self.get_object()
        appointment.status = 'REJECTED'
        appointment.save()
        return Response({'message': 'Appointment rejected.'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = super().get_queryset()
        category_filter = self.request.query_params.get('category')
        subcategory_filter = self.request.query_params.get('sub_category')
        service_filter = self.request.query_params.get('service')

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

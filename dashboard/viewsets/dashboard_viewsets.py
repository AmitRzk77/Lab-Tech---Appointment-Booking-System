from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from appointments.models import Appointments
from services.models import Service
from contact.models import Contact
from appointments.serializers.appointments_serializers import AppointmentListSerializers
from contact.serializers.contact_serializers import ContactListSerializers
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta


class dashboardViewSet(ViewSet):
    def list(self, request):
        total_appointments = Appointments.objects.count()
        total_services = Service.objects.count()
        total_inquiries = Contact.objects.count()

        # Revenue chart logic
        today = now()
        revenue_chart = []
        for i in range(5, -1, -1):
            month_start = (today.replace(day=1) - timedelta(days=30 * i)).replace(day=1)
            month_end = (month_start + timedelta(days=31)).replace(day=1)
            month_name = month_start.strftime('%B')
            amount = Appointments.objects.filter(
                date__gte=month_start,
                date__lt=month_end
            ).aggregate(Sum('amount'))['amount__sum'] or 0
            revenue_chart.append({'month': month_name, 'amount': amount})

        # Use existing serializers
        recent_bookings = Appointments.objects.order_by('-created_at')[:5]
        recent_inquiries = Contact.objects.order_by('-created_at')[:5]

        return Response({
            'total_appointments': total_appointments,
            'total_services': total_services,
            'total_inquiries': total_inquiries,
            'revenue_chart': revenue_chart,
            'recent_bookings': AppointmentListSerializers(recent_bookings, many=True).data,
            'recent_inquiries': ContactListSerializers(recent_inquiries, many=True).data,
        })

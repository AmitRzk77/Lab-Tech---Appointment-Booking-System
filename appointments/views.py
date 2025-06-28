from django.shortcuts import render, redirect
from .forms import AppointmentForm
from categories.models import Category
from services.models import Service
from .models import Appointments
from django.contrib import messages
import re


def booking_page(request):
    return render(request, 'appointment/appointment.html')


def add_appointment(request):
    categories = Category.objects.all()
    services = Service.objects.select_related('category').all()

    service_id = request.GET.get('service')
    try:
        preselected_service = int(service_id) if service_id else None
    except ValueError:
        preselected_service = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        date = request.POST.get('date')
        category_id = request.POST.get('category')
        service_id = request.POST.get('service')
        payment_option = request.POST.get('payment_option')
        amount = request.POST.get('amount')
        message = request.POST.get('message')

        # Validations
        if not re.match(r'^[\w\.-]+@gmail\.com$', email):
            messages.error(request, "Please enter a valid Gmail address.")
        elif not re.match(r'^(\+977\s*|)98\d{8}$', phone_number):
            messages.error(request, "Please enter a valid Nepali phone number starting with 98.")
        else:
            try:
                category = Category.objects.get(id=category_id)
                service = Service.objects.get(id=service_id)

                Appointments.objects.create(
                    name=name,
                    email=email,
                    phone_number=phone_number,
                    address=address,
                    gender=gender,
                    date=date,
                    category=category,
                    service=service,
                    payment_option=payment_option,
                    amount=amount,
                    message=message
                )

                messages.success(request, "Appointment submitted successfully. You will receive a mail about its status.")
                return redirect('add_user_appointment')  # Or redirect to confirmation page
            except Exception as e:
                messages.error(request, f"Error: {e}")

    if request.user.is_superuser:
        template_name = 'appointment/add_appointment.html'
    else:
        template_name = 'appointment/add_user_appointment.html'

    return render(request, template_name, {
        'categories': categories,
        'services': services,
        'preselected_service': preselected_service,
    })

from django.shortcuts import render




def booking_page(request):
    return render(request, 'appointment/appointment.html')  # Adjust path if needed

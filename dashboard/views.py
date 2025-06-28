from django.shortcuts import render

# Create your views here.
#def dashboard_page(request):
#      return render(request, 'dashboard/dashboard.html')
from django.shortcuts import render, redirect

def dashboard_page(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'dashboard/dashboard.html')  # Admin dashboard
    else:
        return render(request, 'home/home.html')  # Public homepage

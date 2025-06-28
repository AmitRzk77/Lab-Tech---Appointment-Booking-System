from django.urls import path
from .views import dashboard_page  # Import your view for the dashboard page

urlpatterns = [
    path('dashboard-page/', dashboard_page, name='dashboard'),
    path('', dashboard_page, name='home'),  # Route to the dashboard page
]

from django.urls import path, include
from .views import booking_page
from . import views

urlpatterns = [
     path('management/', views.booking_page, name='booking-management'),

    
]


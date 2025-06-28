from django.urls import path, include
from .views import booking_page
from . import views

urlpatterns = [
     path('management/', views.booking_page, name='booking-management'),
     path('add-appointment/', views.add_appointment, name='add_appointment'),
     path('add-user-appointment/', views.add_appointment, name='add_user_appointment'),

    
]


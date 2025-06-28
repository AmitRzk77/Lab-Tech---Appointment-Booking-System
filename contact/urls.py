from django.urls import path, include
from .views import contact_inquiry_list
from . import views

urlpatterns = [

path('contact/inquiries/', views.contact_inquiry_list, name='contact_inquiry_list'),


]

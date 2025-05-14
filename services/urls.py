from django.urls import path
from . import views

urlpatterns = [
    path('management/', views.service_page, name='service-management'),
    path('manage-groups/', views.manage_groups_view, name='manage_groups'),
    path('add-service/', views.add_service, name='add_service'),
    
]

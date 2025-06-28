from django.urls import path
from . import views
#from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/login/', views.admin_login, name='login'),
    path('admin/send-otp/', views.send_otp_page, name='admin-send-otp-page'),
    path('admin/verify-otp/', views.verify_otp_page, name='admin-verify-otp-page'),
    path('admin/set-password/', views.set_password_page, name='admin-set-password-page'),
    #path('admin/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('admin/logout/', views.admin_logout, name='logout'),
]

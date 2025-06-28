from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'adminlogin/login.html', {'error': 'Invalid credentials'})
    return render(request, 'adminlogin/login.html')
    

def send_otp_page(request):
    return render(request, 'adminlogin/send_otp.html')

def verify_otp_page(request):
    return render(request, 'adminlogin/verify_otp.html')

def set_password_page(request):
    return render(request, 'adminlogin/set_password.html')

def admin_logout(request):
    logout(request)
    return redirect('home')  # or any page you want

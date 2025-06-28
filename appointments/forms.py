from django import forms
from .models import Appointments

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = [
            'name', 'email', 'phone_number', 'address', 'gender', 'date',
            'category', 'service', 'payment_option', 'message', 'amount'
        ]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'gender': forms.RadioSelect(),
            'payment_option': forms.RadioSelect(),
        }

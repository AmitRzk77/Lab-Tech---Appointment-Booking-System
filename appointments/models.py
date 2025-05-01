from django.db import models
from services.models import Service
from categories.models import Category
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Appointments(models.Model):

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    PAYMENT_CHOICES = [('ONLINE PAYMENT', 'online payment'), ('PAYMENT AT CLINIC', 'payment at clinic')]

    name = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField()
    email = models.EmailField()
    phone_number = PhoneNumberField(region = None) 
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments_services')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name= 'select_category')
    sub_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='select_sub_category')  # <== ADDED
    message = models.TextField(blank=True)
    payment_option = models.CharField(max_length=100, choices= PAYMENT_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

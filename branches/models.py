from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = phone = PhoneNumberField(region = None)
    address = models.TextField()
    gps_coordinate = models.CharField(max_length=255)
    is_headquater = models.BooleanField(default=False)
    is_other = models.BooleanField(default=False)

    def __str__(self):
        return self.name
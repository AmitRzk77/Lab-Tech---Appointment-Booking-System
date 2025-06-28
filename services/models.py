from django.db import models
from categories.models import Category

# Create your models here.
from django.db import models




class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    featured_img = models.ImageField(upload_to='services/')
    other_img = models.ImageField(upload_to='services/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name= 'services_category')
    sub_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

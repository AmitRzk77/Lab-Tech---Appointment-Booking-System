from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null =True, blank=True, related_name='sub_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    
    def __str__(self):
        return self.category_name
    
    
    #class Meta:
    #    ordering = ['category']
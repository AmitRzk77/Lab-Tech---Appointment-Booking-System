from django.db import models

from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey

class Category(models.Model):
    category= models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_categories')

    parent = ChainedForeignKey(
        'self',
        chained_field="parent",  # field that filters
        chained_model_field="parent",  # model field that matches
        show_all=False,
        auto_choose=True,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='sub_categories'
    )

    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category
    
    def clean(self):
        if self.parent == self:
            raise ValidationError("A category cannot be its own child.")
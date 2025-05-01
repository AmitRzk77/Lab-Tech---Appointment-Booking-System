from django.contrib import admin
from .models import Category

# Register your models here.

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_name', 'category']
    
    # Filter the categories for subcategories so only parent categories (those with no parent) are shown
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(parent=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Category)
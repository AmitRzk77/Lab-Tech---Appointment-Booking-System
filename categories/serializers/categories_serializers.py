from rest_framework import serializers
from ..models import Category

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category',]

class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'category', 'parent', 'sub_categories']
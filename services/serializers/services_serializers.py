from rest_framework import serializers
from ..models import Service
from categories.models import Category

# Nested Category serializer
class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

# LIST - Nested category and sub-category
class ServiceListSerializers(serializers.ModelSerializer):
    category = CategorySimpleSerializer(read_only=True)
    sub_category = CategorySimpleSerializer(read_only=True)

    class Meta:
        model = Service
        fields = '__all__'

# RETRIEVE - Nested category and sub-category
class ServiceRetriveSerializers(serializers.ModelSerializer):
    category = CategorySimpleSerializer(read_only=True)
    sub_category = CategorySimpleSerializer(read_only=True)

    class Meta:
        model = Service
        fields = '__all__'

# WRITE - Simple ID fields for category and sub-category
class ServiceWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

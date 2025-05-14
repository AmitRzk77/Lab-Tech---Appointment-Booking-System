from rest_framework import serializers
from ..models import Service
from categories.models import Category

# Nested Category serializer
class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']

    

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

    #def validate(self, attrs):
     #   category = attrs.get('category')
     #   sub_category = attrs.get('sub_category')

     #   if sub_category and sub_category.parent_id != category.id:
    #        raise serializers.ValidationError({
    #            "sub_category": "Selected sub-category does not belong to the selected category."
     #       })

     #   return attrs

    

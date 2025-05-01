from rest_framework import serializers
from ..models import Category



class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['category_name', 'parent', 'subcategories']


    def get_subcategories(self, obj):
        # Limit the depth of serialization
        if self.context.get('depth', 0) < 2:  # Change 2 to your desired depth
            subcategories = obj.sub_categories.all()
            return CategorySerializer(subcategories, many=True, context={'depth': self.context.get('depth', 0) + 1}).data
        return []

    

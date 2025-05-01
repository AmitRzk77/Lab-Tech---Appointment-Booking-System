from rest_framework import serializers
from ..models import Appointments
from services.models import Service
from categories.models import Category

# For nested service and category
class ServiceNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [ 'name', 'price' ,'category']  # You can add more if needed

class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'category_name', 'parent']

class AppointmentListSerializers(serializers.ModelSerializer):
    service = ServiceNestedSerializer(read_only=True)
    category = CategoryNestedSerializer(read_only=True)
    sub_category = CategoryNestedSerializer(read_only=True)

    class Meta:
        model = Appointments
        fields = '__all__'

class AppointmentsRetriveSerializers(serializers.ModelSerializer):
    service = ServiceNestedSerializer(read_only=True)
    category = CategoryNestedSerializer(read_only=True)
    sub_category = CategoryNestedSerializer(read_only=True)

    class Meta:
        model = Appointments
        fields = '__all__'

class AppointmentsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'

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
        fields = [ 'category', 'parent']

#class AppointmentListSerializers(serializers.ModelSerializer):
    #service = ServiceNestedSerializer(read_only=True)
    #category = CategoryNestedSerializer(read_only=True)
    #sub_category = CategoryNestedSerializer(read_only=True)
class AppointmentListSerializers(serializers.ModelSerializer):
    service_id = serializers.IntegerField(source='service.id', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    category_name = serializers.CharField(source='category.category', read_only=True)


    class Meta:
        model = Appointments
        fields = [
            'id', 'name', 'date', 'email', 'phone_number', 'address', 'gender',
            'service_id', 'service_name', 'category_id', 'category_name',
            'message', 'payment_option', 'amount', 'created_at', 'updated_at', 'status'
        ]
    
    

    



    

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

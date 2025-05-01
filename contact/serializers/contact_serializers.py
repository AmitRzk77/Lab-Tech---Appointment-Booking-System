from rest_framework import serializers

from ..models import Contact

class ContactListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactRetriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ConatctWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
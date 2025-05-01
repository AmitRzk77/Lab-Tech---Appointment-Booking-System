from rest_framework import serializers

from ..models import Branch

class BranchListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class BranchRetriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class BranchWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
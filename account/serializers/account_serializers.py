from rest_framework import serializers
from django.contrib.auth.models import User

class AdminSendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value, is_staff=True).exists():
            raise serializers.ValidationError("No admin found with this email.")
        return value


class AdminVerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp')
        if not User.objects.filter(email=email, is_staff=True).exists():
            raise serializers.ValidationError("Invalid email or OTP.")
        return data


class AdminSetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True, min_length=8)

    def validate_email(self, value):
        if not User.objects.filter(email=value, is_staff=True).exists():
            raise serializers.ValidationError("No admin found with this email.")
        return value

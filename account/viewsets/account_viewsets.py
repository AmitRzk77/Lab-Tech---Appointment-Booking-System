from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random

from ..models import AdminPasswordResetOTP
from ..serializers.account_serializers import (
    AdminSendOTPSerializer,
    AdminVerifyOTPSerializer,
    AdminSetNewPasswordSerializer,
)


class adminPasswordResetViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'], url_path='send-otp')
    def send_otp(self, request):
        serializer = AdminSendOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email, is_staff=True)
            except User.DoesNotExist:
                return Response({"error": "Admin with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

            otp = str(random.randint(100000, 999999))
            AdminPasswordResetOTP.objects.create(user=user, otp=otp)

            send_mail(
                'Admin Password Reset OTP',
                f'Your OTP is: {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({"message": "OTP sent to admin email."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='verify-otp')
    def verify_otp(self, request):
        serializer = AdminVerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            try:
                user = User.objects.get(email=email, is_staff=True)
                otp_record = AdminPasswordResetOTP.objects.filter(
                    user=user, otp=otp, is_used=False
                ).latest('created_at')

                # Mark OTP as used
                otp_record.is_used = True
                otp_record.save()

                return Response({"message": "OTP verified. You can now reset your password."})
            except (User.DoesNotExist, AdminPasswordResetOTP.DoesNotExist):
                return Response({"error": "Invalid OTP or email."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='set-password')
    def set_new_password(self, request):
        serializer = AdminSetNewPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']
            try:
                user = User.objects.get(email=email, is_staff=True)
                
                # Check if there's a used OTP for this user
                otp_verified = AdminPasswordResetOTP.objects.filter(user=user, is_used=True).latest('created_at')

                user.set_password(new_password)
                user.save()

                return Response({"message": "Password has been reset successfully."})
            except (User.DoesNotExist, AdminPasswordResetOTP.DoesNotExist):
                return Response({"error": "OTP not verified or invalid email."}, status=status.HTTP_400_BAD_REQUEST)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Endpoints
#/api/account/send-otp/ → sends OTP

#/api/account/verify-otp/ → verifies OTP

#/api/account/set-password/ → sets password
#use this endpoints to reset passwords
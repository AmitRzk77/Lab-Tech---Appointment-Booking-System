from django.db import models

# Create your models here.
# dashboard/models.py or users/models.py

from django.db import models
from django.contrib.auth.models import User

class AdminPasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - OTP"

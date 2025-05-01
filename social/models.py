from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='social_logos/')
    link = models.URLField()

    def __str__(self):
        return self.title
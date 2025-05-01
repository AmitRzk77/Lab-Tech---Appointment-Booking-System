from django.db import models
import os

# Create your models here.
class Banner(models.Model):
    img = models.ImageField(upload_to='banners/images/', blank=True, null=True)
    img_link = models.URLField(blank=True, null=True)
    video = models.FileField(upload_to='banners/videos/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Banner {self.id}"
    

    def delete(self, *args, **kwargs):
        # Delete files if they exist and path is valid
        if self.img and hasattr(self.img, 'path') and os.path.isfile(self.img.path):
            os.remove(self.img.path)
 
        if self.video and hasattr(self.video, 'path') and os.path.isfile(self.video.path):
            os.remove(self.video.path)
 
        super().delete(*args, **kwargs)

class PopUp(models.Model):
    title = models.CharField(max_length=255)
    imgs = models.ImageField(upload_to='popups/')
    links = models.URLField()

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=255)

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')

    




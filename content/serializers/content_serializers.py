from rest_framework import serializers
from ..models import Banner, Gallery, PopUp, Team ,GalleryImage
import os

# ----------------------
# Banner Serializers
# ----------------------
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

    def validate(self, data):
        if (data.get('img') and data.get('video')) or (not data.get('img') and not data.get('video')):
            raise serializers.ValidationError('You must provide either an image or a video, but not both.')
        return data
   
 
    def delete(self, *args, **kwargs):
        if self.img and os.path.isfile(self.img.path):
            os.remove(self.img.path)
 
        if self.video and os.path.isfile(self.video.path):
            os.remove(self.video.path)
 
        super().delete(*args, **kwargs)

    
    
   
    



# ----------------------
# Gallery Serializers
# ----------------------
# serializers.py
class GalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # returns full image URL

    class Meta:
        model = GalleryImage
        fields = ['id', 'image']


class GallerySerializer(serializers.ModelSerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    images = GalleryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'uploaded_images', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images', [])
        gallery = Gallery.objects.create(**validated_data)
        for image in images_data:
            GalleryImage.objects.create(gallery=gallery, image=image)
        return gallery





# class GallerySerializer(serializers.ModelSerializer):
#     images = serializers.ListField(child=serializers.ImageField(), write_only=True)
#     uploaded_images = GalleryImageSerializer(source='images', many=True, read_only=True)

#     class Meta:
#         model = Gallery
#         fields = ['id', 'title', 'images', 'uploaded_images']

#     def create(self, validated_data):
#         images_data = validated_data.pop('images')
#         gallery = Gallery.objects.create(**validated_data)
#         for image in images_data:
#             GalleryImage.objects.create(gallery=gallery, image=image)
#         return gallery



# ----------------------
# PopUp Serializers
# ----------------------
class PopUpListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = '__all__'

class PopUpRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = '__all__'

class PopUpWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = '__all__'

# ----------------------
# Team Serializers
# ----------------------
class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

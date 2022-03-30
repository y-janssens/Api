from rest_framework import serializers
from django.contrib.auth.models import User
from videos.models import Video, Category

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        depth = 1

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
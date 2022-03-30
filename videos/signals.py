from django.contrib.auth.models import User
from .models import Video
from api.serializers import VideosSerializer

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings

def deleteVideo(sender, instance, **kwargs):
    video = instance
    file = video.file
    thumbnail = video.thumbnail
    try:
        file.delete()
        thumbnail.delete()
        #video.delete()
    except:
        pass

post_delete.connect(deleteVideo, sender=Video)
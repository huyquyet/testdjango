from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Album(models.Model):
    name_album = models.TextField()
    description_album = models.TextField()
    link_thumbnail_album = models.TextField()
    date_time_create = models.DateTimeField(default=timezone.now)
    date_time_update = models.DateTimeField(default=timezone.now)
    user_create_album = models.ForeignKey(User, related_name='album')
    user_like_album = models.ManyToManyField(User, related_name='liked_albums')

    def __unicode__(self):
        return self.name_album

    class Meta:
        ordering = ["-date_time_create"]


class Images(models.Model):
    pic = models.ImageField(upload_to='images/', default='images/no-img.jpg')
    upload_date = models.DateTimeField(default=timezone.now)
    album = models.ForeignKey(Album)
    name_picture = models.TextField()
    #    link_picture = models.TextField()
    description_picture = models.TextField()
    user_like_pic = models.ManyToManyField(User, related_name='user_like_p')
    user_comment_pic = models.ManyToManyField(User, related_name='user_comment_p')

    def __unicode__(self):
        return self.name_picture


class Comment(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField()
    user_cmt = models.ForeignKey(User, related_name='user_comment')
    picture = models.ForeignKey(Images, related_name='id_pic')

    def __unicode__(self):
        return self.content

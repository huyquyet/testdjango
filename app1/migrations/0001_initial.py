# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_album', models.TextField()),
                ('description_album', models.TextField()),
                ('link_thumbnail_album', models.TextField()),
                ('user_creat_album', models.ForeignKey(related_name='user_creat', to=settings.AUTH_USER_MODEL)),
                ('user_like_album', models.ManyToManyField(related_name='user_like_a', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_picture', models.TextField()),
                ('link_picture', models.TextField()),
                ('description_picture', models.TextField()),
                ('album', models.ForeignKey(to='app1.Album')),
                ('user_comment_pic', models.ManyToManyField(related_name='user_comment_p', to=settings.AUTH_USER_MODEL)),
                ('user_like_pic', models.ManyToManyField(related_name='user_like_p', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='picture',
            field=models.ForeignKey(related_name='id_pic', to='app1.Images'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_cmt',
            field=models.ForeignKey(related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]

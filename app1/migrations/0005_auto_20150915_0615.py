# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20150915_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_time_creat',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 6, 15, 3, 703237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_time_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 6, 15, 3, 703264, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='album',
            name='user_creat_album',
            field=models.ForeignKey(related_name='album', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='album',
            name='user_like_album',
            field=models.ManyToManyField(related_name='liked_albums', to=settings.AUTH_USER_MODEL),
        ),
    ]

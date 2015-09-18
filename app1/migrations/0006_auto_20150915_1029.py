# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20150915_0615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-date_time_create']},
        ),
        migrations.RenameField(
            model_name='album',
            old_name='user_creat_album',
            new_name='user_create_album',
        ),
        migrations.RemoveField(
            model_name='album',
            name='date_time_creat',
        ),
        migrations.RemoveField(
            model_name='images',
            name='link_picture',
        ),
        migrations.AddField(
            model_name='album',
            name='date_time_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='images',
            name='pic',
            field=models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'images/'),
        ),
        migrations.AddField(
            model_name='images',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_time_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

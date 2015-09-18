# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20150914_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_time_creat',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 4, 18, 49, 645401, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_time_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 4, 18, 49, 645424, tzinfo=utc)),
        ),
    ]

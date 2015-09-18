# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-date_time_creat']},
        ),
        migrations.AddField(
            model_name='album',
            name='date_time_creat',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 14, 8, 14, 40, 475377, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='album',
            name='date_time_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 14, 8, 14, 40, 475400, tzinfo=utc)),
        ),
    ]

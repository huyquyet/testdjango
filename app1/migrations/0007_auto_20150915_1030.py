# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20150915_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='pic',
            field=models.ImageField(default=b'images/no-img.jpg', upload_to=b'images/'),
        ),
    ]

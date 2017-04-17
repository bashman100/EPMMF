# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-17 15:46
from __future__ import unicode_literals

import bands.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0002_auto_20170412_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=bands.models.get_image_path),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=bands.models.get_image_path),
        ),
    ]

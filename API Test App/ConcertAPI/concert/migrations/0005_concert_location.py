# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0004_remove_concert_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='location',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
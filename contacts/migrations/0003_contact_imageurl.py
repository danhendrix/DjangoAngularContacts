# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20170605_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='imageUrl',
            field=models.CharField(default='https://i.ytimg.com/vi/GF60Iuh643I/hqdefault.jpg', max_length=100),
        ),
    ]

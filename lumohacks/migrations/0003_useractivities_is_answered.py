# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumohacks', '0002_auto_20170917_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivities',
            name='is_answered',
            field=models.BooleanField(default=False),
        ),
    ]

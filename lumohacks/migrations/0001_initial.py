# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 01:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_a', to=settings.AUTH_USER_MODEL)),
                ('user_b', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_b', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('exp', models.IntegerField()),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lumohacks.Connection')),
            ],
        ),
        migrations.CreateModel(
            name='PetUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField()),
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lumohacks.Activity')),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthyFood', '0002_auto_20170805_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionClinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=5)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('disease', models.CharField(max_length=20)),
                ('physical', models.CharField(max_length=50)),
            ],
        ),
    ]

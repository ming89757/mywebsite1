# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-12-19 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20201219_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

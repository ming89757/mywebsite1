# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-12-19 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0003_auto_20201216_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, to='mystore.Author'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-12-16 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0002_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='mystore.Author'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-20 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата загрузки'),
        ),
    ]

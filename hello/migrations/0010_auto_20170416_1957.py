# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-16 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20170416_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='excercise',
            name='lever',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='excercise',
            name='mass_share',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]

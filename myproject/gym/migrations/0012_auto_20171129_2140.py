# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0011_auto_20171129_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='excercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.Excercise'),
        ),
        migrations.AlterField(
            model_name='set',
            name='workout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='gym.Workout'),
        ),
    ]

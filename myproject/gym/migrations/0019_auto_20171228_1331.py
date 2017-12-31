# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0018_auto_20171226_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='comments',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='excercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.Excercise'),
        ),
    ]
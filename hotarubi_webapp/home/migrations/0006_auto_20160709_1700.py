# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-09 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160708_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guildevent',
            options={'verbose_name': 'Threadsssss', 'verbose_name_plural': 'My sddddddfes'},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'verbose_name': 'Threadsssss', 'verbose_name_plural': 'My sddddddfes'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]

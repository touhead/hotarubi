# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20160709_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.AddField(
            model_name='thread',
            name='banner',
            field=models.ImageField(blank=True, upload_to='home/threads', verbose_name='バナ－の画像(任意)'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='home/threads', verbose_name='イベントの画像'),
        ),
    ]

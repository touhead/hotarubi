# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160612_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='home/events', verbose_name='news image'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_news'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='New',
        ),
    ]

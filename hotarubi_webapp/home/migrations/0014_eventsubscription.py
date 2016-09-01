# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-01 14:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0013_auto_20160713_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guild_event_event_subscription', to='home.GuildEvent', verbose_name='イベント')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_event_subscription', to=settings.AUTH_USER_MODEL, verbose_name='ユ－ザ')),
            ],
            options={
                'verbose_name_plural': 'イベント登録',
                'verbose_name': 'イベント登録',
            },
        ),
    ]

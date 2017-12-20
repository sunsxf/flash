# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-20 00:22
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market_manage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='contactor',
        ),
        migrations.AddField(
            model_name='market',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='market',
            name='contact',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8054\u7cfb\u4eba'),
            preserve_default=False,
        ),
    ]

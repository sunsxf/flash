# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-19 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u7248\u672c\u540d\u79f0')),
                ('version_id', models.CharField(max_length=50, verbose_name='\u7248\u672c\u53f7')),
            ],
            options={
                'verbose_name': '\u7248\u672c\u7ba1\u7406',
                'verbose_name_plural': '\u7248\u672c\u7ba1\u7406',
            },
        ),
    ]

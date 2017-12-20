# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-20 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package_manage', '0001_initial'),
        ('flash_config', '0002_auto_20171220_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashconfig',
            name='package',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='package_manage.PackageManage', verbose_name='\u5305\u540d'),
        ),
    ]

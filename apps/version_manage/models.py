# encoding=utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

class Version(models.Model):
    name = models.CharField(max_length=50, verbose_name='版本名称')
    version_code = models.CharField(max_length=50, verbose_name='版本号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    class Meta:
        verbose_name = '版本管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.version_code

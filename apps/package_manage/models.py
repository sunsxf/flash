# encoding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class PackageManage(models.Model):
    name = models.CharField(max_length=20, verbose_name='包名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        verbose_name = '包管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

# encoding=utf-8
from __future__ import unicode_literals

from django.db import models
from image_manage.models import UserProfile
from datetime import datetime


# Create your models here.

class Market(models.Model):
    name = models.CharField(max_length=50, verbose_name='渠道名称')
    category = models.CharField(max_length=50, verbose_name='类别')
    contact = models.CharField(max_length=50, verbose_name='联系人')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '渠道管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
# encoding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models


# Create your models here.

# class Flash(models.Model):
#     market = models.ForeignKey(MARKET, verbose_name='渠道')
#     version = models.ForeignKey(VERSION, verbose_name='版本')
#     user = models.ForeignKey(User, verbose_name='发布者')
#     pub_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
#     status = models.CharField(max_length=10, choices=(('offline','下线'),('online','上线')), default='offline')
#
#     class Meta:
#         verbose_name = '闪屏配置管理'
#         verbose_name_plural = verbose_name
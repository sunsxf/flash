# encoding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class Image(models.Model):
    image_desc = models.CharField(max_length=5, verbose_name='图片描述', default='')
    image = models.ImageField(max_length=100, upload_to='image_manage/%Y/%m', verbose_name='图片管理', )
    jump_url = models.CharField(max_length=100, verbose_name='闪屏跳转url', default='')
    upload_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')
    class Meta:
        verbose_name = '图片管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.image_desc


class UserProfile(AbstractUser):
    # 扩展系统User表
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.nick_name
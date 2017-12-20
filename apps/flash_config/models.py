# encoding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

from market_manage.models import Market
from version_manage.models import Version
from image_manage.models import Image
from package_manage.models import PackageManage


# Create your models here.

class FlashConfig(models.Model):
    market = models.ForeignKey(Market, verbose_name='渠道')
    version = models.ForeignKey(Version, verbose_name='版本')
    image = models.ForeignKey(Image, verbose_name='图片')
    package = models.ForeignKey(PackageManage, verbose_name='包名')
    pub = models.CharField(max_length=20, verbose_name='发布者')
    status = models.CharField(max_length=10, choices=(('offline', '下线'), ('online', '上线')), default='offline')
    pub_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        verbose_name = '闪屏配置管理'
        verbose_name_plural = verbose_name

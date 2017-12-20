# encoding=utf-8

import xadmin
from xadmin import views
from .models import FlashConfig
import redis
from random import Random
from image_manage.models import Image


class FlashConfigAdmin(object):
    list_display = ['market', 'version', 'image', 'package', 'pub', 'status', 'pub_time']
    search_fields = ['market', 'version', 'image', 'package', 'pub', 'status']
    list_filter = ['market__name', 'version', 'image', 'package', 'pub', 'status', 'pub_time']
    list_editable = ['status']

    def save_models(self):
        obj = self.new_obj
        pkg = obj.package.name
        mk = obj.market.name
        ver = obj.version.version_code
        _image = '127.0.0.1:8000/media/' + obj.image.image.name
        url = obj.image.jump_url
        du = 3
        skip = 'off'
        conn = redis.StrictRedis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
        _key = "%s:%s:%s" % (pkg, ver, mk)
        _hs = self.gen_random_str()
        conn.hmset(_key, {"md5": _hs, "json": {"image": _image, 'url':url, 'du': du, 'skip':skip}})
        obj.save()

    def gen_random_str(self, randomlength=16):
        str_ = ''
        chars_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        length = len(chars_) - 1
        random_ = Random()
        for i in range(randomlength):
            str_ += chars_[random_.randint(0, length)]
        return str_


xadmin.site.register(FlashConfig, FlashConfigAdmin)

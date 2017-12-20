# encoding=utf-8
import xadmin
from .models import Image


class ImageAdmin(object):
    list_display = ['image_desc', 'image', 'jump_url', 'upload_time']
    search_fields = ['image_desc', 'image', 'jump_url']
    list_filter = ['image_desc', 'image', 'jump_url', 'upload_time']

    def save_models(self):
        img = self.new_obj
        img.save()


xadmin.site.register(Image, ImageAdmin)

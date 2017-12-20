# encoding=utf-8
import xadmin
from .models import Version
from xadmin import views


class VersionAdmin(object):
    list_display = ['name', 'version_code', 'add_time']
    search_fields = ['name', 'version_code']
    list_filter = ['name', 'version_code', 'add_time']


class GlobalSettings(object):
    site_title = '闪屏后台管理系统'
    site_footer = '元智在线网'
    # menu_style = 'accordion'


xadmin.site.register(Version, VersionAdmin)

xadmin.site.register(views.CommAdminView, GlobalSettings)

import xadmin
from xadmin import views
from .models import PackageManage


class PackageManageAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


xadmin.site.register(PackageManage, PackageManageAdmin)
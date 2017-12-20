# encoding=utf-8

import xadmin
from .models import Market


class MarketAdmin(object):
    list_display = ['name', 'category', 'contact', 'add_time']
    search_fields = ['name', 'category', 'contact__username']
    list_filter = ['name', 'category', 'contact', 'add_time']


xadmin.site.register(Market, MarketAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import User, Search

class SearchAdmin(admin.ModelAdmin):
    search_fields = ['request', 'response']

admin.site.register(User)
admin.site.register(Search, SearchAdmin)

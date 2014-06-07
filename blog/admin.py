__author__ = 'Root'

from django.contrib import admin
from models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'label', 'id', 'display')
    search_fields = ('label', )
    fields = ('title', 'blog', 'pic', 'display', 'label', 'date')
    list_filter = ('title', )
    date_hierarchy = 'date'
    ordering = ('-id',)

admin.site.register(Blog, BlogAdmin)

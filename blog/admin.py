__author__ = 'Root'

from django.contrib import admin
from models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'label', 'id')
    search_fields = ('label', )
    fields = ('title', 'blog', 'pic', 'label', 'date')
    list_filter = ('title', )
    date_hierarchy = 'date'
    ordering = ('date',)

admin.site.register(Blog, BlogAdmin)

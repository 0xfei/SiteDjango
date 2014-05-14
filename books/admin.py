__author__ = '0x01f'

from django.contrib import admin
from models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'id')
    search_fields = ('title', )
    fields = ('title', 'author', 'type')
    list_filter = ('title', )
    ordering = ('-id',)

admin.site.register(Books, BooksAdmin)

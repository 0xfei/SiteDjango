__author__ = 'Root'

from django.contrib import admin
from models import Words


class WordsAdmin(admin.ModelAdmin):
    list_display = ('label', 'date', )
    search_fields = ('label', 'date')
    list_filter = ('label', )
    date_hierarchy = 'date'
    ordering = ('-date', )

admin.site.register(Words, WordsAdmin)

__author__ = 'Root'

from django.contrib import admin
from models import Movies


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'search')
    search_fields = ('name', )
    list_filter = ('name', )

admin.site.register(Movies, MovieAdmin)

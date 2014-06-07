__author__ = '0x01f'

from django.shortcuts import render_to_response
from models import Books
from blog.models import Blog
from blog.views import all_label


def books(request):
    recents = Blog.objects.order_by('-id')[:8]
    w = Books.objects.all()
    return render_to_response('books.html', {'books': w, 'labels': all_label(),
                                             'recents': recents})
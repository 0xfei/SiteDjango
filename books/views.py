__author__ = '0x01f'

from django.shortcuts import render_to_response
from models import Books


def books(request):
    w = Books.objects.all()
    return render_to_response('books.html', {'books': w})

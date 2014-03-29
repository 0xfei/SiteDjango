__author__ = 'Root'

from django.http import Http404
from django.shortcuts import render_to_response
from models import Blog


def blog(request):
    page = Blog.objects.all()
    return render_to_response('blog.html', {'blogs': page})


def see(request, number):
    try:
        number = int(number)
    except TypeError:
        raise Http404
    page = Blog.objects.get(id=number)
    if not page:
        raise Http404
    return render_to_response('see.html', {'page': page})

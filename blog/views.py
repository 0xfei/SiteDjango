__author__ = 'Root'

from django.shortcuts import render_to_response
from models import Blog


def blog(request):
    page = Blog.objects.all()
    return render_to_response('blog.html', {'blogs': page})

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


def all_label(request):
    labels = Blog.objects.order_by('label')
    prev = ''
    page = []
    for i in labels:
        if i.label == prev:
            continue
        else:
            page.append(i.label)
            prev = i.label
    if not page:
        raise Http404
    return render_to_response('label.html', {'labels': page})


def deal_label(request, label_name):
    blogs = Blog.objects.filter(label__contains=label_name)
    if not blogs:
        raise Http404
    return render_to_response('blog.html', {'blogs': blogs})

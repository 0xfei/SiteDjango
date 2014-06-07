__author__ = 'Root'

from django.http import Http404
from django.shortcuts import render_to_response
from models import Blog


def blog(request):
    page = Blog.objects.order_by('id')
    recents = Blog.objects.order_by('-id')[:8]
    limit = len(Blog.objects.all())
    if limit % 5 == 0:
        page_max = limit/5
    else:
        page_max = limit/5+1
    return render_to_response('blog.html', {'blogs': page,
                                            'labels': all_label(),
                                            'recents': recents,
                                            'page_max': page_max,
                                            'page_now': 1,
                                            'page_next': 2,
                                            'page_prev': 0,
                                            'range': range(1, page_max+1)})


def see(request, number):
    try:
        number = int(number)
    except TypeError:
        raise Http404
    page = Blog.objects.get(id=number)
    limit = len(Blog.objects.all())
    if not page:
        raise Http404
    if number < limit:
        n = number+1
    else:
        n = 0
    if number > 1:
        p = number-1
    else:
        p = 0
    recents = Blog.objects.order_by('-id')[:8]
    return render_to_response('see.html', {'page': page,
                                           'prev': p,
                                           'next': n,
                                           'labels': all_label(),
                                           'recents': recents})


def all_label():
    labels = Blog.objects.order_by('label')
    prev = ''
    page = []
    for i in labels:
        if i.label == prev:
            continue
        else:
            page.append(i.label)
            prev = i.label
    return page


def deal_label(request, label_name):
    blogs = Blog.objects.filter(label__contains=label_name)
    if not blogs:
        raise Http404
    recents = Blog.objects.order_by('-id')[:8]
    limit = len(Blog.objects.all())
    if limit % 5 == 0:
        page_max = limit/5
    else:
        page_max = limit/5+1
    return render_to_response('blog.html', {'blogs': blogs, 'labels': all_label(),
                                            'recents': recents, 'page_max': page_max,
                                            'page_now': 1,
                                            'page_next': 2,
                                            'page_prev': 0,
                                            'range': range(1, page_max+1)})

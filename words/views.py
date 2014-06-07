__author__ = 'Root'

from django.shortcuts import render_to_response
from django.http import Http404
from models import Words
from blog.models import Blog
from blog.views import all_label


def words(request):
    w = Words.objects.all()
    recents = Blog.objects.order_by('-id')[:8]
    return render_to_response('words.html', {'words': w, 'labels': all_label(),
                                             'recents': recents})

def see_words(request, number):
    try:
        number = int(number)
    except TypeError:
        raise Http404
    page = Words.objects.get(id=number)
    if not page:
        raise Http404
    recents = Blog.objects.order_by('-id')[:8]
    return render_to_response('see_words.html', {'page': page, 'labels': all_label(),
                                                 'recents': recents})

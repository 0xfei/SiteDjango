__author__ = 'Root'

from django.shortcuts import render_to_response
from django.http import Http404
from models import Words


def words(request):
    w = Words.objects.all()
    return render_to_response('words.html', {'words': w})


def see_words(request, number):
    try:
        number = int(number)
    except TypeError:
        raise Http404
    page = Words.objects.get(id=number)
    if not page:
        raise Http404
    return render_to_response('see_words.html', {'page': page})

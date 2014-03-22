__author__ = 'Root'

from django.shortcuts import render_to_response
from models import Words


def words(request):
    w = Words.objects.all()
    return render_to_response('words.html', {'words': w})

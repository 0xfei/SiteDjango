__author__ = 'Root'

from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Movies


def us_tvs(request):
    tvs = Movies.objects.all()
    return render_to_response('us_tvs.html', {'tvs': tvs})

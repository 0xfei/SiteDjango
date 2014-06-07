__author__ = 'Root'

from django.shortcuts import render_to_response
from blog.models import Blog
from blog.views import all_label
from models import Movies


def us_tvs(request):
    recents = Blog.objects.order_by('-id')[:8]
    tvs = Movies.objects.all()
    return render_to_response('us_tvs.html', {'tvs': tvs,
                                              'labels': all_label(), 'recents': recents})

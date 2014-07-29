from django.shortcuts import render_to_response
from django.http import Http404
from blog.models import Blog
from blog.views import all_label


def page(request, number):
    try:
        number = int(number)
    except TypeError:
        raise Http404
    limit = len(Blog.objects.all())
    if limit % 5 == 0:
        page_max = limit/5
    else:
        page_max = limit/5+1
    if number > page_max:
        raise Http404
    high = limit - (number-1)*5
    low = high - 5
    if low < 0:
        low = 0
    blogs = Blog.objects.order_by('-id').filter(id__gt=low).filter(id__lte=high)
    if not blogs:
        raise Http404
    recents = Blog.objects.order_by('-id')[:8]
    if number - 1 > 0:
        pp = number - 1
    else:
        pp = 0
    if number + 1 <= page_max:
        pn = number + 1
    else:
        pn = 0
    page_now = number
    return render_to_response('blog.html', {'blogs': blogs,
                                            'labels': all_label(),
                                            'recents': recents,
                                            'page_max': page_max,
                                            'page_now': page_now,
                                            'page_prev': pp,
                                            'page_next': pn,
                                            'range': range(1, page_max+1)})


def home(request):
    return page(request, 1)


def contact(request):
    recents = Blog.objects.order_by('-id')[:8]
    return render_to_response('contact.html', {'labels': all_label(), 'recents': recents})


def google(request):
    return render_to_response('google.html')


def baidu(request):
    return render_to_response('baidu.html')

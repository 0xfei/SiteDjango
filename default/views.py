from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponse, Http404, HttpResponseRedirect
from forms import ContactForm
import datetime
from blog.models import Blog


def home(request):
    page = Blog.objects.all()
    return render_to_response('home.html', {'blogs':page})


def contact(request):
    return render_to_response('contact.html')


def google(request):
    return render_to_response('google.html')


def baidu(request):
    return render_to_response('baidu.html')


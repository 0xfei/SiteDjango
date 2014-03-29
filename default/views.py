from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.core.servers.basehttp import FileWrapper
from mysite.settings import STATIC_ROOT
import os
from blog.models import Blog
import tempfile
import zipfile



def home(request):
    page = Blog.objects.all()
    return render_to_response('home.html', {'blogs':page})


def contact(request):
    return render_to_response('contact.html')


def google(request):
    return render_to_response('google.html')


def send_android(request):
    filename = os.path.join(STATIC_ROOT, r'0x01f.apk')
    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    archive.write(filename, r'0x01f.apk')
    archive.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=android.zip'
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response


def baidu(request):
    return render_to_response('baidu.html')

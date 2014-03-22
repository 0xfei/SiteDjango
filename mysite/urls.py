from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import blog
from ustvs.views import us_tvs
from words.views import words
from default.views import home, contact, see, google



admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', home),
    url(r'^zhi9ebushihoutai/', include(admin.site.urls)),
    url(r'^blog/$', blog),
    url(r'^us_tvs/$', us_tvs),
    url(r'^words/$', words),
    url(r'^contact/$', contact),
    url(r'^blog/(\d{1,4})', see),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^google.*$', google),
)

urlpatterns += patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
)


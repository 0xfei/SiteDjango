__author__ = 'Root'
#coding=utf-8

from django.db import models
from mysite.settings import MEDIA_ROOT


class Movies(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'剧名')
    picture = models.ImageField(upload_to='static/image', verbose_name=u'海报剧照')
    search = models.URLField(max_length=255, verbose_name=u'搜索美剧')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = u'追剧'
        verbose_name_plural = u'追剧'

__author__ = 'Root'
#coding=utf-8

from django.db import models
from tinymce.models import HTMLField


class Blog(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'题目')
    label = models.CharField(max_length=128, verbose_name=u'标签')
    date = models.DateField(auto_created=True, verbose_name=u'日期')
    blog = HTMLField(max_length=65536, verbose_name=u'正文')

    def __unicode__(self):
        return r'title: %s label: %s date: %s' % (self.title, self.label, self.date)

    class Meta:
        verbose_name = u'博客管理'
        verbose_name_plural = u'博客管理'

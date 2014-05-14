__author__ = '0x01f'
#coding=utf-8

from django.db import models


class Books(models.Model):
    title = models.TextField(max_length=1024, verbose_name=u'书名')
    author = models.TextField(max_length=1024, verbose_name=u'作者')
    type = models.TextField(max_length=1024, verbose_name=u'类型')

    def __unicode__(self):
        return r'title: %s author: %s ' % (self.title, self.author)

    class Meta:
        verbose_name = u'书籍管理'
        verbose_name_plural = u'书籍管理'
        ordering = ['-id']

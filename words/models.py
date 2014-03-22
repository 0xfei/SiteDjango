__author__ = 'Root'
#coding=utf-8

from django.db import models


class Words(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name=u'记录日期')
    label = models.CharField(max_length=20, verbose_name=u'标签')
    message = models.TextField(max_length=1024, verbose_name=u'碎言碎语')

    def __unicode__(self):
        return str(self.date) + ':' + self.label

    class Meta:
        verbose_name = u'碎言碎语'
        verbose_name_plural = u'碎言碎语'
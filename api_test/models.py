from __future__ import unicode_literals  # 有什么用？
from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now=True, auto_created=True)
    is_delete = models.IntegerField(default=0)

    def __unicode__(self):
        """
        转码？？？
        :return:
        """
        return self.book_name


class User(models.Model):
    userid = models.CharField(max_length=20)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=48, null=False, default='a123456')
    register_time = models.DateTimeField(auto_created=True,auto_now_add=True)
    is_cancel = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username




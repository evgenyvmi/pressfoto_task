# -- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import time
import datetime


class Image(models.Model):
	image = models.ImageField(verbose_name=u'Изображение')
	name = models.CharField(verbose_name=u'Название', max_length=50)
	description = models.TextField(verbose_name=u'Описание')
	date = models.DateField(verbose_name=u'Дата загрузки', default=timezone.now)
	def __unicode__(self):
		return self.name + self.description
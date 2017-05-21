#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^search/$', views.search, name='search'),
    url(r'^new_image/$', views.new_image, name='new image'),
    url(r'^images/$', views.images, name='images'),
    url(r'^images/([0-9]{1,2})/$', views.image, name='image'),
    url(r'^images/([0-9]{1,2})/edit/$', views.edit_image, name='edit image'),
    url(r'^images/([0-9]{1,2})/full_image$', views.full_image, name='full_image'),

] 
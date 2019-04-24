# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views
# Create your urls here.

urlpatterns = [
	url(r'^$',views.index , name='index'),
	url(r'^home',views.home , name='home'),
	url(r'^LiveLogFile/(?P<TSRpath>\w+)/',views.LiveLogFile, name='LiveLogFile'),
	url(r'^LiveDevLogFile/(?P<TSRpath>\w+)/',views.LiveDevLogFile, name='LiveDevLogFile'),
	url(r'^LiveAdvanceImages/(?P<TSRpath>\w+)/',views.LiveAdvanceImages, name='LiveAdvanceImages'),
]

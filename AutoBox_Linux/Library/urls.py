# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views
# Create your urls here.

urlpatterns = [
	url(r'^$',views.index , name='index'),
	url(r'^AddNovelForm',views.AddNovelForm , name='AddNovelForm'),
	url(r'^AddChapterForm',views.AddChapterForm , name='AddChapterForm'),
	url(r'^AddPageForm',views.AddPageForm , name='AddPageForm'),
	url(r'^ADDPAGE',views.ADDPAGE , name='ADDPAGE'),
	url(r'^ADDCHAPTER',views.ADDCHAPTER , name='ADDCHAPTER'),
	url(r'^ADDNOVEL',views.ADDNOVEL, name='ADDNOVEL'),
	url(r'^fetchdata/(?P<filename>\w+)/',views.fetchdata, name='fetchdata'),
	url(r'^home',views.home , name='home')
]

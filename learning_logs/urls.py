# -*- coding:utf-8 -*-
#����learning_logs��URLģʽ

from django.conf.urls import url

from .import views

urlpatterns = [
	#��ҳ
	url(r'^$', views.index, name = 'index'),
	
	#��ʾ���е�����
	url(r'^topics/$', views.topics, name='topics'),	
]

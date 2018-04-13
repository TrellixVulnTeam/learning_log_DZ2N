# -*- coding:utf-8 -*-
#����learning_logs��URLģʽ

from django.urls import path
from django.conf.urls import url
from .import views

app_name = 'learning_logs'

urlpatterns = [
	#��ҳ
	path('', views.index, name = 'index'),
	
	#��ʾ���е�����
	path('topics/', views.topics, name = 'topics'),	
	
	#�ض��������ϸҳ��
	path('topics/<int:topic_id>/', views.topic, name = 'topic'),
]

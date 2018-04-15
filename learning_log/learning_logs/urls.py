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
	
	#����������������ҳ
	path('new_topic/', views.new_topic, name = 'new_topic'),
	
	#�����������Ŀ��ҳ��
	path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
	
	#���ڱ༭��Ŀ��ҳ��
	path('edit_entry/<int:entry_id>', views.edit_entry, name = 'edit_entry'),
	
]

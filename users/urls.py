#ΪӦ�ó���users����URLģʽ

from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name = 'users'

urlpatterns = [
	#��½ҳ��
	path('login/', login, {'template_name': 'users/login.html'}, name='login'),
	
	#ע��
	path('logout', views.logout_view, name = 'logout'),
	
	#ע��ҳ��
	path('register/', views.register, name = 'register'),
	
]

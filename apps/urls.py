
from django.contrib import admin
from .import views  # 导入模块
from django.urls import path


urlpatterns = [
    path('', views.login),
    path('index.html', views.index),  # 登录成功之后的个人页
    path('search.html',views.search),
    path('register.html',views.register)
]
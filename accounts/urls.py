"""project_movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

# urlpatterns = [
#     path('', views.MypageView.as_view(), name='mypage'),
#     path('agree/', views.AgreeView.as_view(), name='agree'),
#     path('join/', views.JoinView.as_view(), name='join'),
#     path('welcome/', views.WelcomeView.as_view(), name='welcome'),
# ]

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('update/', views.update, name='update'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
    path('userid/', views.UseridView.as_view(), name='userid'),
    path('agree/', views.AgreeView.as_view(), name='agree'),
    path('heart/', views.HeartView.as_view(), name='heart'),
    path('delheart/', views.Del_heartView.as_view(), name='del_heart'),
]
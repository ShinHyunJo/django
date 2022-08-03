"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClistView.as_view(), name='clist'),
    path('review/', views.ReviewView.as_view(), name='review'),
    path('setup/', views.SetupView.as_view(), name='csetup'),
    path('modify/', views.ModifyView.as_view(), name='modify'),
    path('write/', views.WriteView.as_view(), name='write'),
    path('remove/', views.RemoveView.as_view(), name='remove'),
    path('cmnt/', views.CmntView.as_view(), name='cmnt'),
    path('cremove/', views.CremoveView.as_view(), name='cremove'),
    path('movie/', views.MovieView.as_view(), name='movie'),
]

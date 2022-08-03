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

app_name = 'movies'
urlpatterns = [
    path('<int:option>/', views.MoviesView.as_view(), name='movies'),
    path('minfo/<int:movie_pk>/', views.MinfoView.as_view(), name='minfo'),
    path('genre_choice/', views.Genre_choiceView.as_view(), name='genre_choice'),
    path('choice_movie/', views.Choice_movieView.as_view(), name='choice_movie'),
    path(r'reco_movie/', views.Reco_movieView.as_view(), name='reco_movie'),
    path(r'movie/search/', views.movie_search, name="movie_search"),
    path('<int:movie_pk>/', views.detail, name='detail'),
]

import random

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from movies.models import Movie, Movie_genres, Genre
from accounts.models import User
# Create your views here.

class HomeView(View):
    def get(self, request):
        random_movies = []
        movies = Movie.objects.order_by('-popularity')

        random_movies.sort()

        random_nums = random.sample(range(0, len(movies)), 8)
        random_nums.sort()

        for i in random_nums:
            random_movies.append(movies[i])

        context = {'movies': random_movies}
        return render(request, 'home.html', context)

    def post(self, request):
        pass

class LoginView(View):
    def post(self, request):
        form = request.POST.dict()
        error = ''

        isExisted = User.objects.filter(username=form['userid'], password=form['passwd']).exists()

        # if count == 1:
        if isExisted:  # 로그인 성공시

            # 세션변수에 아이디와 id값을 저장 (userinfo:'abc123 | 1')
            # request.session['userinfo'] = form['userid'] + '|' + str(user.id)
            # print(request.session['userinfo'])

            user = User.objects.get(username=form['userid'])
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            returnPage = '/'

        else:
            returnPage = '/loginfail'
            # error = '로그인에 실패하였습니다.'

        # context = {'error' : error}

        return redirect(returnPage)

class LoginfailView(View):
    def get(self, request):
        return render(request, 'loginfail.html')



class LogoutView(View):
    def post(self, request):
        if request.user.is_authenticated:
            auth_logout(request)
        return redirect('home')
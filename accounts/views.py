from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import CustomUserCreationForm, CustomUserChangeForm
import json
from accounts.models import User, Heart
from movies.models import Movie


# Create your views here.


# @require_http_methods(['GET', 'POST'])
def login(request):
    # print(request)
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        form = request.POST.dict()
        user = User(username=form['muserid'],
                    password=form['mpasswd']
                    )
        auth_login(request, user)

        # form = AuthenticationForm(request, request.POST)
        if user.is_authenticated:
            return redirect('profile')
        else:
            error = '<li>로그인 정보를 확인하세요</li>'

        context = {'error': error}

    return render(request, '/', context)


        #
        # if form.is_valid():
        #     auth_login(request, form.get_user())
        #     return redirect(request.GET.get('next') or '/')
    # else:
    #     form = AuthenticationForm()
    # context = {
    #     'form': form,
    # }
    # return render(request, 'home.html', context)
    #
    #


    #     print(form)
    #
    #     user = User(username=form['userid'],
    #                 password=form['passwd']
    #                 )
    #     auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    #
    #     if user.is_authenticated:
    #         return redirect(request.GET.get('next') or 'home')
    #
    # else:
    #     context = {
    #     }
    # return render(request, 'accounts/login.html', context)

    # username = request.POST['userid']
    # password = request.POST['passwd']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     return redirect('home')
    # else:
    #     error = '<li>로그인 정보를 확인하세요</li>'
    #
    # context = {'error': error}
    # return render(request, '/', context)


# @require_POST   현재 get으로 오고 있음
def logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            auth_logout(request)
        return redirect('home')


@require_http_methods(['GET', 'POST'])
def signup(request):
    # if request.user.is_authenticated:
    #    return redirect('home')

    if request.method == 'POST':
        form = request.POST.dict()
        print(form)
        email = form['email1'] + '@' + form['email2']
        user = User(username = form['userid'],
                    password = form['passwd'],
                    userid = form['name'],
                    email = email
                    )
        user.save()
        auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        print(user.is_authenticated)
        if user.is_authenticated:
            return redirect('profile')

    context = {
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def signout(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('home')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)


# @require_safe
def profile(request):
    if request.method == 'GET':
        context = {
        }
        return render(request, 'accounts/profile.html', context)

    if request.method == 'POST':
        print('로그아웃 할까요~~')
        if request.user.is_authenticated:
            auth_logout(request)
            print('로그아웃 됐어요~~')
        return redirect('home')


    # person = get_object_or_404(get_user_model(), username=username)
    # if person.is_staff and not request.user.is_staff:
    #     # staff권한 가진 경우 프로필페이지 접근하지 못하도록 함
    #     # staff는 접근 가능 가능
    #     # messages.warning(request, "권한이 없습니다.")
    #     # 권한 없을때 메시지를 띄우고 요청을 보내기 이전 페이지로 redirect하는 방법을 고민....
    #     return redirect('home')
    # context = {
    #     'person': person,
    # }
    # return render(request, 'accounts/profile.html', context)


class UseridView(View):
    def get(self, request):
        # join/userid?userid=아이디
        # 응답메세지 => {'result':  0 또는 1}
        form = request.GET.dict()

        # select count(*) form member where userid=?
        count = User.objects.filter(username=form['userid']).count()
        # if form['password'] is None:
        #     count = User.objects.filter(username=form['userid']).count()
        # else:
        #     count = User.objects.filter(username=form['userid'],
        #                                 password=form['passwd']).count()

        # 조회된 카운트를 json형식의 데이터로 생성
        json_data = {'count': count}

        # 생성된 json데이터를 직렬화함 - 지원안됨(직렬화시 필요한 정보부족)
        # json_data = serializers.serialize('json', json_data)
        # 카운트는 json.dumps함수를 이용해서 간단하게 문자열로 직렬화
        return HttpResponse(json.dumps(json_data), content_type='application/json')

    def post(self, request):
        pass


class Del_heartView(View):
    def get(self, request):
        return render(request, 'accounts/heart.html')

    def post(self, request):
        delform = request.POST.dict()
        deltable = Heart.objects.get(title=delform['deltitle'])
        deltable.delete()
        return render(request, 'accounts/mypage.html')

class HeartView(View):
    def get(self, request):
        # form = request.GET.dict()
        # h = Heart(title=form['data1'], date=form['data2'], img=form['data3'])
        # h.save()
        heart = Heart.objects.all()
        context = {'heart': heart}
        # data1 = request.GET.get('data1')
        # data2 = request.GET.get('data2')
        # data3 = request.GET.get('data3')
        #
        # context = {'data1': data1, 'data2': data2, 'data3': data3}
        return render(request, 'accounts/heart.html', context)

    def post(self, request):
        form = request.POST.dict()
        h = Heart(title=form['title'], date=form['date'], img=form['img'])
        heart = Heart.objects.all()

        he = heart.filter(title=form['title']).count()
        #mpk = Movie.objects.values(id).get(form['mid'])
        print(he)
        #print(mpk)
        aaa = he
        if he < 1:
                print(aaa)
                print(form['title'])
                h.save()
        context = {'heart': heart}

        # data1 = request.POST.get('data1', '')
        # data2 = request.POST.get('data2', '')
        # data3 = request.POST.get('data3', '')
        # context = {'title': data1, 'date': data2, 'img': data3}
        # return redirect('accounts/heart.html')
        return render(request, 'accounts/heart.html', context)


class AgreeView(View):
    def get(self, request):
        return render(request, 'accounts/agree.html')


class CheckmeView(View):
    def get(self, request):
        return render(request, 'accounts/signup.html')

    def post(self, request):
        SECRET_KEY = '6LdJ86YgAAAAAFCwfn1twIbyxdgxto3309au3KYr'
        VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'
        form = request.POST.dict()
        # ?secret=비밀키&response=클라이언트 응답키
        params = {'secret': SECRET_KEY, 'response': form['g-recaptcha']}

        # 구글 recaptcha

        from django.contrib.sites import requests
        result = requests.get(VERIFY_URL, params=params).json()
        # 결과 success가 true면 joinme로 redirect
        if result['success']:
            # 인증성공시 이름과 전화번호를 dict에 저장해둠
            tokens = {'name': form['name'], 'phone': form['phone']}
            tokens = json.dumps(tokens, ensure_ascii=True)
            print(tokens)
            res = redirect('/join/joinme')
            res.set_cookie('tokens', tokens, max_age=60*10)
            return res

            #tokens = {'name': form['name'], 'phone': form['phone']}

            #return redirect('/join/joinme') # 기존거 주석 쿠키 설정없이 페이지만 전환

            #res = redirect('/join/joinme')
            # dict(res)객체를 쿠키에 저장해둠(유지시간 maxage 10분설정)
            # 응답객체.set_cookie(키, 값, 유지시간)
            #res.set_cookie('tokens', tokens, max_age=60*10)
            #return res

        else:
            error = '자동가입방지 인증이 실패했습니다'

        context = {'form': form, 'error': error}
        return render(request, 'accounts/signup.html', context)
from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from urllib.parse import urlencode

# Create your views here.
from math import ceil
from community.models import Review, Comment
from accounts.models import User
from movies.models import Movie

# Create your views here.

class ClistView(View):
    def get(self, request, perPage=5):
        form = request.GET.dict()
        qry = ''

        if request.GET.get('fkey') is not None and request.GET.get('ftype') is not None:
            if form['ftype'] == 'title':
                clist = Review.objects.all().filter(title__contains=form['fkey'])
            elif form['ftype'] == 'mtitle':
                clist = Review.objects.all().filter(movie__title__contains=form['fkey'])
            elif form['ftype'] == 'contents':
                clist = Review.objects.all().filter(contents__contains=form['fkey'])

            # get으로 전송된 키와 값을 인코딩해서 질의문자열로 변환
            qry = urlencode({'ftype': form['ftype'], 'fkey': form['fkey']})

        else:
            clist = Review.objects.all()

        pages = ceil(clist.count() / perPage)
        cpage = 1
        if request.GET.get('cpage') is not None: cpage = form['cpage']

        start = (int(cpage) - 1) * perPage
        end = start + perPage
        clist = clist[start:end]

        # cmt = Comment.objects.filter(rno__comment=1)



        stpgn = int((int(cpage) - 1) / 10) * 10 + 1

        context = {'crs': clist, 'pages': pages, 'range': range(stpgn, stpgn + 10), 'qry': qry }

        return render(request, 'community/clist.html', context)

    def post(self, request):
        pass

class SetupView(View):
    def get(self, request):
        for i in range(175):
            r = Review(title='영화는 재밌어',
                      user=User.objects.get(id=2),
                      contents='영화는 재밌어',
                       movie=Movie.objects.get(id=144))

            r.save()

            r = Review(title='재밌는건 마블',
                      user=User.objects.get(id=1),
                      contents='재밌는건 마블',
                       movie=Movie.objects.get(id=517302))

            r.save()

            r = Review(title='마블은 빨개',
                      user=User.objects.get(id=2),
                      contents='마블은 빨개',
                       movie=Movie.objects.get(id=543633))

            r.save()

        return redirect('/')


class ReviewView(View):
    def get(self, request):
        form = request.GET.dict()

        Review.objects.filter(id=form['rno']).update(views=F('views') + 1)

        cr = Review.objects.all().get(id=form['rno'])

        cmt = Comment.objects.select_related().filter(rno__id=form['rno']).order_by('cno', 'id')
        # lgnusr = ''
        #
        # if request.session.get('userinfo') is not None:
        #     lgnusr = request.session['userinfo'].split('|')[0]

        context = {'cr': cr, 'cmt': cmt}

        return render(request, 'community/review.html', context)

    def post(self, request):
        pass


class ModifyView(View):
    def get(self, request):
        form = request.GET.dict()
        r = Review.objects.values().get(id=form['rno'])
        m = Movie.objects.values().get(id=r['movie_id'])

        context = {'r': r, 'm': m}

        return render(request, 'community/modify.html', context)

    def post(self, request):
        form = request.POST.dict()
        print(form)
        Review.objects.filter(id=form['rno']).update(title=form['rtitle'], contents=form['contents'])

        return redirect('/community/review?rno=' + form['rno'])


class WriteView(View):
    def get(self, request):
        return render(request, 'community/write.html')

    def post(self, request):
        form = request.POST.dict()

        r = Review(title=form['rtitle'],
                   contents=form['contents'],
                   movie_id=form['id'],
                   user_id=form['user']
                   )
        r.save()

        rno = Review.objects.latest('id').id

        return redirect('/community/review?rno=' + str(rno))


class RemoveView(View):
    def get(self, request):
        form = request.GET.dict()
        print(form)

        # c = Review.objects.values('user_id').get(id=form['rno'])
        c = Review.objects.get(id=form['rno'])
        print(c)
        print(request.user.id)
        print(c.user_id)

        # if문을 안 쓰면 pds/remove/?pno= 경로 직접 치면 남의꺼도 삭제 됨
        if request.user.id == c.user_id:
            r = Review.objects.filter(id=form['rno'])
            r.delete()

        return redirect('clist')

    def post(self, request):
        pass


class CmntView(View):
    def post(self, request):
        form = request.POST.dict()

        cno = Comment.objects.values().order_by('-pk')[0]

        c = Comment(cno= cno['id'] + 1,
                    rno=Review.objects.get(id=form['rno']),
                    userid=User.objects.get(userid=form['userid']),
                    comments=form['comments'])
        c.save()

        return redirect('/community/review?rno=' + form['rno'])


class CremoveView(View):
    def post(self, request):
        form = request.POST.dict()
        rc = Comment.objects.get(id=form['cid'])

        if request.user.id == int(form['userid']):
            rc.delete()

        return redirect('/community/review?rno=' + form['rno'])

class MovieView(View):
    def get(self, request):
        form = request.GET.dict()
        # print(form)

        # select * from Movies_movie where title = 영화제목
        # 테이블모델명.objects.get(조건) : 1개의 결과값만 처리
        # result = Movies_movie.objects.get(title = '후예들')
        # print(result.movies_movie)  # 속성명으로 값 출력

        # 테이블모델명.objects.filter(조건) : 1개이상 결과값 처리
        # result = Movie.objects.filter(title=form['title'])
        result = Movie.objects.filter(title__contains=form['title'])
        # print(result.values())

        # 조회결과를 JSON객체로 생성
        from django.core import serializers
        json_data = serializers.serialize('json', result)
        # print(json_data, form['title'])

        # 생성된 JSON객체를 HTTP 응답객체로 전송
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request):
        pass

# class CmodifyView(View):
#     # def post(self, request):
#     #     form = request.POST.dict()
#     #     Comment.objects.filter(id=form['id']).update(comments=form['contents'])
#     def get(self, request):
#         form = request.GET.dict()
#         cmt = Comment.objects.get(id=form['id'])
#
#         return redirect('/community/cmodify')


from django.core.paginator import Paginator
from django.db.models import Q,Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# Create your views here.
from django.views.decorators.http import require_safe
from movies.models import Movie, Movie_genres, Genre
# from movies.forms import CommentForm




class MoviesView(View):
    def get(self, request, option):
        if option == 1:
            movies = Movie.objects.order_by('-release_date')
        elif option == 2:
            movies = Movie.objects.order_by('-popularity')
        elif option == 3:
            movies = Movie.objects.order_by('title')
        elif option == 4:
            movies = Movie.objects.order_by('-vote_average')

        else:
            movies = Movie.objects.order_by('-popularity')

        genres = Movie_genres.objects.all()
        mgenres = Genre.objects.all()

        paginator = Paginator(movies, 8)
        page = paginator.get_page(paginator)

        context = {
            'movies': page,
            'genres': genres,
            'mgenres': mgenres
        }
        return render(request, 'movies/movies.html', context)

    def post(self, request):
        pass


class MinfoView(View):
    def get(self, request, movie_pk):
        # movies = Movie.objects.order_by('-popularity')
        movie = get_object_or_404(Movie, pk=movie_pk)
        genres = Movie_genres.objects.all()
        mgenres = Genre.objects.all()

        if (movie.vote_average * 10 // 10) >= 8:
            vote_average = '★★★★★'
        elif (movie.vote_average * 10 // 10) >= 6:
            vote_average = '★★★★'
        elif (movie.vote_average * 10 // 10) >= 4:
            vote_average = '★★★'
        elif (movie.vote_average * 10 // 10) >= 2:
            vote_average = '★★'
        elif (movie.vote_average * 10 // 10) >= 0:
            vote_average = '★'

            return vote_average

        # genre = Movie_genres.objects.select_related(movie)
        # genre = Movie.objects.select_related(id)
        # genres = Movie_genres.objects.all()

        # select title, movie_id, genre_id, name
        # from movies_movie as mm, movies_movie_genres as mmg, movies_genre as mg
        # where mm.id = mmg.movie_id and mmg.genre_id = mg.id;

        gr = Movie_genres.objects.filter(movie__id=movie_pk).values('genre__name')

        context = {
            'movie': movie,
            'genres': genres,
            'mgenres': mgenres,
            'star': vote_average,
            'gr': gr
        }
        return render(request, 'movies/minfo.html', context)

    def post(self, request):
        pass


class Genre_choiceView(View):
    def get(self, request):
        return render(request, 'movies/genre_choice.html')

    def post(self, request):
        pass


class Reco_movieView(View):
    def get(self, request):
        return render(request, 'movies/reco_movie.html')

    def post(self, request):
        pass


class Choice_movieView(View):
    def get(self, request):
        return render(request, 'movies/choice_movie.html')

    def post(self, request):
        form = request.POST.getlist('genre')
        form = list(map(int, form))
        # print(form)
        movies = Movie.objects.order_by('-popularity')
        mgenres = Movie_genres.objects.all()
        gm = Genre.objects.all()

        context = {'genres': form, 'movies': movies, 'mgenres': mgenres, 'gm': gm}

        return render(request, 'movies/choice_movie.html', context)




def movie_search(request):
    keyword = request.GET.get('message')
    if keyword == '':
        movies = []
    else:
        movies = Movie.objects.filter(Q(title__contains=keyword)|Q(overview__contains=keyword))

    context = {
        'keyword': keyword,
        'movies': movies,
    }
    return render(request, 'movies/movie_search.html', context)




@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # comment_form = CommentForm()
    comments = movie.comment_set.all()
    reviews = movie.reviews.all()[:5]  # 영화에 달린 리뷰 정보 5개 보냄
    reviewer_rank = movie.reviews.all().aggregate(Avg('rank'))['rank__avg']  # 리뷰어 평점 추가
    reviewer_count = movie.reviews.all().count()  # 리뷰어 수 추가

    context = {
        'movie': movie,
        #'comment_form': comment_form,
        'comments': comments,
        'reviews': reviews,
        'reviewer_rank': reviewer_rank,
        'reviewer_count': reviewer_count,
    }
    return render(request, 'movies/detail.html', context)
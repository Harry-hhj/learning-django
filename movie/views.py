from django.http import HttpResponse
from django.shortcuts import render


def movie(request):
    return render(request, 'movie.html')


def movie_list(request):
    return HttpResponse('电影列表')

from django.urls import path
from . import views


app_name = 'movie'

urlpatterns = [
    path('', views.movie, name='index'),
    path('list/', views.movie_list, name='list'),
]
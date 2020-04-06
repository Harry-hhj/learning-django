from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.book, name='index'),
    path('detail/<book_id>', views.book_detail, name='detail'),
    path('author', views.author_detail, name='author'),
    path('publisher/<uuid:publisher_id>', views.pubish_detail, name='publisher'),
    path('list/', views.book_list, name='list'),
]

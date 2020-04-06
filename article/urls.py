from django.urls import re_path, path, register_converter
from . import views

app_name = 'article'


urlpatterns = [
    # r''：代表原生字符串，为raw简写
    re_path(r'^$', views.article, name='index'),
    re_path(r'^list/(?P<year>\d{4})/$', views.article_list, name='year'),
    re_path(r'^list/(?P<year>\d{4})/(?P<month>\d{2})/$', views.article_list_month, name='month'),
    re_path(r'^list/(?P<year>\d{4})/(?P<month>\d{2})/(?P<date>[0-9][0-9]?)/$', views.article_list_date, name='date'),
    # re_path(r'^list/(?P<categories>\w+|(\w+\+\w+)+)/$', views.article_categories_list)
    path('list/<cate:categories>/', views.article_categories_list, name='categories')
]

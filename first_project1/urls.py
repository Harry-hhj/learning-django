"""first_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.http import HttpResponse
# import movie.views


# def index(request):
#     return HttpResponse('首页')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    path('book/', include('book.urls')),
    # path('movie/', include(('movie.urls', 'movie'), namespace='movie')),
    path('movie/', include('movie.urls', 'movie')),
    # path('movie/', include(([
    #     path('', movie.views.movie),
    #     path('list/', movie.views.movie_list)
    # ], 'movie'), namespace='movie')),
    path('', include('front.urls')),
    # 同一个app下有两个实例
    path('cms/', include('cms.urls', namespace='cms')),
    path('cms1/', include('cms.urls', namespace='cms1')),
    path('article/', include('article.urls')),
    path('city/', include('city.urls')),
    path('filter/', include('filter.urls'))
]

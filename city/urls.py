from django.urls import path
from . import views

app_name = 'city'

urlpatterns = [
    path('', views.index, name='index')
]
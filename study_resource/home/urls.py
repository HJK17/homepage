from django.urls import path
from study_resource.home.views import DetailView, Homepage
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='mypage'),
    path('study/homepage/', Homepage.as_view(), name='homepage'),
    path('study/detail/', DetailView.as_view(), name='detail'),
]

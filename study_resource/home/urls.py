from django.urls import path
from study_resource.home.views import DetailView, Homepage
# from study_resource.home import views
# from apps.study_resource.views import Homepage
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('study/homepage/', Homepage.as_view(), name='homepage'),
    path('study/detail/', DetailView.as_view(), name='detail'),
]

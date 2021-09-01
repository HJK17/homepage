
from django.urls import path
from personal_project import views

app_name = 'personal_project'

urlpatterns = [
    path('porject/homeproject/', views.homeproject, name='homeproject')
]

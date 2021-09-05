from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django_redis import get_redis_connection
from django.core.cache import cache
from personal_project.goods.models import *
from django.views.generic import View


def IndexView(request):

    # 使用模板
    return render(request, "project/index.html")
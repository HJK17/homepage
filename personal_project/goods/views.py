from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def Goodspage(request):
    return render(request, 'project/goodspage.html')

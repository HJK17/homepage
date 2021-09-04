from django.shortcuts import render
from django.views import View


# Create your views here.


class GoodspageView(View):
    def get(self, request):
        render(request, 'project/goodspage.html')

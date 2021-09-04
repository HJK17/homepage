from django.shortcuts import render


# Create your views here.

def homeproject(request):
    return render(request, 'project/index.html')

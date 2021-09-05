from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('goods.urls', namespace='pgoods')),
    path('', include('user.urls', namespace='puser')),
    path('', include('order.urls', namespace='porder')),
    path('', include('cart.urls', namespace='pcart')),

    path('', include('home.urls', namespace='studyhome')),
    path('', include('users.urls', namespace='studyusers')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

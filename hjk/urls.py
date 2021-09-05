from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personal_project.goods.urls', namespace='pgoods')),
    path('', include('personal_project.user.urls', namespace='puser')),
    path('', include('personal_project.order.urls', namespace='porder')),
    path('', include('personal_project.cart.urls', namespace='pcart')),

    path('', include('study_resource.home.urls', namespace='studyhome')),
    path('', include('study_resource.users.urls', namespace='studyusers')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

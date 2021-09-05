from django.urls import path, include, re_path
from personal_project.goods.views import IndexView
# from personal_project.goods.views import IndexView, DetailView, ListView

app_name = 'goods'

urlpatterns = [
    path("project/index", IndexView, name="index"),  # 首页
    # path("index/", IndexView.as_view(), name="index"),  # 首页
    # re_path(r'^goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'),  # 详情页
    # re_path(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'),  # 列表页
]

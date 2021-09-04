from django.urls import path, include, re_path
from personal_project.user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, \
    UserAddressView

app_name = 'user'

urlpatterns = [
    re_path(r"^register/$", RegisterView.as_view(), name='register'),  # 注册
    re_path(r"^register/$", RegisterView.as_view(), name='register'),  # 注册
    re_path(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 激活
    # path('login', LoginView.as_view(), name='login'),  # 登录
    re_path(r"^login/$", LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout'),  # 登出

    path('', UserInfoView.as_view(), name='user'),  # 用户中心--信息页
    re_path(r"^order/(?P<page>\d+)/$", UserOrderView.as_view(), name='order'),
    path('address', UserAddressView.as_view(), name='address'),  # 用户中心--地址页

]

from django.urls import path
from study_resource.users.views import RegisterView, ImageCodeView, WriteBlogView
from study_resource.users.views import SmsCodeView, LoginView, LogoutView, ForgetPasswordView, UserCenterView

app_name = 'users'

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('study/register/', RegisterView.as_view(), name='register'),
    path('study/imagecode/', ImageCodeView.as_view(), name='imagecode'),
    path('smscode/', SmsCodeView.as_view(), name='smscode'),
    path('study/login/', LoginView.as_view(), name='login'),
    path('study/logout/', LogoutView.as_view(), name='logout'),
    path('study/forgetpassword/', ForgetPasswordView.as_view(), name='forgetpassword'),
    path('study/center/', UserCenterView.as_view(), name='center'),
    path('study/writeblog/', WriteBlogView.as_view(), name='writeblog'),
]

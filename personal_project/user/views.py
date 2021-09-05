from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import re
from personal_project.user.models import User
from django.views.generic import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired  # 加密
from celery_tasks.tasks import send_register_active_email


def register(request):
    """显示注册页面"""
    if request.method == "GET":
        return render(request, "")
    else:
        """注册处理"""
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get("pwd")
        email = request.POST.get("email")
        allow = request.POST.get("allow")  # 同意协议
        if allow != 'on':
            return render(request, "project/register.html", {'errmsg': "请同意协议"})
        # 数据效验
        if not all([username, password, email]):  # all 方法 可迭代判断每个元素
            return render(request, "project/register.html", {'errmsg': "数据不完整"})
        # 验证邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, "project/register.html", {'errmsg': "邮箱错误"})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request, "project/register.html", {'errmsg': "用户名已存在"})
        # 业务处理
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()
        # 返回处理
        return redirect(reverse('pgoods:index'))


class RegisterView(View):

    def get(self, request):
        return render(request, 'project/register.html')

    def post(self, request):
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        if not all([username, password, email]):
            return render(request, 'project/register.html', {'errmsg': '数据不完整'})

        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'project/register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'project/register.html', {'errmsg': '请同意协议'})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'project/register.html', {'errmsg': '用户名存在'})

        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        # 发送激活邮件，包含激活链接: http://127.0.0.1:8000/user/active/3
        # 激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密

        # 加密用户的身份信息，生成激活token
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)  # bytes
        token = token.decode()

        # 发邮件
        send_register_active_email.delay(email, username, token)

        return redirect(reverse('pgoods:index'))

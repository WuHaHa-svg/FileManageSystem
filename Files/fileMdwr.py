# 中间件
from django.shortcuts import redirect
from django.urls import reverse
import re


class FileMdwr():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #获取请求的url
        path = request.path

        #必须登录的页面需要用session验证
        if re.match(r'^/file', path) or re.match(r'^/logout', path):
            if 'userInfo' not in request.session:
                return redirect(reverse("login"))

        response = self.get_response(request)
        return response

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
import io
import random
from PIL import Image, ImageDraw, ImageFont
from Files.models import User


# Create your views here.
# 注册页面
def signup(request):
    return render(request, 'signup/signup.html')


# 注册操作
def doSignup(request):
    username = request.POST['username']
    passwd = request.POST['passwd']
    passwd_1 = request.POST['passwd_1']
    same_name = User.objects.filter(username=username)
    if same_name:
        conf = '此用户已存在！'
        context = {'conf': conf}
        return render(request, 'signup/signup.html', context)
    if passwd_1 != passwd:
        conf = '两次输入密码不一致！'
        context = {'conf': conf}
        return render(request, 'signup/signup.html', context)

    if request.session['verifycode'] == request.POST['code']:
        mod = User()
        mod.username = username
        mod.passwd = passwd
        mod.save()
        conf = '创建成功，快去登陆吧！'
        context = {'conf': conf}
        return render(request, 'signup/signup.html', context)
        # return redirect(request,reverse("login"))
    else:
        conf = '验证码错误！'
        context = {'conf': conf}
        return render(request, 'login/login.html', context)


# 验证码
def signupVerify(request):
    bgcolor = (242, 164, 247)
    im = Image.new('RGB', (100, 25), bgcolor)
    draw = ImageDraw.Draw(im)
    for i in range(0, 100):
        xy = (random.randrange(0, 100), random.randrange(0, 25))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    str1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    rand_str = ''
    for i in range(0, 4):
        a = random.randint(0, 9)
        rand_str = rand_str + str1[a]
    font = ImageFont.truetype('static/fronts/arial.ttf', 21)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
    del draw
    request.session['verifycode'] = rand_str
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

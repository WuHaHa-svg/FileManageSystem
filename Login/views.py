from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
import io
import random
from PIL import Image, ImageDraw, ImageFont
from Files.models import User


# Create your views here.

# 登陆页面
def login(request):
    return render(request, 'login/login.html')


# 登陆操作
def doLogin(request):
    try:
        user = User.objects.get(username=request.POST['username'])
    except:
        conf = '请核对账户信息是否正确，若无账户，请先注册！'
        context = {'conf': conf}
        return render(request, 'login/login.html', context)
    if user.passwd == request.POST['passwd']:
        if request.session['verifycode'] == request.POST['code']:
            request.session['userInfo'] = user.toDict()
            return redirect(reverse("file_index"))
        else:
            conf = '验证码错误！'
            context = {'conf': conf}
            return render(request, 'login/login.html', context)
    else:
        conf = '用户名或者密码错误！'
        context = {'conf': conf}
        return render(request, 'login/login.html', context)


# 注销
def logout(request):
    del request.session['userInfo']
    return render(request, 'login/login.html')


# 验证码
def verify(request):
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

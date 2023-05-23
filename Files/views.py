from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, FileResponse
from django.db.models import Q
from .models import User, File


# Create your views here.

# 加载文件管理首页
def index(request):
    return render(request, 'files/index.html')


# 用户编辑信息表单
def editInfo(request):
    return render(request, 'files/user_edit.html')


# 更新数据库用户信息
def updateInfo(request, uid=0):
    op = User.objects.get(id=uid)
    op.username = request.POST['username']
    op.introduction = request.POST['introduction']
    op.save()
    context = {'conf': "编辑信息后，需重新登录！"}
    return render(request, 'login/login.html', context)


# 浏览文件管理页面
def fileHome(request, uid):
    mod = File.objects
    fileList = mod.filter(Q(author_id=uid) & Q(file_status=1))
    if list(fileList) == []:
        context = {'conf': "您并没有上传任何文件！"}
        return render(request, 'files/nofile.html', context)
    else:
        context = {'fileList': fileList}
        return render(request, 'files/file_home.html', context)


# 添加文件表单页面
def addFile(request):
    return render(request, 'files/add.html')


# 持久化存储文件，同步数据库
def insertFile(request, author_id):
    # author_id
    file = request.FILES.get("file", None)
    file_lenth = len(file) // 1024  # 文件大小/KB

    if request.POST['file_name']:
        file_name = request.POST['file_name'] + '.' + str(file).split('.')[-1]
    else:
        file_name = str(file)

    file_status = 1
    file_type = str(file).split('.')[-1].upper()
    file_path = './static/uploads/' + file_name
    # 文件存储
    with open(file_path, 'wb+') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    # 数据库同步
    mod = File()
    mod.file_name = file_name
    mod.file_status = file_status
    mod.author_id = author_id
    mod.file_type = file_type
    mod.file_lenth = file_lenth
    mod.file_path = file_path
    mod.save()

    return redirect(reverse("file_index"), )


# 删除文件
def delFile(request, fid):
    op = File.objects.get(id=fid)
    op.file_status = 0
    op.save()
    return redirect(reverse("file_index"))


# 下载文件
def downloadFile(request, fid):
    op = File.objects.get(id=fid)
    file_path = op.file_path
    file_name = file_path.split('/')[-1]
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename=file_name'
    return response

from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index, name="file_index"),                         #文件管理首页
    path('edit/', views.editInfo, name="editInfo"),                         #用户编辑信息
    path('update/<int:uid>', views.updateInfo, name="updateInfo"),          #更新用户数据库信息
    path('home/<int:uid>', views.fileHome, name="fileHome"),                #文件管理页面
    path('addfile/', views.addFile, name="addFile"),                        #加载提交文件表单
    path('insert/<int:author_id>', views.insertFile, name="insertFile"),    #同步文件到数据库
    path('del/<int:fid>', views.delFile, name="delFile"),                   #删除文件
    path('download/<int:fid>', views.downloadFile, name="downloadFile"),    #下载文件
]

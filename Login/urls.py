from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login, name="login"),  # 登陆页面
    path('doLogin/', views.doLogin, name="dologin"),  # 登陆操作
    path('logout/', views.logout, name="logout"),  # 注销、消除session
    path('verify/', views.verify, name="verify"),  # 验证码

]

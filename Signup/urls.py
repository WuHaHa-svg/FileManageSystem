from django.urls import path,include
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('signup',views.signup,name = "signup"),                    #注册页面
    path('doSignup',views.doSignup,name = "dosignup"),              #注册操作
    path('signupVerify',views.signupVerify,name = "signupverify"),  #注册验证码

]

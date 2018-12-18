from django.conf.urls import url
from user.views import Login, Logout, Checkis, ResetPassword, create_user, Registry

urlpatterns = [
    url(r'^login/$', Login, name="Login"),
    url(r'^logout/$', Logout, name="Logout"),
    url(r'^registry/$', Registry, name="Registry"),
    url(r'^checkis/$', Checkis),
    url(r'^reset_password/(?P<onlyid>.+)$', ResetPassword),
    # 创建用户
    url(r'^create_user/$', create_user),
    # 获取个人详情
    # 修改个人资料
]

from django.conf.urls import url
from user.views import Login, Logout, Checkis, ResetPassword, create_user

urlpatterns = [
    url(r'^login/$', Login, name="Login"),
    url(r'^logout/$', Logout, name="Logout"),
    url(r'^checkis/$', Checkis),
    url(r'^reset_password/(?P<onlyid>.+)$', ResetPassword),
    # 创建用户
    url(r'^create_user/$', create_user),
]

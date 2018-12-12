from django.conf.urls import url
from user.views import Login, Checkis, ResetPassword

urlpatterns = [
    url(r'^login/$', Login, name="Login"),
    url(r'^checkis/$', Checkis),
    url(r'^reset_password/(?P<onlyid>.+)$', ResetPassword)
]

from django.conf.urls import url
from user.views import Login

urlpatterns = [
    url(r'^login/$', Login, name="Login"),
]

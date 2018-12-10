from django.conf.urls import url
from user.views import Login, Checkis

urlpatterns = [
    url(r'^login/$', Login, name="Login"),
    url(r'^checkis/$', Checkis),
]

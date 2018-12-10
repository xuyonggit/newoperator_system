from django.conf.urls import url
from page.views import index

urlpatterns = [
    url(r'^index_new/$', index, name="Index"),
]

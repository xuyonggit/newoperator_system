from django.conf.urls import url
from page.views import index, names
urlpatterns = [
    url(r'^index_new_1/$', index, name="Index"),
    url(r'^names/$', names),
]

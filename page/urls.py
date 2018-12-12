from django.conf.urls import url
from page.views import index
from page.views import index_new_2
from page.views import index_new_3
from page.views import index_new_4
from page.views import guanli
urlpatterns = [
    url(r'^index_new_1/$', index, name="Index"),
    url(r'^index_new_2/$', index_new_2, name="Index_new_2"),
    url(r'^index_new_3/$', index_new_3, name="Index_new_3"),
    url(r'^index_new_4/$', index_new_4, name="Index_new_4"),
    url(r'^guanli/$', guanli, name="Guanli"),
]

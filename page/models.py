from django.db import models

# Create your models here.


class url_name (models.Model):
    username = models.CharField('名称', max_length=255, default=None)
    urls = models.CharField('链接', max_length=255, default=None)
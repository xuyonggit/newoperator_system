# md5
import hashlib
import uuid
from django.http import HttpResponseRedirect
from user.models import tb_user, tb_resetpwd


# 检查登录状态
def needLogin(func):
    """
    检查是否登录
    :param request:
    :return:
    """
    def warpper(request, *args, **kwargs):
        sessionId = request.COOKIES.get("sessionId", False)
        if sessionId and checkSessionId(sessionId):
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/user/login/")
    return warpper


def to_md5(str):
    """
    密码MD5加密
    :param str:
    :return: str md5
    """
    md = hashlib.md5()
    md.update(str.encode('utf-8'))
    return md.hexdigest()


def makeResetLink(email_address):
    """
    创建重置密码uuid
    :param email_address:
    :return: uuid or False
    """
    address = email_address
    cdata = tb_user.objects.get(email_address=address)
    uid = cdata.id
    onlyid = uuid.uuid4()
    old_data = tb_resetpwd.objects.filter(userId=uid)
    if len(old_data) > 0:
        old_data.update(
            status=1
        )
    tb_resetpwd.objects.create(
        userId=uid,
        onlyId=onlyid,
    )
    return onlyid


def outUseOnlyId(onlyId):
    """
    失效重置ID
    :param onlyId:
    :return: bool
    """
    onlyId = onlyId
    c = tb_resetpwd.objects.get(onlyId=onlyId)
    c.status = 1
    c.save()
    return True


def makeSessionId(st='gintong'):
    """
    创建sessionId
    :param st: 任意字符串
    :return: sessionId
    """
    import time, hashlib, string
    m = hashlib.md5()
    m.update('this is my operator system-Gintong'.encode())
    m.update(str(time.time()).encode())
    m.update(str(st).encode())
    return m.hexdigest()


def saveSessionId(sessionId):
    pass


def checkSessionId(sessionId):
    return True

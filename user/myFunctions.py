# md5
import datetime
import hashlib
import json
import uuid
from django.http import HttpResponseRedirect
from user.models import tb_user, tb_resetpwd, tb_registry_code
from user.session import Mysessionbase


# 检查登录状态
def needLogin(func):
    """
    检查是否登录
    :param request:
    :return:
    """
    def warpper(request, *args, **kwargs):
        try:
            sessionid = request.META['HTTP_SESSIONID']
            if not sessionid:
                sessionid = request.COOKIES['sessionId'].replace("%3D", '=')
        except:
            sessionid = None
        Mysessionbase().clear_expired()
        if Mysessionbase(sessionid).exists():
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


# create user
def createUser(username, passwd, email_address, inviteId, position=None):
    """
    创建新用户
    :param username: 用户名
    :param passwd: 密码
    :param email_address: 邮箱地址
    :param inviteId: 邀请者id
    :param position: 职位
    :return: boolean
    """
    tb_user.objects.create(
        username=username,
        passwd=passwd,
        email_address=email_address,
        position=position,
        status=1
    )
    return True


# check exists user
def userExists(email_address):
    """
    判断用户是否存在，以邮箱地址为主
    :param email_address:
    :return: boolean
    """
    address = email_address
    if not address:
        raise ValueError('无效的address: {}'.format(address))
    d = tb_user.objects.filter(email_address=address)
    if len(d) > 0:
        return True
    return False


def checkRegistryCode(code):
    code = code
    try:
        red = tb_registry_code.objects.filter(registry_code=code, status=0).get()
        return red.userId
    except:
        return False


def invialdRegistryCode(code):
    code = code
    try:
        red = tb_registry_code.objects.filter(registry_code=code).get()
        red.status = 1
        red.save()
    except Exception as e:
        print(e)
        pass


def create_sessionId(userid, val='gintong'):
    # M = Mysessionbase()
    sessionid = Mysessionbase().create(userid=userid, username=val)
    return sessionid


def clearSessionId(sessionid):
    Mysessionbase().clear(sessionid=sessionid)


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def getUserIdFromSessionId(sessionid):
    return Mysessionbase().getUidfromSessionId(sessionid)


def make_UserInfo(uid):
    userinfo = tb_user.objects.filter(id=uid).values().first()
    if userinfo:
        del userinfo['passwd']
        return userinfo
    else:
        return False


def update_UserInfo(uid, username, sex, age, email_address, position=""):
    tb_user.objects.filter(id=uid).update(
        username=username,
        sex=sex,
        age=age,
        email_address=email_address,
        position=position
    )

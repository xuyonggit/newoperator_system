import base64
import datetime
import time
from django.utils import timezone
from user.models import session
from newoperator_system.settings import SESSION_COOKIE_AGE


class Mysessionbase(object):
    """
    session 管理
    """
    def __init__(self, session_id=None):
        """
        :param session_id:
        """
        self.session_key = session_id

    def save(self, userid):
        if self.session_key is None:
            return self.create()
        expired_date = timezone.now() + timezone.timedelta(seconds=SESSION_COOKIE_AGE)
        session.objects.create(
            userId=userid,
            sessionId=self.session_key,
            expire_date=expired_date
        )

    def create(self, userid, username='gintong'):
        username = username
        self.session_key = self.__get_new_sessionid(username=username)
        self.save(userid)
        return self.session_key
        # print(" create sessionid Error")

    def delete(self, sessionId=None):
        if sessionId is None:
            if self.session_key is None:
                return
            sessionId = self.session_key
        try:
            session.objects.get(sessionId=sessionId).delete()
        except session.DoesNotExist:
            pass

    def exists(self):
        return session.objects.filter(sessionId=self.session_key).exists()

    def clear(self):
        pass

    def clear_expired(self):
        session.objects.filter(expire_date__lt=timezone.now()).delete()

    def __get_new_sessionid(self, username='gintong'):
        """
        生成随机sessionid
        依据：当前unix时间戳 + username + 1
        :param username:
        :return: _sessionid
        """
        t = time.time()
        tmpvalue = str(t) + str(username) + '1'
        _sessionid = base64.b64encode(tmpvalue.encode()).decode()
        return _sessionid

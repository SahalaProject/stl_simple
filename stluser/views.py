from rest_framework.response import Response
from rest_framework.views import APIView
from stluser.common import response
from stluser import models
from stluser import serializers
import logging
# Create your views here.
from stluser.common.token import generate_token
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger('FastRunner')


class RegisterView(APIView):

    authentication_classes = ()
    permission_classes = ()

    """
    注册:{
        "user": "demo"
        "password": "1321"
        "email": "1@1.com"
    }
    """

    def post(self, request):

        try:
            username = request.data["username"]
            password = request.data["password"]
            email = request.data["email"]
        except KeyError:
            return Response(response.KEY_MISS)

        if models.UserInfo.objects.filter(username=username).first():
            return Response(response.REGISTER_USERNAME_EXIST)

        if models.UserInfo.objects.filter(email=email).first():
            return Response(response.REGISTER_EMAIL_EXIST)

        request.data["password"] = make_password(password)

        serializer = serializers.UserInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(response.REGISTER_SUCCESS)
        else:
            return Response(response.SYSTEM_ERROR)


class LoginView(APIView):
    """
    登陆视图，用户名与密码匹配返回token
    """
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        """
        用户名密码一致返回token
        {
            username: str
            password: str
        }
        """
        try:
            username = request.data["username"]
            password = request.data["password"]
        except KeyError:
            return Response(response.KEY_MISS)

        user = models.UserInfo.objects.filter(username=username).first()

        if not user:
            return Response(response.USER_NOT_EXISTS)

        if not check_password(password, user.password):
            return Response(response.LOGIN_FAILED)

        token = generate_token(username)

        try:
            models.UserToken.objects.update_or_create(user=user, defaults={"token": token})
        except ObjectDoesNotExist:
            return Response(response.SYSTEM_ERROR)
        else:
            response.LOGIN_SUCCESS["token"] = token
            response.LOGIN_SUCCESS["user"] = username
            return Response(response.LOGIN_SUCCESS)


class ForgetPasswordView(APIView):

    authentication_classes = ()
    permission_classes = ()

    """
    找回密码:{
        "user": "demo"
        "password": "abc123456"
        "repwd": "abc123456"
    }
    """

    def patch(self, request):
        username = request.data["username"]
        oldpwd = models.UserInfo.objects.filter(username=username).first().password
        res = check_password(request.data["oldpwd"], oldpwd)
        if res == False:
            return Response(response.MODPWD_FAILED)
        try:
            user = models.UserInfo.objects.filter(username=username).first()
            password = request.data["password"]
        except KeyError:
            return Response(response.KEY_MISS)

        if not models.UserInfo.objects.filter(username=username).first():
            return Response(response.FIND_NOT_EXISTS)

        request.data["password"] = make_password(password)
        user.username = request.data["username"]
        user.password = request.data["password"]
        user.save()
        return Response(response.FIND_SUCCESS)



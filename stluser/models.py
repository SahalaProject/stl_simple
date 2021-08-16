from django.db import models


# Create your models here.

class BaseTable(models.Model):
    """
    公共字段列
    """

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)


class UserInfo(BaseTable):
    """
    用户注册信息表
    """
    user_type_choice = (
        (1, 'ordinary_user'),
        (2, 'vip'),
        (3, 'svip'),
    )

    class Meta:
        verbose_name = "用户信息"
        db_table = "UserInfo"

    username = models.CharField('用户名', max_length=20, unique=True, null=False)
    real_name = models.CharField('真实姓名', max_length=20, null=True)
    password = models.CharField('登陆密码', max_length=100, null=False)
    email = models.EmailField('用户邮箱', unique=True, null=False)
    user_type = models.IntegerField('用户类型', default=1, null=True)
    project_field = models.CharField("可查看的项目", max_length=200, null=False, default='')


class UserToken(BaseTable):
    """
    用户登陆token
    """

    class Meta:
        verbose_name = "用户登陆token"
        db_table = "UserToken"

    user = models.OneToOneField(to=UserInfo, on_delete=models.CASCADE)
    token = models.CharField('token', max_length=50)

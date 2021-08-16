from django.http import JsonResponse
from rest_framework.permissions import BasePermission


# 用户类型：1-普通用户, 2-离职用户, 3-超级会员。
# 用户项目：项目ID:可见的项目内容范围

class VisitPermission(BasePermission):
    message = "访客没有基础权限，请联系管理员。"

    def has_permission(self, request, view):
        if request.user.project_field:
            return True
        return False


class AddPermission(BasePermission):
    message = "普通用户没有新增配置的权限"

    def has_permission(self, request, view):
        print("request:", request)
        if request.user.user_type == 1:
            return True
        return False
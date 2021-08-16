"""STL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from stlapp.views import project, report, permanagement

urlpatterns = [
    # 项目相关接口地址
    path('project/', project.ProjectView.as_view({
        "get": "list",
        "post": "add",
        "patch": "update",
        "delete": "delete"
    })),
    path('project/<int:pk>/', project.ProjectView.as_view({"get": "single"})),

    # 权限管理相关接口
    path('management/projectname/', permanagement.APIManagementView.as_view({"get": "getAllProjectName"})),
    path('management/username/', permanagement.APIManagementView.as_view({"get": "getAllUserName"})),
    path('management/type/', permanagement.APIManagementView.as_view({"get": "getUserType"})),
    path('management/change/', permanagement.APIManagementView.as_view({"post": "changeManagement"})),

    # 获取所有项目情况接口
    # path('projectstatus/', projectStatus.APIAllProjectView.as_view({"get": "getAllProjectStatus"})),

    # 报告地址
    path('reports/', report.ReportListView.as_view({
        "get": "list"
    })),

    path('reports/<int:pk>/', report.ReportView.as_view({
        "delete": "delete",
        "get": "look",
        # "get": "save_report"
    })),

]

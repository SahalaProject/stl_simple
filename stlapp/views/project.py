from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from stlapp import models, serializers
from STL import pagination
from rest_framework.response import Response
from stlapp.utils import response
# from stlapp.utils import prepare
from stlapp.utils.decorator import request_log


class ProjectView(GenericViewSet):
    """
    项目增删改查
    """

    queryset = models.Project.objects.all().order_by('-update_time')
    serializer_class = serializers.ProjectSerializer
    pagination_class = pagination.MyCursorPagination

    @method_decorator(request_log(level='DEBUG'))
    def list(self, request):
        """
        查询项目信息
        """
        field_message = request.user.project_field
        is_not_page = request.query_params.get('is_not_page')  # 克隆模态不分页查看所有项目

        try:
            if is_not_page:
                if field_message == 'all':
                    project_s = models.Project.objects.all().order_by('-create_time')
                else:
                    project_s = models.Project.objects.filter(id__in=eval(field_message)).order_by('-create_time')

                serializer_projects = serializers.ProjectSerializer(instance=project_s, many=True).data
                return Response({'results': serializer_projects})
            else:
                if field_message == 'all':
                    project_s = models.Project.objects.filter(id__in=eval(field_message)).order_by('-create_time')
                else:
                    project_s = models.Project.objects.filter(id__in=eval(field_message)).order_by('-create_time')
                page_projects = self.paginate_queryset(project_s)
        except:
            if field_message == 'all':
                projects = self.get_queryset()
                page_projects = self.paginate_queryset(projects)
            if not field_message:
                projects = models.Project.objects.filter(id__in=[])
                page_projects = self.paginate_queryset(projects)

        serializer = self.get_serializer(page_projects, many=True)
        return self.get_paginated_response(serializer.data)

    @method_decorator(request_log(level='INFO'))
    def add(self, request):
        """添加项目 {
            name: str
        }
        """
        if request.user.user_type != 3:
            return Response(response.PROJECT_CREATE_POWER)

        name = request.data["name"]

        if models.Project.objects.filter(name=name).first():
            response.PROJECT_EXISTS["name"] = name
            return Response(response.PROJECT_EXISTS)

        request.data["responsible"] = request.user.real_name

        # 反序列化
        serializer = serializers.ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            project = models.Project.objects.get(name=name)
            # prepare.project_init(project)
            return Response(response.PROJECT_ADD_SUCCESS)

        return Response(response.SYSTEM_ERROR)

    @method_decorator(request_log(level='INFO'))
    def update(self, request):
        """
        编辑项目
        """
        if request.user.user_type != 3:
            return Response(response.PROJECT_UPDATE_POWER)

        try:
            project = models.Project.objects.get(id=request.data['id'])
        except (KeyError, ObjectDoesNotExist):
            return Response(response.SYSTEM_ERROR)

        if request.data['name'] != project.name:
            if models.Project.objects.filter(name=request.data['name']).first():
                return Response(response.PROJECT_EXISTS)

        # 调用save方法update_time字段才会自动更新
        project.name = request.data['name']
        project.responsible = request.user.real_name
        project.desc = request.data['desc']
        project.save()

        return Response(response.PROJECT_UPDATE_SUCCESS)

    @method_decorator(request_log(level='INFO'))
    def delete(self, request):
        """
        删除项目
        """
        if request.user.user_type != 3:
            return Response(response.PROJECT_DELETE_POWER)
        try:
            project = models.Project.objects.get(id=request.data['id'])

            project.delete()

            return Response(response.PROJECT_DELETE_SUCCESS)
        except ObjectDoesNotExist:
            return Response(response.SYSTEM_ERROR)

    @method_decorator(request_log(level='INFO'))
    def single(self, request, **kwargs):
        """
        得到单个项目相关统计信息
        """
        pk = kwargs.pop('pk')

        field_message = request.user.project_field
        if (str(pk) in field_message) or (field_message == 'all'):
            try:
                queryset = models.Project.objects.get(id=pk)
            except ObjectDoesNotExist:
                return Response(response.PROJECT_NOT_EXISTS)

            serializer = self.get_serializer(queryset, many=False)
            # project_info = prepare.get_project_detail(pk)
            project_info = {}

            project_info.update(serializer.data)
            return Response(project_info)
        return Response(response.PROJECT_SINGLE_POWER)


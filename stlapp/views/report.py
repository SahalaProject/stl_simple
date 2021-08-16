import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
import os
from STL import pagination
from stlapp import models, serializers
from stlapp.utils import response
from stlapp.utils.decorator import request_log
from django.db.models import Q
from STL.settings import REPORT_ROOT


class ReportListView(GenericViewSet):
    """
    报告视图
    """
    queryset = models.Report.objects
    serializer_class = serializers.ReportSerializer
    pagination_class = pagination.MyPageNumberPagination

    @method_decorator(request_log(level='DEBUG'))
    def list(self, request):
        """报告列表
        """

        query_params = request.query_params
        project = query_params['project']
        search = query_params["search"]
        execution_type = query_params.get('execution_type', [1, 2, 3])
        execution_type_ = eval(execution_type) if isinstance(execution_type, str) else execution_type

        field_message = request.user.project_field
        if (project in field_message) or (field_message == 'all'):
            queryset = self.get_queryset().filter(project__id=project, execution_type__in=execution_type_).order_by('-update_time')
            if search != '':
                queryset = queryset.filter(Q(name__contains=search) | Q(execution_name=search))

            page_report = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page_report, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(response.REPORT_LOOK_POWER)

    @method_decorator(request_log(level='INFO'))
    def delete(self, request, **kwargs):
        """删除报告
        """
        """
           删除一个报告pk
           删除多个
           [{
               id:int
           }]
        """
        try:
            if kwargs.get('pk'):  # 单个删除
                models.Report.objects.get(id=kwargs['pk']).delete()
            else:
                for content in request.data:
                    reportobject = models.Report.objects.get(id=content['id'])
                    if reportobject.type != 4:
                        models.Report.objects.get(id=content['id']).delete()
                    else:
                        models.Report.objects.get(id=content['id']).delete()
                        report = json.loads(reportobject.summary)
                        path = '/var/www/html' + (report["stat"]['WebUIurl'].replace("http://8.129.223.219", ''))
                        os.remove(path)


        except:
            return Response(response.REPORT_NOT_EXISTS)

        return Response(response.REPORT_DEL_SUCCESS)

    @method_decorator(request_log(level='INFO'))
    def look(self, request, **kwargs):
        """查看报告
        """
        pk = kwargs["pk"]

        report = models.Report.objects.get(id=pk)
        summary = json.loads(report.summary, encoding="utf-8")
        summary["html_report_name"] = report.name
        return render_to_response('report_template.html', summary)


class ReportView(GenericViewSet):
    """
    报告视图
    """
    authentication_classes = ()
    permission_classes = ()
    queryset = models.Report.objects
    serializer_class = serializers.ReportSerializer
    pagination_class = pagination.MyPageNumberPagination

    @method_decorator(request_log(level='DEBUG'))
    def list(self, request):
        """报告列表
        """
        project = request.query_params['project']
        search = request.query_params["search"]
        queryset = self.get_queryset().filter(project__id=project).order_by('-update_time')
        if search != '':
            queryset = queryset.filter(name__contains=search)

        page_report = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page_report, many=True)
        return self.get_paginated_response(serializer.data)

    @method_decorator(request_log(level='INFO'))
    def delete(self, request, **kwargs):
        """删除报告
        """
        """
           删除一个报告pk
           删除多个
           [{
               id:int
           }]
        """
        try:
            if kwargs.get('pk'):  # 单个删除
                reportobject = models.Report.objects.get(id=kwargs['pk'])
                if reportobject.type != 4:
                    models.Report.objects.get(id=kwargs['pk']).delete()
                else:
                    models.Report.objects.get(id=kwargs['pk']).delete()
                    report = json.loads(reportobject.summary)
                    path = '/var/www/html' + (report["stat"]['WebUIurl'].replace("http://8.129.223.219", ''))
                    os.remove(path)
            else:
                for content in request.data:
                    models.Report.objects.get(id=content['id']).delete()

        except:
            return Response(response.REPORT_NOT_EXISTS)

        return Response(response.REPORT_DEL_SUCCESS)

    @method_decorator(request_log(level='INFO'))
    def look(self, request, **kwargs):
        """
        查看报告  分表 ReportSummary
        """
        pk = kwargs["pk"]
        report = models.Report.objects.filter(id=pk).first()

        project_info = models.Project.objects.filter(id=report.project_id).first()

        report_summary_ = models.ReportSummary.objects.filter(report_id=pk).first()  # 分表报告详情
        # 如果没有报告详情，默认展示report中summary, 兼容旧数据和默认数据，避免展示500页

        # 当存在本地报告summary时加载本地
        report_file = os.path.join(REPORT_ROOT, str(pk) + '.txt')
        if os.path.exists(report_file):
            with open(report_file, 'r', encoding='utf8')as fp:
                report_summary = fp.read()
        elif report_summary_:
            report_summary = report_summary_.summary
        else:
            report_summary = report.summary

        summary = json.loads(report_summary, encoding="utf-8")
        summary["html_report_name"] = report.execution_name if report.execution_name else report.name
        summary["html_project_name"] = project_info.name
        summary["html_project_id"] = report.project_id

        for i in range(len(summary["details"])):
            response_time = 0

            a = []
            for j in range(len(summary["details"][i]["records"])):
                a.append(summary["details"][i]["records"][j]["meta_data"]["response"]["response_time_ms"])
            for x in a:
                if x != 'N/A':
                    response_time = response_time + x
            summary["details"][i]["time"]["duration"] = response_time
            a = {}
            a["response_time_new"] = response_time
            summary["details"][i].update(a)

        summary["details"] = sorted(summary["details"], key=lambda e: e.__getitem__('response_time_new'), reverse=True)

        return render_to_response('report_template.html', summary)

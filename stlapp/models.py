from django.db import models

# Create your models here.
from stluser.models import BaseTable


class Project(BaseTable):
    """
    项目信息表
    """

    class Meta:
        verbose_name = "项目信息"
        db_table = "Project"

    name = models.CharField("项目名称", unique=True, null=False, max_length=100)
    desc = models.CharField("简要介绍", max_length=100, null=False)
    responsible = models.CharField("创建人", max_length=20, null=False)


class Report(BaseTable):
    """
    报告存储
    """
    report_type = (
        (1, "调试"),
        (2, "异步"),
        (3, "定时"),
        (4, "WebUI")
    )

    class Meta:
        verbose_name = "测试报告"
        db_table = "Report"

    name = models.CharField("报告名称", null=False, max_length=100)
    type = models.IntegerField("报告类型", choices=report_type)
    summary = models.TextField("主体信息", null=False)  # 只存储列表显示内容，具体详情在分表 Summary
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    executor_name = models.CharField("执行人", default='', max_length=50, null=True)
    execution_name = models.CharField(verbose_name='报告所属的api/case/task名称', default='null', max_length=100)
    execution_id = models.IntegerField(verbose_name='报告所属的api/case/task的id', default=0)
    execution_type = models.IntegerField(verbose_name="报告所属的api/case/task的类型", default=0, choices=((0, 'Task'), (1, 'Api'), (2, 'Case'), (3, '公共Case'), (4, '失败重试'), (5, 'CICD任务')))
    run_status = models.IntegerField(verbose_name='运行状态', default=0, choices=((0, '运行中'), (1, '已完成')))


class ReportSummary(BaseTable):
    """报告的-报告详情 分表"""
    class Meta:
        verbose_name = "报告详情"
        db_table = "reportsummary"

    summary = models.TextField("主体信息", null=False)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)



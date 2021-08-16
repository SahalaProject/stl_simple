# -*- coding: utf-8 -*-
from rest_framework.viewsets import GenericViewSet
from stlapp import models
from stluser.models import UserInfo
from rest_framework.response import Response
from stlapp.utils import response
from STL.settings import BASE_DIR
import json

class APIManagementView(GenericViewSet):
    """
    API操作视图
    """

    def getAllProjectName(self, request):
        if request.user.user_type > 2:
            params = request.query_params
            uid = params["uid"]
            projectnameobj = models.Project.objects.values('name', "id")
            user_have = UserInfo.objects.filter(pk=uid).first().project_field
            # print(user_have.project_field)
            # user_have = list(user_have.project_field)
            user_havelist = json.loads(user_have)
            # print(user_havelist)
            projectnamelist = []
            response_dic = {}
            for i in projectnameobj:
                nonedict = {}
                nonedict['code'] = i["id"]
                nonedict['name'] = i["name"]
                projectnamelist.append(nonedict)
            response_dic["projectallname"] = projectnamelist
            response_dic["user_have"] = user_havelist
            response.MANAGEMENT_GET_SUCCESS['msg'] = response_dic
            return Response(response.MANAGEMENT_GET_SUCCESS)
        else:
            return Response(response.CONFIG_UPDATE_POWER)

    def getAllUserName(self, request):
        if request.user.user_type > 2:
            params = request.query_params
            usernameobj = UserInfo.objects.values("real_name", "id")
            usernamelist = []
            response_dic = {}
            for i in usernameobj:
                if i["real_name"] is not None:
                    nonedict = {}
                    nonedict['code'] = i["id"]
                    nonedict['name'] = i["real_name"]
                    usernamelist.append(nonedict)
            # response_dic["allusername"] = list(set(usernamelist))
            response_dic["allusername"] = usernamelist
            response.MANAGEMENT_GET_SUCCESS['msg'] = response_dic
            return Response(response.MANAGEMENT_GET_SUCCESS)
        else:
            return Response(response.CONFIG_UPDATE_POWER)


    def changeManagement(self, request):
        if request.user.user_type > 2:
            try:
                usernamecode = request.data['usernamecode']
                projectcode = request.data['projectcode']
                usercode = request.data['usercode']
            except:
                return Response(response.MANAGEMENT_POST_FAIL)
            if usernamecode == '' or projectcode == '' or projectcode == [] or usercode == '':
                return Response(response.MANAGEMENT_POST_FAIL)
            if int(usercode) == 3 and request.user.user_type != 3:
                return Response(response.CONFIG_UPDATE_POWER)
            userobj = UserInfo.objects.get(id=usernamecode)
            userobj.user_type = usercode
            userobj.project_field = json.dumps(projectcode)
            userobj.save()
            return Response(response.MANAGEMENT_POST_SUCCESS)

    def getUserType(self, request):
        params = request.query_params
        type = request.user.user_type
        response.MANAGEMENT_GET_SUCCESS['msg'] = type
        return Response(response.MANAGEMENT_GET_SUCCESS)
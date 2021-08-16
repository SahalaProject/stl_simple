PROJECT_ADD_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": "项目添加成功"
}

MANAGEMENT_GET_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": ""
}

MANAGEMENT_POST_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "权限管理更新成功"
}

MANAGEMENT_POST_FAIL = {
    "code": "0102",
    "success": False,
    "msg": "权限管理更新失败"
}

PROJECT_EXISTS = {
    "code": "0101",
    "success": False,
    "msg": "项目已存在"
}

PROJECT_NOT_EXISTS = {
    "code": "0102",
    "success": False,
    "msg": "项目不存在"
}

DEBUGTALK_NOT_EXISTS = {
    "code": "0102",
    "success": False,
    "msg": "miss debugtalk"
}

DEBUGTALK_UPDATE_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "debugtalk更新成功"
}

PROJECT_UPDATE_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "项目更新成功"
}

PROJECT_DELETE_SUCCESS = {
    "code": "0003",
    "success": True,
    "msg": "项目删除成功"
}

SYSTEM_ERROR = {
    "code": "9999",
    "success": False,
    "msg": "System Error"
}

TREE_ADD_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": "树形结构添加成功"
}

TREE_UPDATE_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "树形结构更新成功"
}


KEY_MISS = {
    "code": "0100",
    "success": False,
    "msg": "请求数据非法"
}

LOG_MISS = {
    "code": "0100",
    "success": False,
    "msg": "日志不存在"
}

FILE_UPLOAD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '文件上传成功'
}

FILE_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '文件已存在,默认使用已有文件'
}

API_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '接口添加成功'
}

DATA_TO_LONG = {
    'code': '0100',
    'success': False,
    'msg': '数据信息过长！'
}

API_NOT_FOUND = {
    'code': '0102',
    'success': False,
    'msg': '未查询到该API'
}

API_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': 'API删除成功'
}

REPORT_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': '报告删除成功'
}

API_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': 'API更新成功'
}

SUITE_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': 'Suite添加成功'
}

SUITE_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': 'Suite删除成功'
}

CASE_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '用例添加成功'
}

CASE_MOVE_SUCCESS = {
    'code': '200101',
    'success': True,
    'msg': '用例移动成功'
}

AI_CASE_ADD_SUCCESS = {
    'code': '60001',
    'success': True,
    'msg': '智能生成用例成功'
}

AI_CASE_ADD_FAIL = {
    'code': '60002',
    'success': False,
    'msg': '无参的API不需要生成用例'
}


API_SEARCH_FAIL = {
    'code': '60003',
    'success': False,
    'msg': 'swagger地址和API不匹配'
}


CASE_EXISTS = {
    "code": "0101",
    "success": False,
    "msg": "此节点下已存在该用例集,请重新命名"
}

CASE_NOT_EXISTS = {
    "code": "0102",
    "success": False,
    "msg": "此用例集不存在"
}

CASE_DELETE_SUCCESS = {
    "code": "0003",
    "success": True,
    "msg": "用例集删除成功"
}

CASE_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '用例集更新成功'
}

CONFIG_EXISTS = {
    "code": "0101",
    "success": False,
    "msg": "此配置已存在，请重新命名"
}

VARIABLES_EXISTS = {
    "code": "0101",
    "success": False,
    "msg": "此变量已存在，请重新命名"
}

VARIABLES_SETFAILES = {
    "code": "0101",
    "success": False,
    "msg": "此变量值无法转换为对应类型"
}

CONFIG_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '环境添加成功'
}

VARIABLES_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '变量添加成功'
}

CONFIG_NOT_EXISTS = {
    "code": "0102",
    "success": False,
    "msg": "指定的环境不存在"
}

REPORT_NOT_EXISTS = {
    "code": "0102",
    "success": False,
    "msg": "指定的报告不存在"
}

VARIABLES_NOT_EXISTS = {
    "code": "0102",
    "success": False,
    "msg": "指定的全局变量不存在"
}

CONFIG_UPDATE_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "环境更新成功"
}

VARIABLES_UPDATE_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "全局变量更新成功"
}

TASK_ADD_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": "定时任务新增成功"
}

TASK_TIME_ILLEGAL = {
    "code": "0101",
    "success": False,
    "msg": "时间表达式非法"
}

TASK_HAS_EXISTS = {
    "code": "0102",
    "success": False,
    "msg": "定时任务已存在"
}

TASK_EMAIL_ILLEGAL = {
    "code": "0102",
    "success": False,
    "msg": "请指定邮件接收人列表"
}

TASK_DEL_SUCCESS = {
    "code": "0003",
    "success": True,
    "msg": "任务删除成功"
}

PLAN_DEL_SUCCESS = {
    "code": "0003",
    "success": True,
    "msg": "集成计划删除成功"
}

PLAN_ADD_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": "计划添加成功"
}

PLAN_KEY_EXIST = {
    "code": "0101",
    "success": False,
    "msg": "该KEY值已存在，请修改KEY值"
}

PLAN_ILLEGAL = {
    "code": "0101",
    "success": False,
    "msg": "提取字段格式错误，请检查"
}

PLAN_UPDATE_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "计划更新成功"
}

HOSTIP_EXISTS = {
    "code": "0101",
    "success": False,
    "msg": "此域名已存在，请重新命名"
}

HOSTIP_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '域名添加成功'
}

HOSTIP_NOT_EXISTS = {
    "code": "0102",
    "success": False,
    "msg": "指定的域名不存在"
}


HOSTIP_UPDATE_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "域名更新成功"
}
HOST_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': '域名删除成功'
}


PROJECT_UPDATE_POWER = {
    "code": "010001",
    "success": False,
    "msg": "当前用户没有编辑的权限"
}

PROJECT_DELETE_POWER = {
    "code": "010002",
    "success": False,
    "msg": "当前用户没有删除的权限"
}

PROJECT_CREATE_POWER = {
    "code": "010003",
    "success": False,
    "msg": "该用户无创建项目的权限，请联系管理员"
}

CONFIG_CREATE_POWER = {
    "code": "011003",
    "success": False,
    "msg": "该用户无新增配置的权限，请联系管理员"
}

CONFIG_UPDATE_POWER = {
    "code": "011003",
    "success": False,
    "msg": "用户无更新配置的权限，请联系管理员"
}


PROJECT_LOOK_POWER = {
    "code": "010004",
    "success": False,
    "msg": "当前用户没有查看项目的权限"
}

PROJECT_SINGLE_POWER = {
    "code": "010005",
    "success": False,
    "msg": "当前用户没有查看单个项目的权限"
}

DEBUGTALK_LOOK_POWER = {
    "code": "020000",
    "success": False,
    "msg": "当前用户没有查看debugtalk的权限"
}

DEBUGTALK_SAVE_POWER = {
    "code": "020001",
    "success": False,
    "msg": "当前用户没有修改debugtalk的权限"
}


TREE_LOOK_POWER = {
    "code": "030001",
    "success": False,
    "msg": "当前用户没有查看tree的权限"
}

TREE_UPDATE_POWER = {
    "code": "030002",
    "success": False,
    "msg": "没有更新树形结构的权限"
}


API_LOOK_POWER = {
    "code": "040001",
    "success": False,
    "msg": "当前用户没有查看api的权限"
}


SUITE_LOOK_POWER = {
    "code": "050001",
    "success": False,
    "msg": "当前用户没有查看suite的权限"
}

CONFIG_LOOK_POWER = {
    "code": "060001",
    "success": False,
    "msg": "当前用户没有查看配置的权限"
}

CONFIG_ADD_POWER = {
    "code": "060002",
    "success": False,
    "msg": "当前用户没有增加配置的权限"
}


VARIABLES_LOOK_POWER = {
    "code": "070001",
    "success": False,
    "msg": "当前用户没有查看变量的权限"
}

HOST_LOOK_POWER = {
    "code": "080001",
    "success": False,
    "msg": "当前用户没有查看host的权限"
}

REPORT_LOOK_POWER = {
    "code": "090001",
    "success": False,
    "msg": "当前用户没有查看报告的权限"
}

TASK_LOOK_POWER = {
    "code": "100001",
    "success": False,
    "msg": "当前用户没有查看任务的权限"
}

LOCUST_RUN_POWER = {
    "code": "110001",
    "success": True,
    "msg": "当前用户没有执行性能locust的权限"
}

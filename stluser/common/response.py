KEY_MISS = {
    "code": "0100",
    "success": False,
    "msg": "请求数据非法"
}

REGISTER_USERNAME_EXIST = {
    "code": "0101",
    "success": False,
    "msg": "用户名已被注册"
}

REGISTER_EMAIL_EXIST = {
    "code": "0101",
    "success": False,
    "msg": "邮箱已被注册"
}

SYSTEM_ERROR = {
    "code": "9999",
    "success": False,
    "msg": "System Error"
}

REGISTER_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": "register success"
}

FIND_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": "密码修改成功"
}

FIND_NOT_EXISTS = {
    "code": "0001",
    "success": False,
    "msg": "用户不存在，请检查用户名"
}

LOGIN_FAILED = {
    "code": "0103",
    "success": False,
    "msg": "用户名或密码错误"
}

USER_NOT_EXISTS = {
    "code": "0104",
    "success": False,
    "msg": "该用户未注册"
}

MODPWD_FAILED = {
    "code": "0105",
    "success": False,
    "msg": "旧密码错误"
}

LOGIN_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": "login success"
}

RUN_KEY_MISS = {
    "code": "010001",
    "success": False,
    "msg": "触发请求数据非法"
}


RUN_SUCCESS = {
    "code": "010002",
    "success": True,
    "msg": "触发定时任务成功！"
}

RUN_UI_SUCCESS = {
    "code": "010003",
    "success": True,
    "msg": "新增执行WEB-UI自动化成功，请勿多次请求！！！"
}


RUN_PROJECT_MISS = {
    "code": "010004",
    "success": False,
    "msg": "该项目id不存在web-ui测试"
}

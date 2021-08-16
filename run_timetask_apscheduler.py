# coding:utf-8

# auther: liyubin

import os
import time
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

host = 'http://127.0.0.1:80'  # 后台接口host
username = 'timetask'  # 独立定时触发账号
password = '111111'


def backup_mysql():
    """备份mysql数据库"""
    if os.path.exists('/home'):
        folder = os.path.join('/home', 'mysql_backup')
        folder if os.path.exists(folder) else os.makedirs(folder)
    else:
        folder = './media'
    backup_name = os.path.join(folder, 'stl_backup_' + str(time.strftime("%Y%m%d%H%M")) + '.sql')
    # code = 'mysql -uw -p123456  stl < {0}'.format(backup_name)  # 全还原 不报错
    code = 'mysqldump -uw -p123456 --databases stl > {0}'.format(backup_name)  # 全备份
    print('备份mysql数据库: ', backup_name)
    os.system(code)


def job():
    """时间间隔 触发 定时任务"""
    # 登录获取token
    url_login = host + '/api/user/login/'
    json_login = {"username": username, "password": password}
    res_login = requests.post(url=url_login, json=json_login)
    token = res_login.json().get('token') if res_login.status_code == 200 else '获取token失败'

    # 触发定时任务
    url_task = host + '/api/stl/task_run/'
    res_run_task = requests.get(url_task, headers={'Authorization': token})
    msg = res_run_task.json() if res_run_task.status_code == 200 else '触发定时任务异常'

    print('Apscheduler触发: {0}, {1}'.format(msg, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', seconds=50)  # 时间间隔过短会导致重复下发任务
# scheduler.add_job(backup_mysql, 'cron', day_of_week='0, 1, 2, 3, 4, 5, 6', hour=1, minute=20)  # 定时备份mysql数据库
scheduler.start()



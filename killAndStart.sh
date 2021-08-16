source /etc/profile
cd /www/wwwroot/STL

ps -ef | grep run_timetask_apscheduler.py | grep -v grep | awk '{print $2}' | xargs kill -9

nohup python3.6 manage.py runserver 192.168.87.81:5000 > /www/wwwroot/STL/logs/server8000.log 2>&1 &

nohup python3.6 run_timetask_apscheduler.py > /www/wwwroot/STL/logs/run_timetask_apscheduler.log 2>&1 &
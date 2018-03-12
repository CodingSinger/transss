

import datetime

import os

from TestBootStrap import testStart

now = datetime.datetime.now()

last_test = datetime.datetime.fromtimestamp(os.stat("data/schestat.log").st_mtime)

if last_test < now + datetime.timedelta(days=-1):
    #如果上次测试时间距离现在超过一天则启动
    testStart()








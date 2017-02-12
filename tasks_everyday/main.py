# coding=utf-8

import itertools
import json
import time
import uuid
# from logging import getLogger
from random import randint
from threading import Timer

import util
from xiami import xiami

# log = getLogger(__name__)

TASK_SAVE_PATH = './local/task.json'


class Task(object):

    def __init__(self, hour, min, func, args=(), workday=False, holiday=False, pause_days=0, id=None):
        self.func = func  # 类型或函数
        self.args = tuple(args)
        self.hour = hour
        self.min = min
        self.workday = workday
        self.holiday = holiday
        self.pause_days = pause_days
        self.id = str(uuid.uuid4()) if not id else id

    def __repr__(self):
        return self.func.__name__
        # return str(self.__dict__) if self.type in task_types else '<PreTask_%s>' % self.type

    # def to_dict(self, include_id=False):
    #     if self.type not in task_types:
    #         return None
    #     d = self.__dict__.copy()
    #     if not include_id:
    #         del d['id']
    #     return d


def auto_check_in():
    # sleep_secs = randint(0, 1800)
    # log.info(u'将在%d秒后进行虾米签到。' % sleep_secs)
    # time.sleep(sleep_secs)    
    try:
        x = xiami()
        ret = x.check_in()
        if ret:
            util.sendEmail('hyiit@qq.com', u'虾米签到失败', ret)
    except Exception, ex:
        util.sendEmail('hyiit@qq.com', u'虾米签到失败', ex)



tasks = [  # Task(7, 35, alarm_song, (),workday=True),
    # Task(7, 43, tell_weather, (),workday=True),
    # Task(7, 50, tell_time_every_10min, (),workday=True),
    #
    # Task(8, 45, tell_weather, (),holiday=True),
    # Task(9, 45, tell_weather, (False,True),holiday=True),

    Task(18, 56, auto_check_in, (), workday=True, holiday=True),
]


def start_tasks():
    print(u"程序开始运行")
    

    while True:        
        t = time.localtime()
        # wd = tell_time.is_workday(t)
        # # [7, 8] + list(range(19, 24)) if wd else [0] + list(range(8, 24))
        # time_range = tell_time.tell_range
        # if t.tm_hour in time_range:
        #     tell_time.tell_time(t)

        # f_tks = filter(lambda tk: tk.workday if wd else tk.holiday, tasks)

        for task in tasks:
            if t.tm_hour == task.hour and task.min >= t.tm_min:
                func = task.func
                if task.pause_days == 0:
                    interval = (task.min - t.tm_min) * 60 - t.tm_sec
                    interval = max(0, interval)
                    print(u"将在%s秒后执行任务：%s。|%s。" %
                             (interval, func.__name__, task))
                    Timer(interval, func, task.args).start()
                elif task.pause_days > 0:
                    task.pause_days -= 1
                    print(u"今日不执行任务‘%s’，将于%s日后执行。|%s。" %
                             (func.__name__, task.pause_days, task))
                else:
                    print(u"任务‘%s’已停止。|%s。" % (func.__name__,  task))
        
        t = time.localtime()        
        time.sleep(3600 - t.tm_min * 60 - t.tm_sec)


if __name__ == '__main__':
    start_tasks()
    # auto_check_in()

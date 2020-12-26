# -*- coding:utf-8 -*-
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import time

stop_flag = 0

def timer(n):
    while True:
        if stop_flag == 1:
            break
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(n)

class myscheduler(object):
    def __init__(self):
        self.scheduler = BlockingScheduler()

    def timer_callback(self, message):
        global stop_flag
        print(message)
        stop_flag = 1

    def start_timing(self,message,timeout):
        self.scheduler.add_job(func=self.timer_callback,args=[message],trigger="date",run_date=datetime.datetime.now()+datetime.timedelta(seconds=timeout))
        self.scheduler.start()

    def stop_timing(self):
        self.scheduler.shutdown()

if __name__ == '__main__':
    myscheduler = myscheduler()
    thread = threading.Thread(target=myscheduler.start_timing,args=["timeout!!!", 10])
    thread.start()
    timer(2)
    myscheduler.stop_timing()    

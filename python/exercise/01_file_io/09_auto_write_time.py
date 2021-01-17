"""
write time every 2 seconds
"""

import time

f = open('20210117_time.txt','a+')

f.seek(0,0)
n = 0

for line in f: # file offset will auto update after this command
    n += 1

while True:
    n += 1
    time.sleep(2)
    s = "%d. %s\n"%(n,time.ctime())
    print(s)
    f.write(s)
    f.flush()

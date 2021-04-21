import os
import time

flog = open(strftime("%Y%m%d%H%M%S", time.localtime()) + '.txt', a)

flog.write('aabbc' + '\n')
flog.flush()
os.rsync(flog.fileno())

flog.close()

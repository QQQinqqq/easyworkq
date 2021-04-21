import os
import time

flog = open(time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.txt', 'a')

flog.write('aabbc' + '\n')
flog.flush()
os.fsync(flog.fileno())

flog.close()

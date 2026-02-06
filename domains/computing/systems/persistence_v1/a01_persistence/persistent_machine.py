import os
import time

my_pid= os.getpid()
while True:
    print(my_pid)
    time.sleep(1)
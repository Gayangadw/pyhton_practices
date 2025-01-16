#How to get the time of pyhton program execution

import time
def myFuntion():
    start_time = time.time()
    s=0
    for i in range (1,n+1):
        s+=s
        end_time=time.time()
        return s,end_time-start_time
n=5
print(myFuntion())

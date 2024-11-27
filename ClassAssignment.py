#wap to estimate runtime of all the functions you have used so far

import time as t
from functionScope import add as fn1
from functionScope import sub as fn2


def timeFunction(func,*args,**kwargs):#wraper
    startTime=t.time()
    res = func(args,kwargs)
    endTime= t.time()
    runTimeInSec = endTime - startTime
    print(f"\n time to execute function is{runTimeInSec*1000000} micro seconds")

a=1
b=2
timeFunction(fn1,a,b)
timeFunction(fn2,a,b)

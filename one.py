import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
mori="morteza"
import re
import subprocess
from subprocess import PIPE, Popen
arr=[]
def ping(a):
    process = Popen(['ping', '-c','1','time.ir'],stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    x=re.search("time=(?P<time>[0-9]{1,5})" , str(out))

    arr.append(x.groupdict()['time'])
    mori=33
    

    if len(arr) > 10:
        arr.pop(0)
    plt.cla()
    plt.plot(arr)
    plt.xlim(-1,11) 
    plt.ylim(0,30)
    plt.ylabel("mori is best")
    plt.title("and the best")
    
ani=animation.FuncAnimation(plt.gcf(), ping, interval=1000)





plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import re
import subprocess
from subprocess import PIPE, Popen


f,ex=plt.subplots(2,2)
ex[1][1].plot([1,1,1],[2,2,2])
ex[1][1].set_title("hi")

f2,ex2=plt.subplots(2,3)

ex2[0][2].plot([1,2,3,4],[0,2,5,3])
ex2[0][2].set_title("bee")
ex2[0][2].set_xticks([1,1.5,2,2.8])
ex2[0][2].set_xticklabels(["m","s",2,2.4])
ex2[0][2].set_xlim(-2,10)


ex2[0][2].set_ylim(-2,5)
plt.show()

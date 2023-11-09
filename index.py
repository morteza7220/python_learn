from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.animation as animation
import numpy as np
import re
import subprocess
from subprocess import PIPE, Popen

root=Tk()
root.geometry("900x700")
root.configure(background="gray")
##############Frames#######################################
top_frame=Frame(root, bg="black")
top_frame.pack(side="top",fill=X, ipadx=10,ipady=10)
top_frame.grid_propagate(False)

main_frame=Frame(root, bg="blue")
main_frame.pack(side="top",fill=X, ipadx=10,ipady=10)

left_frame=Frame(main_frame, bg="green")
left_frame.pack(side="left",fill=Y,anchor=N, ipadx=10,ipady=10, pady=10)


right_frame=Frame(main_frame, bg="yellow")
right_frame.pack(side="left",expand=True,fill=X, ipadx=10,ipady=10)
############################################################
fig,ex=plt.subplots()
ex.plot([1,2,3],[3,1,3])
canvas=FigureCanvasTkAgg(fig, master=right_frame)
canvas.get_tk_widget().pack()

arr_of_ping_time=[]
def ping(a):
    process = Popen(['ping', '-c','1','time.ir'],stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    x=re.search("time=(?P<time>[0-9]{1,5})" , str(out))

    arr_of_ping_time.append(x.groupdict()['time'])
    
    if len(arr_of_ping_time) > 100:
        arr_of_ping_time.pop(0)
    plt.cla()
    plt.plot(arr_of_ping_time)
    # plt.xlim(-1,11) 
    plt.ylim(0,30)
    plt.ylabel("mori is best")
    plt.title("and the best")
    
ani=animation.FuncAnimation(plt.gcf(), ping, interval=1000)


# plt.plot([2,3,4,5],[1,2,3,1])


canvas.draw()
#######################  Label Public ip #########################################
label_for_public_ip=Label(right_frame,text="...........",font=("arial",16,"bold"))
label_for_public_ip.pack()
import requests
try:
    
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
except:
    pass
try:

	label_for_public_ip.configure(text="public ip:\n"+ip)
except:
	label_for_public_ip.configure(text="you\'re not connected to internet")
##################################################################################





############################## Ping #####################Text=1,  Label=2,  btn=1, function=1############
text_inter_ip=Text(right_frame,height=1,width=30,font=("arial",22))
text_inter_ip.pack()

label_for_ping_result=Label(right_frame,text="ارسال شده:\nدریافت شده:\nزمان")
label_for_ping_result.pack()

label_for_ping_result_full=Label(right_frame,text="ارسال شده:\nدریافت شده:\nزمان")
label_for_ping_result_full.pack(side="bottom")

import subprocess
import re
def go_ping():
	ip_1=text_inter_ip.get("1.0","end-1c")
	ccc=subprocess.Popen(["ping","-n","4",ip_1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out,err= ccc.communicate()
	label_for_ping_result_full.config(text=out)
	if re.search("Received = 1", str(out)):
		received=1
	else:
		received=0		
	aaa=re.search("time=(?P<time>[0-9]*).*Sent = (?P<sent>[0-1])", str(out))
	
	if aaa:
		time=aaa.groupdict()['time']
		sent=aaa.groupdict()['sent']
	if  received == 1:
		label_for_ping_result.configure(bg="green")
	else:
		label_for_ping_result.configure(bg="red")
	if aaa and time:	
		label_for_ping_result.configure(text="ارسال شده:"+sent+" 1\nدریافت شده:"+str(received)+"\nزمان\n"+time)
	elif re.search("Request timed out",str(out)):
		label_for_ping_result.configure(text="request timed out")
	elif re.search("could not find host",str(out)):
		label_for_ping_result.configure(text="could not find dest")

btn_ping=Button(right_frame,text="ping",command=go_ping)
btn_ping.pack()
##################################################################################




#######################  Label Local ip #########################################
lablel_show_local_ip=Label(left_frame,text="...........",font=("arial",16,"bold"))
lablel_show_local_ip.pack()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
except:
    pass
try:
	lablel_show_local_ip.configure(text="you\'re local ip:\n"+s.getsockname()[0])
except:
	lablel_show_local_ip.configure(text="error while geting local ip")	
s.close()
##################################################################################



import psutil
addrs = psutil.net_if_addrs()
print(addrs.keys())


#from PIL import *
#from PIL import Image as II
#import PIL as ppp
#mm=II.open("nature1.jpg")
#img = PhotoImage(file=mm)

#panel = Image(root,image=img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")




root.mainloop()

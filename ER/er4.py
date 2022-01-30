
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER




ER4 = ER("ER4","JEMF4","JEM",1,1)
def startER4():
    while True:
        ER4.add_HS()
        if int(ER4.HS_count) > 5: ER4.HS_count = 0
        time.sleep(1)  

def starter4AAA():
    while True:
        ER4.add_HS()
        if int(ER4.HS_count) > 5: ER4.HS_count = 0
        time.sleep(1)  

def er4afc2flow(out_q):
	while True:
		# Produce some data
		hs_mon = ER4.AFC_2['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er4afc2flowmon(in_q):

    while True:
        # Get some data
        data4 = in_q.get()
        #if int(data4) == 3:
            #print(f"{ER4.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER4.rack_id} HS : {data4}")
        if data4 < 25: print('Low AFC2')
        else: print(f"{ER4.rack_id} AFC2 Flow speed : {data4} kg/hr")
        

def er4hs(out_q):
	while True:
		# Produce some data
		hs_mon = ER4.HS_count
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er4hsmon(in_q):

    while True:
        # Get some data
        data4 = in_q.get()
        if int(data4) == 3:
            print(f"{ER4.rack_id} value is 3")
        # Process the data
        else: print(f"{ER4.rack_id} HS : {data4}")

def er4AAA(out_q):
    aaa_mon = ER4.AAA['speed']
    out_q.put(aaa_mon);time.sleep(1)

def er4AAAmon(in_q):
    while True:
        aaa4 = in_q.get()
        if aaa4 < 28000 : print('ER4 Fan Spped Low');time.sleep(0.5)
        else: print(f"{ER4.rack_id} AAA Fan Speed : {aaa4}")

#print(ER4.AFC_2['speed'])
time.sleep(1)
q_er4aaa = Queue()
er4aaa = Thread(target=starter4AAA)

q_er4afc2 = Queue()
er4_afc2_flow = Thread(target=er4afc2flow)
#er4_afc2_flow.start()

q_er4HS = Queue()
er4HS = Thread(target=startER4)
#er4HS.start()




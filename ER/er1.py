
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER




ER1 = ER("ER1","LABO2","LAB",1,1)

def startER1():
    while True:
        ER1.add_HS()
        if int(ER1.HS_count) > 5: ER1.HS_count = 0
        time.sleep(1)  

def starter1AAA():
    while True:
        ER1.add_HS()
        if int(ER1.HS_count) > 5: ER1.HS_count = 0
        time.sleep(1) 

def startafc2():
    while True:
        ER1.er_afc2_speed 

def er1afc2flow(out_q):
	while True:
		# Produce some data
		hs_mon = ER1.AFC_2['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er1afc2flowmon(in_q):

    while True:
        # Get some data
        data1 = in_q.get()
        #if int(data1) == 3:
            #print(f"{ER1.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER1.rack_id} HS : {data1}")
        if data1 < 25: print('Low AFC2')
        else: print(f"{ER1.rack_id} AFC2 Flow speed : {data1} kg/hr")
        

def er1hs(out_q):
	while True:
		# Produce some data
		hs_mon = ER1.HS_count
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er1hsmon(in_q):

    while True:
        # Get some data
        data1 = in_q.get()
        if int(data1) == 3:
            print(f"{ER1.rack_id} value is 3")
        # Process the data
        else: print(f"{ER1.rack_id} HS : {data1}")

def er1AAA(out_q):
    aaa_mon = ER1.AAA['speed']
    out_q.put(aaa_mon);time.sleep(1)

def er1AAAmon(in_q):
    while True:
        aaa1 = in_q.get()
        if aaa1 < 28000 : print('ER1 Fan Spped Low');time.sleep(0.5)
        else: print(f"{ER1.rack_id} AAA Fan Speed : {aaa1}")

#print(ER1.AFC_2['speed'])
time.sleep(1)
q_er1aaa = Queue()
er1aaa = Thread(target=starter1AAA)

q_er1afc2 = Queue()
er1_afc2_flow = Thread(target=startafc2)
#er1_afc2_flow.start()

q_er1HS = Queue()
er1HS = Thread(target=startER1)
#er1HS.start()

ER1.SSPCM_Init()





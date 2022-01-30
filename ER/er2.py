
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER




ER2 = ER("ER2","LABO1","LAB",1,1)

def startER2():
    while True:
        ER2.add_HS()
        if int(ER2.HS_count) > 5: ER2.HS_count = 0
        time.sleep(1)  

def starter2AAA():
    while True:
        ER2.add_HS()
        if int(ER2.HS_count) > 5: ER2.HS_count = 0
        time.sleep(1)  

def er2afc2flow(out_q):
	while True:
		# Produce some data
		hs_mon = ER2.AFC_2['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er2afc2flowmon(in_q):

    while True:
        # Get some data
        data2 = in_q.get()
        #if int(data2) == 3:
            #print(f"{ER2.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER2.rack_id} HS : {data2}")
        if data2 < 25: print('Low AFC2')
        else: print(f"{ER2.rack_id} AFC2 Flow speed : {data2} kg/hr")
        

def er2hs(out_q):
	while True:
		# Produce some data
		hs_mon = ER2.HS_count
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er2hsmon(in_q):

    while True:
        # Get some data
        data2 = in_q.get()
        if int(data2) == 3:
            print(f"{ER2.rack_id} value is 3")
        # Process the data
        else: print(f"{ER2.rack_id} HS : {data2}")

def er2AAA(out_q):
    aaa_mon = ER2.AAA['speed']
    out_q.put(aaa_mon);time.sleep(1)

def er2AAAmon(in_q):
    while True:
        aaa2 = in_q.get()
        if aaa2 < 28000 : print('ER2 Fan Spped Low');time.sleep(0.5)
        else: print(f"{ER2.rack_id} AAA Fan Speed : {aaa2}")

#print(ER2.AFC_2['speed'])
time.sleep(1)
q_er2aaa = Queue()
er2aaa = Thread(target=starter2AAA)

q_er2afc2 = Queue()
er2_afc2_flow = Thread(target=er2afc2flow)
#er2_afc2_flow.start()

q_er2HS = Queue()
er2HS = Thread(target=startER2)
#er2HS.start()





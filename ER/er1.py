
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER




ER1 = ER("ER1","LABO2","LAB")

def startER1():
    while True:
        ER1.add_HS()
        if int(ER1.HS_count) > 5: ER1.HS_count = 0
        time.sleep(1)

def er1speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER1.AFC_2['speed']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er1speedmon(in_q):

    while True:
        # Get some data
        data1 = in_q.get()
        #if int(data1) == 3:
            #print(f"{ER1.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER1.rack_id} HS : {data1}")
        if data1 < 28000 : print('ER1 Fan Spped Low');time.sleep(0.5)
        else: print(f"{ER1.rack_id} AAA Fan Speed : {data1}")

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

#print(ER1.AFC_2['speed'])
time.sleep(1)
q_er1aaa = Queue()
er1speed1 = Thread(target=ER1.tt)
er1speed1.start()

q_er1HS = Queue()
er1HS = Thread(target=startER1)
er1HS.start()





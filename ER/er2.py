
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER




ER2 = ER("ER2","LABO1","LAB")

def startER2():
    while True:
        ER2.add_HS()
        if int(ER2.HS_count) > 5: ER2.HS_count = 0
        time.sleep(1)

def er2speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER2.AFC_2['speed']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er2speedmon(in_q):

    while True:
        # Get some data
        data2 = in_q.get()
        #if int(data1) == 3:
            #print(f"{ER1.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER1.rack_id} HS : {data1}")
        if data2 < 28000 : print('ER2 Fan Spped Low');time.sleep(0.5)
        else: print(f"{ER2.rack_id} AAA Fan Speed : {data2}")

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

time.sleep(1)
q_er2aaa = Queue()
er2speed1 = Thread(target=ER2.tt)
er2speed1.start()

q_er2HS = Queue()
er2HS = Thread(target=startER2)
er2HS.start()






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

def startER2afc1():
    while True:
        ER2.er_afc1speed_gen()
        time.sleep(1)

def startER2afc2():
    while True:
        ER2.er_afc2speed_gen()
        time.sleep(1)

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
        #if int(data2) == 3:
         #   print(f"{ER2.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER2.rack_id} HS : {data2}")

def er2aaaspeed(out_q):
	while True:
		# Produce some data
		hs_mon = ER2.AAA['speed']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er2aaaspeedmon(in_q):

    while True:
        # Get some data
        data2 = in_q.get()
        #if int(data2) == 3:
            #print(f"{ER2.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER2.rack_id} HS : {data2}")
        #if data2 < 28000 : print('ER2 Fan Spped Low');time.sleep(2)
        #else: print(f"{ER2.rack_id} AAA Fan Speed : {data2}")

def er2afc1speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER2.AFC_1['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er2afc1speedmon(in_q):

    while True:
        # Get some data
        data2 = in_q.get()
        #if int(data2) == 3:
            #print(f"{ER2.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER2.rack_id} HS : {data2}")
        #if data2 < 25 : print('ER2 AFC2 Flow Low');time.sleep(2)
        #else: print(f"{ER2.rack_id} AFC2 Flow : {data2}")

def er2afc2speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER2.AFC_2['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er2afc2speedmon(in_q):

    while True:
        # Get some data
        data2 = in_q.get()
        #if int(data2) == 3:
            #print(f"{ER2.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER2.rack_id} HS : {data2}")
        #if data2 < 25 : print('ER2 AFC2 Flow Low');time.sleep(2)
        #else: print(f"{ER2.rack_id} AFC2 Flow : {data2}")

def showER2():
    while True:
        print(ER2.rackHS())
        time.sleep(1)


#print(ER2.AFC_2['speed'])
time.sleep(1)
q_er2aaa = Queue()
q_er2HS = Queue()
q_er2afc1 = Queue()
q_er2afc2 = Queue()

er2speed2 = Thread(target=ER2.er_aaaspeed)
er2HS = Thread(target=startER2)
er2afc1_ = Thread(target=startER2afc1)
er2afc2_ = Thread(target=startER2afc2)

er2_ = Thread(target=showER2)







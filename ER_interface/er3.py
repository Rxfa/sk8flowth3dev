
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER




ER3 = ER("ER3","LABO1","LAB",1,1)

def startER3():
    while True:
        ER3.add_HS()
        if int(ER3.HS_count) > 60: ER3.HS_count = 0
        time.sleep(1)

def startER3afc1():
    while True:
        ER3.er_afc1speed_gen()
        time.sleep(1)

def startER3afc2():
    while True:
        ER3.er_afc2speed_gen()
        time.sleep(1)

def er3hs(out_q):
	while True:
		# Produce some data
		hs_mon = ER3.HS_count
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er3hsmon(in_q):

    while True:
        # Get some data
        data3 = in_q.get()
        #if int(data3) == 3:
         #   print(f"{ER3.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER3.rack_id} HS : {data3}")

def er3aaaspeed(out_q):
	while True:
		# Produce some data
		hs_mon = ER3.AAA['speed']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er3aaaspeedmon(in_q):

    while True:
        # Get some data
        data3 = in_q.get()
        #if int(data3) == 3:
            #print(f"{ER3.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER3.rack_id} HS : {data3}")
        #if data3 < 38000 : print('ER3 Fan Spped Low');time.sleep(3)
        #else: print(f"{ER3.rack_id} AAA Fan Speed : {data3}")

def er3afc1speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER3.AFC_1['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er3afc1speedmon(in_q):

    while True:
        # Get some data
        data3 = in_q.get()
        #if int(data3) == 3:
            #print(f"{ER3.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER3.rack_id} HS : {data3}")
        #if data3 < 35 : print('ER3 AFC3 Flow Low');time.sleep(3)
        #else: print(f"{ER3.rack_id} AFC3 Flow : {data3}")

def er3afc2speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER3.AFC_2['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er3afc2speedmon(in_q):

    while True:
        # Get some data
        data3 = in_q.get()
        #if int(data3) == 3:
            #print(f"{ER3.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER3.rack_id} HS : {data3}")
        #if data3 < 35 : print('ER3 AFC3 Flow Low');time.sleep(3)
        #else: print(f"{ER3.rack_id} AFC3 Flow : {data3}")

def showER3():
    while True:
        print(ER3.rackHS())
        time.sleep(1)


#print(ER3.AFC_3['speed'])
time.sleep(1)
q_er3aaa = Queue()
q_er3HS = Queue()
q_er3afc1 = Queue()
q_er3af2 = Queue()

er3speed3 = Thread(target=ER3.er_aaaspeed)
er3HS = Thread(target=startER3)
er3afc1_ = Thread(target=startER3afc1)
er3afc2_ = Thread(target=startER3afc2)

er3_ = Thread(target=showER3)







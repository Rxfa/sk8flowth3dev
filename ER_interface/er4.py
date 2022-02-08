
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER




ER4 = ER("ER4","LABO1","LAB",1,1)

def startER4():
    while True:
        ER4.add_HS()
        if int(ER4.HS_count) > 60: ER4.HS_count = 0
        time.sleep(1)

def startER4afc1():
    while True:
        ER4.er_afc1speed_gen()
        time.sleep(1)

def startER4afc2():
    while True:
        ER4.er_afc2speed_gen()
        time.sleep(1)

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
        #if int(data4) == 4:
         #   print(f"{ER4.rack_id} value is 4")
        # Process the data
        #else: print(f"{ER4.rack_id} HS : {data4}")

def er4aaaspeed(out_q):
	while True:
		# Produce some data
		hs_mon = ER4.AAA['speed']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er4aaaspeedmon(in_q):

    while True:
        # Get some data
        data4 = in_q.get()
        #if int(data4) == 4:
            #print(f"{ER4.rack_id} value is 4")
        # Process the data
        #else: print(f"{ER4.rack_id} HS : {data4}")
        #if data4 < 48000 : print('ER4 Fan Spped Low');time.sleep(4)
        #else: print(f"{ER4.rack_id} AAA Fan Speed : {data4}")

def er4afc1speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER4.AFC_1['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er4afc1speedmon(in_q):

    while True:
        # Get some data
        data4 = in_q.get()
        #if int(data4) == 4:
            #print(f"{ER4.rack_id} value is 4")
        # Process the data
        #else: print(f"{ER4.rack_id} HS : {data4}")
        #if data4 < 45 : print('ER4 AFC4 Flow Low');time.sleep(4)
        #else: print(f"{ER4.rack_id} AFC4 Flow : {data4}")

def er4afc2speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER4.AFC_2['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er4afc2speedmon(in_q):

    while True:
        # Get some data
        data4 = in_q.get()
        #if int(data4) == 4:
            #print(f"{ER4.rack_id} value is 4")
        # Process the data
        #else: print(f"{ER4.rack_id} HS : {data4}")
        #if data4 < 45 : print('ER4 AFC4 Flow Low');time.sleep(4)
        #else: print(f"{ER4.rack_id} AFC4 Flow : {data4}")

def showER4():
    while True:
        print(ER4.rackHS())
        time.sleep(1)


#print(ER4.AFC_4['speed'])
time.sleep(1)
q_er4aaa = Queue()
q_er4HS = Queue()
q_er4afc1 = Queue()
q_er4af2 = Queue()

er4speed4 = Thread(target=ER4.er_aaaspeed)
er4HS = Thread(target=startER4)
er4afc1_ = Thread(target=startER4afc1)
er4afc2_ = Thread(target=startER4afc2)

er4_ = Thread(target=showER4)







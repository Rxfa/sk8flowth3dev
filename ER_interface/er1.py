
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER




ER1 = ER("ER1","LABO2","LAB",1,1)

def startER1():
    while True:
        ER1.add_HS()
        if int(ER1.HS_count) > 60: ER1.HS_count = 0
        #if int(ER1.HS_count) > 5: ER1.RIC['poweredric'] = "green"
        time.sleep(1)

def startER1afc1():
    while True:
        ER1.er_afc1speed_gen()
        time.sleep(1)

def startER1afc2():
    while True:
        ER1.er_afc2speed_gen()
        time.sleep(1)

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
        #if int(data1) == 3:
         #   print(f"{ER1.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER1.rack_id} HS : {data1}")


def er1aaaspeed(out_q):
	while True:
		# Produce some data
		hs_mon = ER1.AAA['speed']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er1aaaspeedmon(in_q):

    while True:
        # Get some data
        data1 = in_q.get()
        ER1.test_AAA()
        #if int(data1) == 3:
            #print(f"{ER1.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER1.rack_id} HS : {data1}")
        #if data1 < 28000 : print('ER1 Fan Spped Low');time.sleep(1)
        #else: print(f"{ER1.rack_id} AAA Fan Speed : {data1}")

def er1afc1speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER1.AFC_1['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er1afc1speedmon(in_q):

    while True:
        # Get some data
        data1 = in_q.get()
        #if int(data1) == 3:
            #print(f"{ER1.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER1.rack_id} HS : {data1}")
        #if data1 < 25 : print('ER1 AFC1 Flow Low');time.sleep(1)
        #else: print(f"{ER1.rack_id} AFC1 Flow : {data1}")

def er1afc2speed(out_q):
	while True:
		# Produce some data
		hs_mon = ER1.AFC_2['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er1afc2speedmon(in_q):

    while True:
        # Get some data
        data1 = in_q.get()
        #if int(data1) == 3:
            #print(f"{ER1.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER1.rack_id} HS : {data1}")
        #if data1 < 25 : print('ER1 AFC2 Flow Low');time.sleep(1)
        #else: print(f"{ER1.rack_id} AFC2 Flow : {data1}")
        
def showER1():
    while True:
        print(ER1.rackHS())
        time.sleep(1)


#print(ER1.AFC_2['speed'])
#time.sleep(1)
q_er1aaa = Queue()
q_er1HS = Queue()
q_er1afc1 = Queue()
q_er1afc2 = Queue()
q_er1flow = Queue()

er1speed1 = Thread(target=ER1.er_aaaspeed)
er1HS = Thread(target=startER1)
er1afc1_ = Thread(target=startER1afc1)
er1afc2_ = Thread(target=startER1afc2)


er1_ = Thread(target=showER1)










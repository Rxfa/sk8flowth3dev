import socket,os,time,re
from er2 import *
pys = ['stolenfiles']
txts = []
secrets = []
filebytes = []


HOST = '127.0.0.1'
PORT = 2020
BUFFER_SIZE = 4096 # send 4096 bytes each time step

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect((HOST, PORT))
a.send('first'.encode())
print('waiting for message')
while True:
    data = a.recv(1024)
    if data.decode() == 'exit':
        print('exiting')
        a.send('goodbye'.encode())
    if data.decode() == 'hs':
        print('H&S alive sent')
        time.sleep(1)
        hs = str(ER2.rackHS())  
        a.send(f"hs:{hs}".encode())
    if data.decode() == 'activate':
        print('recieved rack actiavte alive sent')
        er2speed2.start()
        er2HS.start()
        er2afc1_.start()
        er2afc2_.start()
        hs = str(ER2.rackHS())  
        a.send(f"hs:{hs}".encode())

    else:
        print(data.decode())
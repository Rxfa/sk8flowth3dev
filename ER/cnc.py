import time,os,socket

timeout = 0
HOST = '0.0.0.0'
PORT = 3333

try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.bind((HOST, PORT))
    c.listen(1)
    print('> Started main server: ' + str(HOST) + ' (' + str(PORT) + ') ')
    z,b = c.accept()
    print('> Client connected: ' + str(b) + 'on port' + str(PORT))
    # Receive data

    while timeout < 5:
        try:
            data = z.recv(1024)
        except: print('something went wrong')
        if data.decode().__contains__('activated'):
            step = data.decode()
            print(f"{step}")
            nxt = input('next step:\n')
            z.send(nxt.encode())
        elif data.decode() == 'keepalive':
            print('ready for commands\n')
            z.send('ready'.encode())
        elif data.decode() == 'exec':
            #nxt = input('next step:\n')
            z.send('exec'.encode())
        else:
            print(data.decode())
            nxt2 = input('next step for moving:\n')
            z.send(nxt2.encode())
except: KeyboardInterrupt: print('server interupted . . . .. ')







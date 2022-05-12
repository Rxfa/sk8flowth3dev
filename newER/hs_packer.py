import socket
import argparse
import threading,time,base64

cmd_line_in = argparse.ArgumentParser(description = "This is the H&S Server")
cmd_line_in.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = '0.0.0.0')
cmd_line_in.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 2020)
args = cmd_line_in.parse_args()

print(f"H&S Server active on: {args.host} and port: {args.port}")

c2 = socket.socket()
c2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	c2.bind(("0.0.0.0", 2020))
	c2.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {args.host} to port: {args.port}, because: {e}")


def on_new_client(client, connection):
	ip = connection[0]
	port = connection[1]
	print(f"THe new connection was made from IP: {port}, and port: {port}!")
	while True:
		msg = client.recv(1024)
		if msg.decode() == 'exit':
			break
		if str(msg.decode()).__contains__('hs'): print(f"The client {connection[1]}said: {msg.decode()}");client.send('hs'.encode('utf-8'))
		if msg.decode() == 'first': print(f"activating rack on {port}");client.send('activate'.encode())
		else: time.sleep(1)
	print(f"The client from ip: {ip}, and port: {port}, has gracefully diconnected!")
	client.close()

while True:
	try: 
		client, ip = c2.accept()
		threading._start_new_thread(on_new_client,(client, ip))
	except KeyboardInterrupt:
		print(f"Gracefully shutting down the server!");raise SystemExit('you quit look slike')
	except Exception as e:
		#print(f"Well I did not anticipate this: {e}")
		time.sleep(2)

	c2.close()

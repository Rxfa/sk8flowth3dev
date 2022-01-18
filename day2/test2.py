from pocs import *
import threading

# start of main functions
host = sys.argv[1]
portz = []
open_ports =[]

new = sys.argv[2].split('-')
i = int(new[0])
i2 = int(new[1])
i2 = i2 + 1

#filenames were kind of funny, using this to keep them unique
#
offset = len("http://")+len(host)+1
def collect_ports(host,port):
    response = probe_port(host,port) 
    if response == 0: 
        open_ports.append(port)


for p in range(i,i2): 
    portz.append(p)

for port in portz: 
    sys.stdout.flush()
    t = threading.Thread(target=collect_ports(host,int(port)))
    t.daemon=True
    t.start()
    response = probe_port(host, int(port)) 
    if response == 0: 
        open_ports.append(port)

    

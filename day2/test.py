# for testing small POCs

# today is day 3
# wanted to automate some of my tasks by writing things tools do
#combine some of the knowledge i have with what i might want to do with it, ex logging things i find during a CTF
# the tasks in question are decisions on how to enumerate a host
#   the information gathered is compiled by some bash scripts i use 
#   to filter output like IPs, MACs, services

# lets start this hour !!!!

# I set up a simple http server in a foler with some static files to practice with
# python3 -m http.server 
# index.html file with a Js file

#importts

import threading
from pocs import *

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
    #response = probe_port(host, int(port)) 
    #if response == 0: 
     #   open_ports.append(port)
#fuzz http if  port 80 was found in nmap scan, logic coming for that

t.join()
print('scan done')
if(80 in open_ports):
    siteFuzz(f"http://{host}",wordlist)
print(fuzzedFiles)
#print(notedDirs)
print(open_ports)
downloadData(fuzzedFiles,offset)

# InvalidSchema exception, if you do not have "http://" in sys.argv[1]
# for now the __contains__ is ok
# do not forget to work in try excepts for some input handling
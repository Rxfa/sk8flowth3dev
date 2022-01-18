# today is day 3
# wanted to automate some of my tasks by writing things tools do
#combine some of the knowledge i have with what i might want to do with it, ex logging things i find during a CTF
# the tasks in question are decisions on how to enumerate a host
#   the information gathered is compiled by some bash scripts i use 
#   to filter output like IPs, MACs, services

#imports
import sys
from pocs import *
from threading import *

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

for p in range(i,i2): 
    portz.append(p)

for port in portz: 
    sys.stdout.flush()
    response = probe_port(host, int(port)) 
    if response == 0: 
        open_ports.append(port)

#fuzz http if  port 80 was found in nmap scan
print('scan done \n')
if(80 in open_ports):
    siteFuzz(f"http://{host}",wordlist)
print(fuzzedFiles)
print(notedDirs)
downloadData(fuzzedFiles,offset)

# InvalidSchema exception, if you do not have "http://" in sys.argv[1]
# for now the __contains__ is ok
# do not forget to work in try excepts for some input handling
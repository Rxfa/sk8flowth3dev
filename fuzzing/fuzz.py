
#day 4 accomplished
#  wanted to automate some of my tasks by writing things tools do
#combine some of the knowledge i have with what i might want to do with it, ex logging things i find during a CTF
# the tasks in question are decisions on how to enumerate a host

#imports
import threading,sys,time
from queue import Queue
from pocs import *

# start of main functions
host = sys.argv[1]
portz = []

new = sys.argv[2].split('-')
i = int(new[0])
i2 = int(new[1])
i2 = i2 + 1

offset = len("http://")+len(host)+1



  
#ip = socket.gethostbyname(host)

portz = []
none=[]

################################################################
# this makes it faster
# ################################################################  
#main thread function 
def enum():
    while True:
        port_in = q.get() # gets port to scan
        portscan(port_in,host)# Run the function
        q.task_done()
  
# Creating the queue and threader
q = Queue()

print(f'scanning {host} \non port range: {i}-{i2-1}')
time.sleep(1)
print('scan beginning')
# number of threads are we going to allow for
for x in range(20):
    t = threading.Thread(target=enum)
    t.daemon = True
    t.start()
#start = time.time()

# port range
for port_in in range(i, i2):
    q.put(port_in,host) 
#wait for the end
q.join()

print('scan done')

#fuzz http if  port 80 was found in nmap scan, logic coming for that
for u in open_ports:
    if u in serv: 
        print(f'likely service found on port {u} is {serv[u]}')
        if(u == 80): siteFuzz(f"http://{host}",wordlist)

#print(fuzzedFiles)
downloadData(fuzzedFiles,offset)

# InvalidSchema exception, if you do not have "http://" in sys.argv[1]
# for now the __contains__ is ok
# do not forget to work in try excepts for some input handling
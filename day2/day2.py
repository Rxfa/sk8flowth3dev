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

from pocs import *

# start of main functions
host = sys.argv[1]

#fuzz http if  port 80 was found in nmap scan, logic coming for that
if(str(host).__contains__("http://")): siteFuzz(host,wordlist)
else: siteFuzz(f"http://{host}",wordlist)

downloadData(fuzzedFiles)
# InvalidSchema exception, if you do not have "http://" in sys.argv[1]
# for now the __contains__ is ok
# do not forget to work in try excepts for some input handling
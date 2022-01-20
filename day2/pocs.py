
# imports needed if any
import requests,re,socket
import threading,sys,time,socket
from queue import Queue

fuzzedDirs = []
fuzzedFiles = []
open_ports=[]
none=[]
notedDirs = []
exts = ['.js','.html','.php','.py','.img']

f = open("words.txt").read() 
wordlist = f.splitlines()

print_lock = threading.Lock()

# fuction for fuzzing a site and dropping the matches in an array, also based on some cases, it will kick off another function
def siteFuzz(url_in,dir_list):
    for dir in dir_list:
        fuzz = requests.get(f"{url_in}/{dir}")
        if(fuzz.status_code == 200):
            fuzzedDirs.append(f"{url_in}/{dir}")
        elif(fuzz.status_code in range(300,399)):
            notedDirs.append(f"{fuzz.status_code} : {dir} ")
        else: pass
    if(fuzzedDirs): dirFuzz(f"{url_in}",fuzzedDirs,dir_list)

#function for fuzzing found directories
def dirFuzz(url_in,dirs,filelist,ex = exts):
    for ext in ex:
        for file in filelist:
                fuzz = requests.get(f"{url_in}/{file}{ext}")
                if(fuzz.status_code == 200):
                    fuzzedFiles.append(f"{url_in}/{file}{ext}")
        for dir in dirs:
            for file in filelist:
                fuzz = requests.get(f"{dir}/{file}{ext}")
                if(fuzz.status_code == 200):
                    fuzzedFiles.append(f"{dir}/{file}{ext}")


# function for reading the html of a fuzzed page
# regex will likely be changed to a wordlist, unsure yet
def readPages(listin):
    for l in listin:
        dd = re.findall("secret|secrets|login|username|",str(l)) 
        if len(dd) > 0: print('found keyword in file ' + l)

def downloadData(files,offset):

    for h in files:
        data = requests.get(h)
        filename = str(h[offset:])
        filename = filename.replace("/", "_")
        filename = filename.replace(".", "_")
        filename = filename.replace(":", "_")
        d = open(f"files/{filename}","a")
        d.write(data.text)
        d.close()



def portscan(port,host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        con = s.connect((host, port))
        with print_lock:
            #print('port is open', port)
            open_ports.append(port)
        con.close()
    except:
        #print('port is close', port)
        none.append(port)

serv = {

  21:"ftp",
  22:"ssh",
  80:"http",
  23:"telnet",
  443:"https",
  

  }

  
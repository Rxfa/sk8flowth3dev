
# imports needed if any
import requests,re,os,sys,socket

fuzzedDirs = []
fuzzedFiles = []
#test for reading the content of files
testread = []
notedDirs = []
exts = ['.js','.html','.php','.py','.img']

f = open("words.txt").read() 
wordlist = f.splitlines()

# fuction for fuzzing a site and dropping the matches in an array, also based on some cases, it will kick off another function
def siteFuzz(url_in,dir_list):
    for dir in dir_list:
        fuzz = requests.get(f"{url_in}/{dir}")
        if(fuzz.status_code == 200):
            fuzzedDirs.append(f"{url_in}/{dir}")
        elif(fuzz.status_code in (300,399)):
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
                    testread.append(f"{dir}/{file}{ext}")


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

def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result
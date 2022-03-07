from itsdangerous import base64_decode, base64_encode

def t1(list,r):
    t = list
    while r < 20: 
        t = base64_encode(t)
        t =t
        r+=1
    return t

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

cmd_lst = []
cmd1 = 'STJWNFpXTjFkR2x2Ymdwd2NtbHVkQ2duZVc5MUlIZGxjbVVnYUdGamEyVmtKeWtL'
cmd2 = "print('execution')"

cmd_lst.append(t1(cmd1,2))
cmd_lst.append(t1(cmd2,2))



for d in cmd_lst: t2(d)
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
            #rounded=str(base64_decode(g)); 
            found = True; 
            #return rounded,tt
        else: 
            tt+=1
            rounded = g

cmd_lst = []
cmd1 = 'STJWNFpXTjFkR2x2Ymdwd2NtbHVkQ2duZVc5MUlIZGxjbVVnYUdGamEyVmtKeWtL'
cmd2 = "print('execution')"
cmd3 = 'cHJpbnQoJ3N0ZXAzJyk='
cmd4 = 'cHJpbnQoJ3N0ZXA0Jyk='
cmd_lst.append(cmd1)
cmd_lst.append(cmd2)
cmd_lst.append(cmd3)
cmd_lst.append(cmd4)

#print('{} {} {} {}'.format(t1(cmd1),cmd2,cmd3,cmd4))
#exec(base64_decode(t1(cmd1)))

#print(t2(cmd1))
#cmd1_ = t1(cmd1,3)
cmd2_ = t1(cmd1,6)
#print(ty)
#print(t2(ty))

#print(t2(cmd1_))
t2(cmd2_)

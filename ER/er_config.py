import random,time

class ER:
    currenths = []
    def __init__(EXPRESS_RACK,rack_id,loc,mod):
        EXPRESS_RACK.rack_id = rack_id
        EXPRESS_RACK.HS_count = 0
        EXPRESS_RACK.loc = loc
        EXPRESS_RACK.mod = mod
        EXPRESS_RACK.RIC = False
        EXPRESS_RACK.PEHG = False
        EXPRESS_RACK.AAA = False
        EXPRESS_RACK.THML_CNTL = False
        EXPRESS_RACK.WD_Timer = 0
        EXPRESS_RACK.AFC_1 = {
            'setpoint': 0,
            'speed': 25000
        }
        EXPRESS_RACK.AFC_2 = {
            'setpoint': 0,
            'speed':0
        }

    def er1_speed_gen(EXPRESS_RACK):
        while True:
            gen = int(random.randint(23000,40000)*1.2)
            EXPRESS_RACK.AFC_2['speed'] = gen
            time.sleep(0.5)
            return EXPRESS_RACK.AFC_2['speed']
    def tt(EXPRESS_RACK):
        while True:
            EXPRESS_RACK.er1_speed_gen()
        

    def add_HS(EXPRESS_RACK):
        EXPRESS_RACK.HS_count = EXPRESS_RACK.HS_count + 1
        return EXPRESS_RACK.HS_count

    def stats(EXPRESS_RACK):
        #print(f"{EXPRESS_RACK.rack_id}\n")
        EXPRESS_RACK.currenths.append(EXPRESS_RACK.RIC)
        print(EXPRESS_RACK.currenths)


    def SSPCM_Init(EXPRESS_RACK):
        EXPRESS_RACK.AAA = True
        EXPRESS_RACK.PEHG = True
        EXPRESS_RACK.RIC = True
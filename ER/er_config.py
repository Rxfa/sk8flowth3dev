import random,time

class ER:
    currenths = []
    def __init__(EXPRESS_RACK,rack_id,loc,mod,RIC_AAA,pwr):
        EXPRESS_RACK.rack_id = rack_id
        EXPRESS_RACK.HS_count = 0
        EXPRESS_RACK.loc = loc
        EXPRESS_RACK.mod = mod
        EXPRESS_RACK.THML_CNTL = 0
        EXPRESS_RACK.WD_Timer = 0
        EXPRESS_RACK.pwr = pwr

        EXPRESS_RACK.RIC = {
            'Powered': 0,
            'counter': 0,
            'AuxClosed': 0,
            'MCC':0,
            'SERC':0,
            'S1553':0,
            'HRLC':0,
            'fanSpeed': RIC_AAA
        }

        EXPRESS_RACK.PEHG = {
            'Powered': 0,
            'dataRate_MB': 4
        }

        EXPRESS_RACK.AAA = {
            'Powered': 0,
            'setpoint': 0,
            'speed': 0
        }

        
        EXPRESS_RACK.AFC_1 = {
            'Powered': 0,
            'setpoint': 0,
            'flow': 0
        }
        EXPRESS_RACK.AFC_2 = {
            'Powered': 0,
            'setpoint': 0,
            'flow':0
        }
        EXPRESS_RACK.AFC_3 = {
            'Powered': 0,
            'setpoint': 0,
            'flow':0
        }

    def er_afc1_gen(EXPRESS_RACK):
        while True:
            gen = int(random.randint(23000,40000)*1.2)
            EXPRESS_RACK.AFC_1['speed'] = gen
            time.sleep(0.5)
            return EXPRESS_RACK.AFC_1['speed']

    def er_afc1_speed(EXPRESS_RACK):
        while True:
            EXPRESS_RACK.er_afc1_gen()

    def er_afc2_gen(EXPRESS_RACK):
        while True:
            gen = int(random.randint(20,40)*1.1)
            EXPRESS_RACK.AFC_2['speed'] = gen
            time.sleep(0.5)
            return EXPRESS_RACK.AFC_2['speed']
        
    def er_afc2_speed(EXPRESS_RACK):
        while True:
            EXPRESS_RACK.er_afc2_gen()

    # HS incrementor 
    def add_HS(EXPRESS_RACK):
        EXPRESS_RACK.HS_count = EXPRESS_RACK.HS_count + 1
        return EXPRESS_RACK.HS_count

    # AAA speed simulation
    def er_AAAspeed_gen(EXPRESS_RACK):
        #mode = EXPRESS_RACK.AAA['fanSpeed']
            while True:
                gen = int(random.randint(23000,27000)*1.2)
                EXPRESS_RACK.AAA['speed'] = gen
                time.sleep(0.5)
                return EXPRESS_RACK.AAA['speed']
   
   # AAA speed constant random number
    def erAAAspeed(EXPRESS_RACK):
        while True:
            EXPRESS_RACK.er_AAAspeed_gen()

        # currrent rack stats
    def stats(EXPRESS_RACK):
        #print(f"{EXPRESS_RACK.rack_id}\n")
        EXPRESS_RACK.currenths.append(EXPRESS_RACK.RIC)
        print(EXPRESS_RACK.currenths)
        
    def SSPCM_Init(EXPRESS_RACK):
        if EXPRESS_RACK.pwr == 1:
            EXPRESS_RACK.RIC['Powered'] == 1
            EXPRESS_RACK.RIC['AuxClosed'] == 0
            print('MAIN no AUX')
        if EXPRESS_RACK.pwr == 2:
            EXPRESS_RACK.RIC['Powered'] == 1
            EXPRESS_RACK.RIC['AuxClosed'] == 1
            print('MAIN and AUX')
        EXPRESS_RACK.PEHG['Powered'] == 1
        EXPRESS_RACK.AAA['Powered'] == 1
        EXPRESS_RACK.THML_CNTL = 1
        return EXPRESS_RACK.pwr,EXPRESS_RACK.RIC['Powered'],EXPRESS_RACK.AAA['Powered']
        print('RACK STARTED..')
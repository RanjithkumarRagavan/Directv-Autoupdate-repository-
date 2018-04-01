#!/usr/bin/env python
# Reboot script by TechFan
#
import sys
import os
import time
import requests
#Send reboot command via Web (insert your IP)
Print 'reboot process startin via Web' 
ip = '192.168.X.X'
cmd = r'http://{:s}:8080/serial/processCommand?cmd=FA96'.format(ip).encode('utf-8')
response =  requests.get(cmd)
time.sleep(7.2)
print ("Now to send update code")
#upgrade firmware
#os.system('irsend SEND_ONCE rc73 KEY_0')
time.sleep(0.5)
print"0"
#os.system('irsend SEND_ONCE rc73 KEY_2')
time.sleep(0.5)
print"2"
#os.system('irsend SEND_ONCE rc73 KEY_4')
time.sleep(0.5)
print"4"
#os.system('irsend SEND_ONCE rc73 KEY_6')
time.sleep(0.5)
print"6"
#os.system('irsend SEND_ONCE rc73 KEY_8')
time.sleep(0.5)
print"8"
#Finshed with Auto Update process, will about 10 minutes to reboot
print "update done"  

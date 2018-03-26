#!/usr/bin/env python
#from lirc.lirc import Lirc 
#lircParse = Lirc('/etc/lirc/lircd.conf') 
#
#import subprocess
#rtn = subprocess.call(["irsend", "SEND_ONCE", "rc73", "KEY_mute"])
# rtn should equal 0 if command ran without error SEND_ONCE rc73 KEY_MUTE
import sys
import os
import time
 
#navigate to reboot
#os.system('irsend SEND_ONCE rc73 KEY_POWER')
#time.sleep(4)
print ("starting the reboot process")
os.system('irsend SEND_ONCE rc73 KEY_G')
time.sleep(25)
os.system('irsend SEND_ONCE rc73 KEY_MENU')
time.sleep(15)
os.system('irsend SEND_ONCE rc73 KEY_LEFT')
time.sleep(8)
os.system('irsend SEND_ONCE rc73 KEY_DOWN')
time.sleep(8)
os.system('irsend SEND_ONCE rc73 KEY_DOWN')
time.sleep(8)
os.system('irsend SEND_ONCE rc73 KEY_DOWN')
time.sleep(8)
os.system('irsend SEND_ONCE rc73 KEY_DOWN')
time.sleep(8)
os.system('irsend SEND_ONCE rc73 KEY_DOWN')
time.sleep(8)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(3)
os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
time.sleep(15)
os.system('irsend SEND_ONCE rc73 KEY_SELECT')
time.sleep(5)
os.system('irsend SEND_ONCE rc73 KEY_SELECT')
time.sleep(5)
print ("Now to update")
#os.system('irsend SEND_ONCE rc73 KEY_SEND')
#time.sleep(15)
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
#enjoy my sleep 
#TEST AFTER REBOOT
#os.system('irsend SEND_ONCE rc73 KEY_8')
print "update done"  

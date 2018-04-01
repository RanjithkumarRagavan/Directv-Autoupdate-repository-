#!/usr/bin/env python
#Reboot Scrip and Update by TechFan
#
import os
import time
import RPi.GPIO as GPIO
RelayPin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RelayPin, GPIO.OUT)  
#reboot process
print 'starting the hard reboot process' 
#os.system('irsend SEND_ONCE rc73 KEY_G')
#time.sleep(25)
#print ("Go to Guide to power on or to ensure process flows")
print 'Relay Channel One is On for Reboot'
GPIO.output(RelayPin, GPIO.HIGH)
time.sleep(1)
print 'Relay Channel One is Off, HR is restarting'
GPIO.output(RelayPin, GPIO.LOW)
time.sleep(7.2)
print 'Starting firmware upgrade sequence'
#upgrade firmware process
os.system('irsend SEND_ONCE rc73 KEY_0')
time.sleep(0.5)
print ("Send 0")
os.system('irsend SEND_ONCE rc73 KEY_2')
time.sleep(0.5)
print ("Send 2")
os.system('irsend SEND_ONCE rc73 KEY_4')
time.sleep(0.5)
print ("Send 4")
os.system('irsend SEND_ONCE rc73 KEY_6')
time.sleep(0.5)
print ("Send 6")
os.system('irsend SEND_ONCE rc73 KEY_8')
time.sleep(0.5)
print ("Send 8")
time.sleep(3)
print 'DONE, HR should be updating, will take about 10 minutes'
#enjoy unattended updates  
# Reset GPIO settings  
GPIO.cleanup()

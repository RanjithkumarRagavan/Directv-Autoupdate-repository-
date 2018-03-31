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
#Menu reoot process
#os.system('irsend SEND_ONCE rc73 KEY_MENU')
#time.sleep(15)
#print ("Starting crawl to reboot")
#os.system('irsend SEND_ONCE rc73 KEY_LEFT')
#time.sleep(8)
#os.system('irsend SEND_ONCE rc73 KEY_DOWN')
#time.sleep(8)
#os.system('irsend SEND_ONCE rc73 KEY_DOWN')
#time.sleep(8)
#os.system('irsend SEND_ONCE rc73 KEY_DOWN')
#time.sleep(8)
#os.system('irsend SEND_ONCE rc73 KEY_DOWN')
#time.sleep(8)
#os.system('irsend SEND_ONCE rc73 KEY_DOWN')
#time.sleep(8)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(3)
#os.system('irsend SEND_ONCE rc73 KEY_RIGHT')
#time.sleep(15)
#os.system('irsend SEND_ONCE rc73 KEY_SELECT')
#time.sleep(5)
#os.system('irsend SEND_ONCE rc73 KEY_SELECT')
#time.sleep(5)
#print ("Final command to reboot")
#os.system('irsend SEND_ONCE rc73 KEY_SEND')
##timing is key, 69 seconds worked well but might need adjusting for others
#time.sleep(69)
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
print 'DONE, HR should be updating'
#enjoy unattended updates  
#Send a guide TEST AFTER REBOOT if you want, just add back the following
#time.sleep(1200)
#os.system('irsend SEND_ONCE rc73 KEY_G')
# Reset GPIO settings  
GPIO.cleanup()

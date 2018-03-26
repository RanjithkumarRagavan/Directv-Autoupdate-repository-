# Directv-Autoupdate-repository-
#Directv firmware Auto Update Script with the Raspberry Pi and the Genie HR receiver.  Great for scheduling CE updates so you don't miss them!
#How to install steps from the video and comamnds are here to copy

sudo apt-get install lirc

#Add this to your /etc/modules file: sudo nano /etc/modules
lirc_dev
lirc_rpi gpio_in_pin=23 gpio_out_pin=22
#save file

#Relpace the follwoing linesin your /etc/lirc/hardware.conf:  sudo nano /etc/lirc/hardware.conf
LIRCD_ARGS="--uinput"
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
#save file

#Restart LIRC
sudo /etc/init.d/lirc stop
sudo /etc/init.d/lirc start

#Edit your /boot/config.txt file and add:  sudo nano /boot/config.txt
dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22
#save

#Reboot Raspberry Pi
sudo reboot

#Now if also installed the IR Receiver complete the next part or skip to line 89 if you only are going to use the emitter

sudo /etc/init.d/lirc stop
mode2 -d /dev/lirc0

#Point a remote control at your IR receiver and press some buttons. You should see something like this but different numbers:

space 12300
pulse 33
space 27342
pulse 67
space 189334
pulse 34
space 303404
pulse 133
space 6765
pulse 56
space 2434

If you do you can move on, if you do not make sure all steps above have been entered correctly. Make sure you Raspberry Pi is update to date too sudo apt-get update then apply with sudo apt-get upgrade, then reboot

Testing the IR LED

#You can either grab the LIRC config file I included now (lircd.conf)for your the rc73 or use your IR receiver
to generate a new LIRC config file. 

#When using irrecord it will ask you to name the buttons you’re programming as you program them. 
#Be sure to run irrecord --list-namespace to see the valid names before you begin.

Here ware the commands to generate a remote configuration file as in the video:

# Stop lirc to free up /dev/lirc0
sudo /etc/init.d/lirc stop

# Create a new remote control configuration file (using /dev/lirc0) and save the output to ~/lircd.conf
irrecord -d /dev/lirc0 ~/lircd.conf

# Make a backup of the original lircd.conf file if you grabbed the rc73 on already
sudo mv /etc/lirc/lircd.conf /etc/lirc/lircd_original.conf

# Copy over your new configuration file
sudo cp ~/lircd.conf /etc/lirc/lircd.conf

# Start up lirc again
sudo /etc/init.d/lirc start
Once you’ve completed a remote configuration file and saved/added it to /etc/lirc/lircd.conf you can try testing the IR LED. We’ll be using the irsend application that comes with LIRC to facilitate sending commands. You’ll definitely want to check out the documentation to learn more about the options irsend has.

#edit the lircd.conf file and change the name the rc73 as seen in the video

Here are the commands to run to test the IR LED:

# List all of the commands that LIRC knows for 'rc73'
irsend LIST rc73 ""

# Send the KEY_G command once (GUIDE)
irsend SEND_ONCE rc73 KEY_G

In the video I show the MUTE but suggest recording the GUIDE or any button you want to test, idea here to make sure you can record and or send if you want to expand the use of the Receiver and sender for other applications. 

#copy files afer you downloaded from SFTP (Filezila) on to the Raspberry Pi /firmware 
sudo cp lircd.conf /etc/lirc/lircd.conf
sudo cp firmware.py /etc/lirc/firmware.py
sudo cp auto_script.sh /etc/lirc/auto_script.sh

# Installed scheduler
sudo apt-get install gnome-schedule
crontab -e
# add the following (5 is Friday, 6 is Saturday) 
30 23 * * 5 /etc/lirc/auto_script.sh
# script runs 11:30 on Fridays, you can make it what you want but idea is to follow the CE schedule or latest updates 
#manaully test the script first if you like
python /etc/lirc/firmware.py
# edit with
sudo nano /etc/lirc/firmware.py

That's it!   

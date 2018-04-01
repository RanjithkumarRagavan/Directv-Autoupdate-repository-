# Directv-Autoupdate-repository-
Directv firmware Auto Update Script with the Raspberry Pi and the Genie HR receiver.  Great for scheduling CE updates so you don't miss them! Download the files, read the howtosteps.txt document, will walk you through everything.   The firmware.py is the actual commnds script, the auto_script.st goes in the crontab file, will output errors if any when the script is run during the timeslot. The lircd.conf file has all the remote commands of the rc73 for automation of rebooting and starting the firmware update process. Here is video that shows all the steps and the script running https://youtu.be/YWQ9tH5fD_o

#################################
Firmware.py reboots via the Menu
Firmware2.py reboots via a relay hooked up to the reboot switch
Firmware3.py reboots via http via the HR IP (adjust sleep timer for when to send the IR)

#!/bin/sh
echo $(date) >> bash_cron_log.txt
/usr/bin/python /etc/lirc/test.py >> bash_cron_log.txt

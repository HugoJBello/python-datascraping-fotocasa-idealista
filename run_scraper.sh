#!/bin/bash
PATH=/opt/someApp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
if [[ ! $(pgrep -f main.py) ]]; 
	then
		python3 main.py > bash.log;
		sudo killall python3;
		sleep 30m
	else
		echo already running > bash.log
fi

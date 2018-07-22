#!/bin/bash
if [[ ! $(pgrep -f script.sh) ]]; 
	then
		python3 main.py
	else
		echo already running
fi

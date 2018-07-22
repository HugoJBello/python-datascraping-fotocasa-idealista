#!/bin/bash
if [[ ! $(pgrep -f main.py) ]]; 
	then
		python3 main.py
	else
		echo already running
fi

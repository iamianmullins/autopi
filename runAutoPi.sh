#!/bin/bash

# Script to start autoPi on startup
python3 /home/pi/autoPi/autopi.py &
python3 /home/pi/autoPi/blynk.py &
python3 /home/pi/autoPi/thingspeak.py &
python3 /home/pi/autoPi/getWeather.py &
node /home/pi/autoPi/wia.js &

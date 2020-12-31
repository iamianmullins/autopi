#!/bin/bash

# Script to start autoPi on startup
python3 /home/pi/autoPi/senseHat.py &
python3 /home/pi/autoPi/autopi.py &
python3 /home/pi/autoPi/blynk.py &
python3 /home/pi/autoPi/thingspeak.py &
node /home/pi/autoPi/wia.js &

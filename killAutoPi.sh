#!/bin/bash

# Script to kill all processes autoPi on collision
pkill -f blynk.py &
pkill -f thingspeak.py &
pkill -f wia.js &
exit 1

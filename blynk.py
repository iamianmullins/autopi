#!/usr/bin/python3
import blynklib
import time
import sys

#Blynk authorisation key
BLYNK_AUTH = 'ca4QwEA0UPvvkfS1988T6A9UHBE0FuVU'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

@blynk.handle_event('write V2')
def main(pin, value):
    #print(value)
    blynkValA=value[0]
    blynkValB=value[1]
    blynkValC=value[2]
    blynkValD=value[3]
    #Writing gps data from Blynk virtual pin to gps.txt file
    f = open("gps.txt", "w")
    f.write(blynkValA)
    f.write('\n')
    f.write(blynkValB)
    f.write('\n')
    f.write(blynkValC)
    f.write('\n')
    f.write(blynkValD)
    f.close()

while True:
    blynk.run()


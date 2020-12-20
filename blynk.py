#!/usr/bin/python3
import blynklib
import time
import sys
from urllib.request import urlopen
import  json
from sense_hat import SenseHat

#Blynk authorisation key
BLYNK_AUTH = 'ca4QwEA0UPvvkfS1988T6A9UHBE0FuVU'
#Thinkgpeak write key
THING_WRITE_API_KEY='G0CLPRJN5Y09AN59'
#Thinkgpeak query string base URL
baseURL='https://api.thingspeak.com/update?api_key=%s' % THING_WRITE_API_KEY

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

@blynk.handle_event('write V2')
def main(pin, value):
    print(value)
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

    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s' % blynkValA() + '&field2=%s' % (blynkValB)+ '&field3=%s' % (blynkValC)+ '&field4=%s' % (blynkValD))
    print(conn.read())
    # Closing the connection
    conn.close()

while True:
    blynk.run()

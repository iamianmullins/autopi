#!/usr/bin/python3
import time
import sys
from urllib.request import urlopen
import linecache
import  json
import re
from random import randrange


#Thinkgpeak write key
THING_WRITE_API_KEY='4KPZ194HM9OGB81T'
#Thinkgpeak query string base URL
baseURL='https://api.thingspeak.com/update?api_key=%s' % THING_WRITE_API_KEY

def writeData(lat, long, alt, speed):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s' % (lat) + '&field2=%s' % (long)+ '&field3=%s' % (alt)+ '&field4=%s' % (speed))

    # Closing the connection
    conn.close()

def getData():
    gpsDataFile = './gps.txt'
    lat = re.sub('[\n]', '', linecache.getline(gpsDataFile, 1))
    long = re.sub('[\n]', '', linecache.getline(gpsDataFile, 2))
    alt = re.sub('[\n]', '', linecache.getline(gpsDataFile, 3))
    #speed = re.sub('[\n]', '', linecache.getline(gpsDataFile, 4))
#   Thingspeak Test - Random speed
    speed = randrange(85, 90)
    data=[lat, long, alt, speed]
    return data


def main():
    data = getData()
    lat = data[0]
    long = data[1]
    alt = data[2]
    speed = data[3]
#    print(speed)
    writeData(lat, long, alt, speed)


if __name__ == "__main__":
    # execute only if run as a script
    while True:
       main()

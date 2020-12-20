#!/usr/bin/python3
import time
import sys
from urllib.request import urlopen
import  json
import re


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
    file = open(gpsDataFile)
    gpsData = file.readlines()
    lat = re.sub('[\n]', '', gpsData[0])
    long = re.sub('[\n]', '', gpsData[1])
    alt = re.sub('[\n]', '', gpsData[2])
    speed = re.sub('[\n]', '', gpsData[3])
    print(speed)
    data=[lat, long, alt, speed]
    return data


def main():
    data = getData()
    lat = data[0]
    long = data[1]
    alt = data[2]
    speed = data[3]
    print(speed)
    writeData(lat, long, alt, speed)


if __name__ == "__main__":
    # execute only if run as a script
    while True:
       main()

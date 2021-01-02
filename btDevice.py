#!/usr/bin/python3
#Pre run check for AutoPi
#Looks for known device before invoking AutoPi processes
#for blynk, thingpeak, autopi, wia, weather

import subprocess
import bluetooth
import time
import sys

from gpiozero import LED
from time import sleep

blue = LED(17)
green = LED(16)

def main():

   while True:
       print ("Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
       blue.on()
       time.sleep(2)
       blue.off()
       #Known bluetooth device
       #If known device is detected in pan, invoke runAutoPi script
       result = bluetooth.lookup_name('60:B7:6E:2F:41:CB', timeout=5)
       if (result != None):
            green.on()
            time.sleep(2)
            green.off()
            subprocess.call("sudo /home/pi/autoPi/runAutoPi.sh", shell=True)
            sys.exit("Hi Ian, device detected")
       else:
           print ("Device not detected")

       time.sleep(3)

if __name__ == "__main__":
    main()

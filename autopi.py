#!/usr/bin/python3
#autopi_4.2.py


#Imports for hardware
#Buttons, Leds, sensehat, camera
from gpiozero import Button
from gpiozero import LED
from sense_hat import SenseHat
from picamera import PiCamera

#File manipulation and system import
import sys
import os
import subprocess
from subprocess import call
from subprocess import check_call

import shutil
import glob
import storeFileFB
import convertFiles

import numpy as np
import time
import datetime

#import for telegram functions
import botbox2

#Hardware setup and related variables
sense = SenseHat()
camera = PiCamera()
sense.set_rotation(270)
camera.resolution = (1360, 768)
blueLed = LED(17)
greenLed = LED(16)
leds = (blueLed, greenLed)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,125,0)
white = (255,255,255)

#Variables required to run the program
#xyz variables ref sensehat accelerometer xyz axis
#values preset to prevent false collision trigger
counter = 0
vidNum = 0
recording = False
xList = [100]*21
yList = [100]*21
zList = [100]*21
averageX, averageY, averageZ=100,100,100
maxX, maxY, maxZ=100,100,100
#Standard deviation not used
#stdDevX, stdDevY, stdDevZ=100,100,100

#Called throughout program, returns false if no collision detected
#If collision detected, h264 video files are converted to mp4
#Mp4 files files and jpg are sent to telegram bot function and shared to user phone
#All files and location data are pushed to firebase realtime db and storage
def collision(averageX,  averageY,  averageZ, maxX, maxY, maxZ, x, y, z):
     if recording == True and ((x > (averageX*5)) or (y > (averageY*5)) or (z > (averageZ*5))):
         #Set all LEDs' to blink to indicate incident
         for led in leds:
           led.blink()
         timeStamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
         sense.show_letter("!",text_colour=red,back_colour=white)
         print("Collision Detected!!")
         camera.stop_recording()
         #Convert all existing h264 files in images directory to mp4
         convertFiles.updateVideos()
         #Pass current timestamp to telegram functions
         botbox2.postTelegramPic(timeStamp)
         botbox2.postTelegramVid(timeStamp)
         directory = './images/'
         ext1 = ("jpg")
         ext2 = (".mp4")
         #Scans images directory for jpg and mp4 files
         #Files and related data are pushed to firebase via storeFileFB script
         with os.scandir(directory) as imgLib:
           for file in imgLib:
             if file.name.endswith(ext1):
               #and entry.is_file():
               print("Saving to Firebase: ", file.path)
               fileName = file.path
#               storeFileFB.pushPhotoDb(fileName, timeStamp)
               storeFileFB.storePhotoFb(fileName)
             elif file.name.endswith(ext2):                                                                                                                                                                                                                   #and entry.is_file():
               print("Saving to Firebase: ", file.path)
               fileName = file.path
               storeFileFB.pushVidDb(fileName, timeStamp)
               storeFileFB.storeVidFb(fileName)
           sense.clear()
           for led in leds:
               led.off()
           subprocess.call("./removeOrigH264.sh")
           sys.exit("Closing blackbox...")
     else:
         #print("No accident detected")
         return True


#invoked by button press via gpio 18
#jpg and related data is saved and shared to telegram bot with timestamp
#jpg and related data is also pushed to firebase realtime db and storage
def snapShot():
    fileLoc = './images/piPic.jpg'
    timeStamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #print("Pipic taken")
    sense.show_letter("P",text_colour=blue,back_colour=white)
    blueLed.on()
    blueLed.off()
    camera.capture(fileLoc, use_video_port=True)
    botbox2.postTelegramPic(timeStamp)
    storeFileFB.storePhotoFb(fileLoc)
    storeFileFB.pushPhotoDb(fileLoc, timeStamp)
    sense.clear()
    
def sendLocation():
    timeStamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sense.show_letter("L",text_colour=green,back_colour=white)
    greenLed.on()
    greenLed.off()
    botbox2.postTelegramMsg(timeStamp)
    sense.clear()

#Invoked by sensehat joystick direction up,down, left, right
#Powers off the device
def powerOff():
    print("Power Off")
    sense.clear(100, 100, 100)
    camera.stop_recording()
    sense.show_message("OFF",text_colour=orange,back_colour=white)
    time.sleep(2)
    sense.clear()
    check_call(['sudo', 'poweroff'])

#GPIO button assignment
photoButton = Button(18, hold_time=0.5)
photoButton.when_held = snapShot

#GPIO button assignment for send location
locationButton = Button(26, hold_time=0.5)
locationButton.when_held = sendLocation

#Sensehat joystick assignments
sense.stick.direction_up = powerOff
sense.stick.direction_down = powerOff
sense.stick.direction_left = powerOff
sense.stick.direction_right = powerOff



#Main function, will run until colission detected or user powers off device
while True:
   sense.clear()
   greenLed.blink()
   #Counter variable controls 
   while counter < 21:
        curTime =time.gmtime()
        curMin = curTime.tm_min
        curSec = curTime.tm_sec
        #print("Cursec",curSec)
        #Resets video number to zero if video count >2
        # Only video 0,1,2 are maintained on the device
        if vidNum > 2:
            vidNum = 0
            print("Reset vidNum")
        #If the device is recorsing and the current secont modulo 20 = 0
        # stop recording and set recording boolean to false 
        if recording == True and ((curSec % 20 == 0)):
            counter=0
            print("Stop recording")
            time.sleep(1)
            camera.stop_recording()
            recording = False
        #If recording variable is set to false, befin recording and set
        # recording variable to true
        if recording == False:
            print("start recording")
            camera.start_recording('./images/pivid{}.h264'.format(vidNum))
            vidNum+=1
            recording = True

        #Get current acceleration from sensehat sensor
        acceleration = sense.get_accelerometer_raw()
        #Assign xyz acceleration  values to local variable
        x=abs(round(acceleration['x'], 3)*100)
        y=abs(round(acceleration['y'], 3)*100)
        z=abs(round(acceleration['z'], 3)*100)
        xList[counter] = x
        yList[counter] = y
        zList[counter] = z
        time.sleep(0.25)
        #Pass xyz params to collision function. If collision returns true, continue to record
        recording = collision(averageX,  averageY,  averageZ, maxX, maxY, maxZ, x, y, z)
        averageX=np.average(xList)
        averageY=np.average(yList)
        averageZ=np.average(zList)
        #Standard deviation not used as value wasn't sufficient to detect potential collision
        #stdDevX=np.std(xList)
        #stdDevY=np.std(yList)
        #stdDevZ=np.std(zList)
        maxX = np.amax(xList)
        maxY = np.amax(yList)
        maxZ = np.amax(zList)
        #Counter variable maintains  x,y,z list size
        counter+=1
        if counter > 20:
            counter=0


#autopi_4.1.py

from gpiozero import Button
from gpiozero import LED
from sense_hat import SenseHat
from picamera import PiCamera
import sys
import os
import subprocess
from subprocess import check_call
import shutil
import glob
import numpy as np
import time as time
import datetime
import storeFileFB
import convertFiles
import botbox2
sense = SenseHat()
sense.clear()
sense.set_rotation(270)
camera = PiCamera()
camera.resolution = (1360, 768)
blueLed = LED(17)
greenLed = LED(16)
leds = (blueLed, greenLed)
counter = 0
vidNum = 0
recording = False
xList = [100]*21
yList = [100]*21
zList = [100]*21
averageX, averageY, averageZ=100,100,100
maxX, maxY, maxZ=100,100,100
#stdDevX, stdDevY, stdDevZ=100,100,100


def collision(averageX,  averageY,  averageZ, maxX, maxY, maxZ, x, y, z):
     if recording == True and ((x > (averageX*10)) or (y > (averageY*10)) or (z > (averageZ*10))):
         for led in leds:
           led.blink()
         timeStamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
         print("x",x)
         print("y",y)
         print("z",z)
         print("maxX",maxX)
         print("maxY",maxY)
         print("maxZ",maxZ)
         print("avgX",averageX)
         print("avgY",averageY)
         print("avgZ",averageZ)
         sense.clear(255, 0, 0)
         print("Collision Detected")
         camera.stop_recording()
         convertFiles.updateVideos()
         botbox2.postTelegramPic(timeStamp)
         botbox2.postTelegramVid(timeStamp)
         directory = './images/'
         ext1 = ("jpg")
         ext2 = (".mp4")
         with os.scandir(directory) as imgLib:
           for file in imgLib:
             if file.name.endswith(ext1):
               #and entry.is_file():
               print("Saving to Firebase: ", file.path)
               fileName = file.path
               storeFileFB.pushPhotoDb(fileName, timeStamp)
               storeFileFB.storePhotoFb(fileName)
             elif file.name.endswith(ext2):                                                                                                                                                                                                                   #and entry.is_file():
               print("Saving to Firebase: ", file.path)
               fileName = file.path
               storeFileFB.pushVidDb(fileName, timeStamp)
               storeFileFB.storeVidFb(fileName)
#         for file in glob.glob('./images/*.mp4'):
#           timeStamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
           #shutil.copy(file, './backup')
#           storeFileFB.push_db(file, timeStamp)
#           storeFileFB.store_file(file)
           sense.clear()
           sys.exit("Closing blackbox...")
     else:
     #    print("No accident detected")
         return True

def snapShot():
    fileLoc = f'./images/piPic.jpg'
    timeStamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sense.clear(100, 255, 0)
    print("Pipic taken")
    sense.show_letter("P")
    blueLed.on()
    time.sleep(1)
    blueLed.off()
    camera.capture(fileLoc, use_video_port=True)
    botbox2.postTelegramPic(timeStamp)
    storeFileFB.storePhotoFb(fileLoc)
    storeFileFB.pushPhotoDb(fileLoc, timeStamp)
    sense.clear()

def powerOff():
    print("Power Off")
    sense.clear(100, 100, 100)
    camera.stop_recording()
    sense.show_message("OFF")
    time.sleep(2)
    sense.clear()
    check_call(['sudo', 'poweroff'])

powerOffBtn = Button(18, hold_time=0.5)
powerOffBtn.when_held = snapShot
sense.stick.direction_up = powerOff
sense.stick.direction_down = powerOff
sense.stick.direction_left = powerOff
sense.stick.direction_right = powerOff




while True:
   greenLed.blink()
   while counter < 21:
        curTime =time.gmtime()
        curMin = curTime.tm_min
        curSec = curTime.tm_sec
        if vidNum > 2:
            vidNum = 0
            print("Reset vidNum")
        if recording == True and (curSec % 15 == 0):
            counter=0
            print("Stop recording")
            time.sleep(1)
            camera.stop_recording()
            recording = False
        if recording == False:
            print("start recording")
            camera.start_recording('./images/pivid{}.h264'.format(vidNum))
            vidNum+=1
            recording = True

        acceleration = sense.get_accelerometer_raw()
        x=abs(round(acceleration['x'], 3)*100)
        y=abs(round(acceleration['y'], 3)*100)
        z=abs(round(acceleration['z'], 3)*100)
        xList[counter] = x
        yList[counter] = y
        zList[counter] = z
        time.sleep(0.25)
        recording = collision(averageX,  averageY,  averageZ, maxX, maxY, maxZ, x, y, z)
        averageX=np.average(xList)
        averageY=np.average(yList)
        averageZ=np.average(zList)
        #stdDevX=np.std(xList)
        #stdDevY=np.std(yList)
        #stdDevZ=np.std(zList)
        maxX = np.amax(xList)
        maxY = np.amax(yList)
        maxZ = np.amax(zList)
        print(zList)
        counter+=1
        if counter > 20:
            counter=0

#autopi_3.0.py
#Introduced pi camera functionality
#Video and still image ablity
#File save functionality

from sense_hat import SenseHat
from picamera import PiCamera
from subprocess import call
import shutil
import glob
import numpy as np
import time as time
import datetime
from time import gmtime
sense = SenseHat()
camera = PiCamera()
camera.resolution = (1360, 768)

counter = 0
vidNum = 0
recording = False
xList = [0]*21
yList = [0]*21
zList = [0]*21
averageX,averageY,averageZ=100,100,100

maxX=100
maxY=100
maxZ=100
stdDevX=100
stdDevY=100
stdDevZ=100


def collision(stdDevX, stdDevY, stdDevZ, maxX, maxY, maxZ, x, y, z):
    if (x > (maxX + (stdDevX * 10))) or (y > (maxY + (stdDevY * 10))) or (z > (maxZ + (stdDevZ * 10))):
        sense.clear(255, 0, 0)
        time.sleep(2)
        print("Collision Detected")
        #camera.stop_preview()
        camera.stop_recording()
        #saveLocation = "backup"
        for file in glob.glob('*.h264'):
            print("copying: ", file)
            shutil.copy(file, './backup')
        return False
    else:
        print("No accident detected")
        return True

def snapShot():
    sense.clear(100, 255, 0)
    print("Pipic taken")
    sense.clear()
    camera.capture('piPic.jpg', use_video_port=True)

def powerOff():
    sense.clear(100, 100, 100)
    camera.stop_recording()
    sense.show_message("Powering down...bye")
    time.sleep(2)
    sense.clear()
    call("sudo nohup shutdown -h now", shell=True)
    
sense.stick.direction_left = snapShot
sense.stick.direction_right = snapShot
sense.stick.direction_down = powerOff
sense.stick.direction_up = powerOff
sense.clear()


while True:
    while counter < 21:
        curTime =gmtime()
        curMin = curTime.tm_min
        curSec = curTime.tm_sec
        if vidNum > 2:
            vidNum = 0
            print("Reset vidNum")
        if recording == True and curSec == 59:
            print("Stop recording")
            time.sleep(1)
            #camera.stop_preview()
            camera.stop_recording()
            recording = False
            timeStamp = datetime.datetime.now()
            print(timeStamp)
        if recording == False:
            print("start recording")
            camera.start_recording('pivid{}.h264'.format(vidNum))
            vidNum+=1
            recording = True
            
        acceleration = sense.get_accelerometer_raw()
        x=abs(round(acceleration['x'], 3)*100)
        y=abs(round(acceleration['y'], 3)*100)
        z=abs(round(acceleration['z'], 3)*100)
        xList[counter] = x
        yList[counter] = y
        zList[counter] = z
        recording = collision(stdDevX, stdDevY, stdDevZ, maxX, maxY, maxZ, x, y, z)
        time.sleep(0.5)
        sense.clear()
        averageX=np.average(xList)
        averageY=np.average(yList)
        averageZ=np.average(zList)
        stdDevX=np.std(xList)
        stdDevY=np.std(yList)
        stdDevZ=np.std(zList)
        maxX = np.amax(xList)
        maxY = np.amax(yList)
        maxZ = np.amax(zList)
        counter+=1
        if counter >= 20:
            counter=0






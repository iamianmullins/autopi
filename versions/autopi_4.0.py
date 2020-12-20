#autopi_4.0.py
#Multiple improvements
#Telegram backup functionality added
	#ref: botbox
#Firebase db and storage integration
	#ref: storeFileFB
#File conversion h264 to mp4
	#ref: convertFiles


from sense_hat import SenseHat
from picamera import PiCamera
import sys
import subprocess
import shutil
import glob
import numpy as np
import time as time
import datetime
import storeFileFB
import convertFiles
import botbox2
sense = SenseHat()
sense.set_rotation(270)
camera = PiCamera()
camera.resolution = (1360, 768)
counter = 0
vidNum = 0
recording = False
xList = [0]*21
yList = [0]*21
zList = [0]*21
averageX, averageY, averageZ=100,100,100
maxX, maxY, maxZ=100,100,100
stdDevX, stdDevY, stdDevZ=100,100,100


def collision(stdDevX, stdDevY, stdDevZ, maxX, maxY, maxZ, x, y, z):
     if (x > (maxX + (stdDevX * 2))) or (y > (maxY + (stdDevY * 2))) or (z > (maxZ + (stdDevZ *2))):
         sense.clear(255, 0, 0)
         time.sleep(2)
         print("Collision Detected")
         camera.stop_recording()
         convertFiles.updateVideos()
         botbox2.postTelegram()
         for file in glob.glob('*.mp4'):
           timeStamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
           print("copying: ", file)
           shutil.copy(file, './backup')
           storeFileFB.push_db('./backup', timeStamp)
           storeFileFB.store_file(file)
           sense.clear()
           sys.exit("Closing blackbox...")
     else:
         print("No accident detected")
         return True

def snapShot():
    sense.clear(100, 255, 0)
    print("Pipic taken")
    sense.show_letter("P")
    time.sleep(0.5)
    sense.clear()
    camera.capture('piPic.jpg', use_video_port=True)

def powerOff():
    sense.clear(100, 100, 100)
    camera.stop_recording()
    sense.show_message("OFF")
    time.sleep(2)
    sense.clear()
    call("sudo nohup shutdown -h now", shell=True)




sense.stick.direction_down = snapShot #LEFT
sense.stick.direction_right = snapShot #DOWN
sense.stick.direction_left = powerOff #UP
sense.stick.direction_up = powerOff #RIGHT
sense.clear()


while True:
   while counter < 21:
        curTime =time.gmtime()
        curMin = curTime.tm_min
        curSec = curTime.tm_sec
        if vidNum > 2:
            vidNum = 0
            print("Reset vidNum")
        if recording == True and (curSec % 20 == 0):
            print("Stop recording")
            time.sleep(1)
            camera.stop_recording()
            recording = False
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

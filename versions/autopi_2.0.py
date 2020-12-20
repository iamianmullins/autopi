#autopi_2.0.py
#Collission detection refinement
#Some sensehat joystick functionality
#PoweOff functionality

from sense_hat import SenseHat
from subprocess import call
import numpy as np 
import time as time
sense = SenseHat()

def collision():
    sense.clear(255, 0, 0)
def powerOff(event):
    blue()
    sense.show_message("Powering down...bye")
    time.sleep(2)
    sense.clear()
    call("sudo nohup shutdown -h now", shell=True)

sense.stick.direction_up = collision
sense.stick.direction_middle = powerOff
sense.clear()


while True:
	counter = 0
	xList = [0]*11
	yList = [0]*11
	zList = [0]*11

	averageX=100
	averageY=100
	averageZ=100
	maxX=100
	maxY=100
	maxZ=100
	while counter < 11:

		acceleration = sense.get_accelerometer_raw()
		x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']

		x=abs(round(x, 3)*100)
		y=abs(round(y, 3)*100)
		z=abs(round(z, 3)*100)
		xList[counter] = x
		yList[counter] = y
		zList[counter] = z
		averageX=np.average(xList)
		averageY=np.average(yList)
		averageZ=np.average(zList)
		
		print("x={0}, y={1}, z={2}".format(x, y, z))
		time.sleep(0.5)


		if (x > (maxX * 10)) or (y > (maxY * 10)) or (z > (maxZ * 10)):
			collision()
			print("x={0}, y={1}, z={2}".format(x, y, z))
			#sense.show_message("Collision Detected!!!")
			time.sleep(2)
			sense.clear()
		maxX = np.amax(xList)
		maxY = np.amax(yList)
		maxZ = np.amax(zList)
		if counter >= 10:
			counter=0



#autopi_1.0.py
#Basic functionality
#Collission detection with loop control


from sense_hat import SenseHat
import numpy as np 
import time as time
sense = SenseHat()

while True:
	i=0
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

		i+=1
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
			print("Collision")
			time.sleep(2)
		maxX = np.amax(xList)
		maxY = np.amax(yList)
		maxZ = np.amax(zList)
		if counter >= 10:
			counter=0


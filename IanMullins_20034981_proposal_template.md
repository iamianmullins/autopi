# AutoPi
#### Student Name: *Ian Mullins*   Student ID: *20034981*

##Description
-- Road traffic accident detector/reporter
A sensor based device using Raspberry Pi 3b+ SBC. Intended use is for the automotive domain.
The device should be powered via usb through the vehicle power outlet.
The device will sense and provide enrinonmental data such as vehicle/device orientation using the Raspberry Pi sense hat.
This data will be sent to an IOT platform via HTTP protocol. If the data meets certain criteria such as 
a substantial change in the device orientation in a short period of time eg the vehicle is upside down or pushed/shunted 
someone will be notified there may have been a road traffic accident and prompted to check up on the vehicle owner/driver.

## Tools, Technologies and Equipment
Hardware: 	
			Raspberry pi 3b+
			Sensehat for raspberry pi
			USB to micro USB cable
			Car power outlet to USB adapter
			Mobile phone with tethered internet connection

Technologies: 
			IOT Platform - Thinsgpeak via HTTP request protocol
			React/Notification - Email via IFTTT webhooks service HTTP request on event(potential RTA)

Language:	Python

IDE:		Geany IDE
Editor: 	Nano



## Project Repository
https://github.com/mullins1989/autopi



# AutoPi
#### Student Name: *Ian Mullins*   Student ID: *20034981*

##Description
-- Road traffic accident detector/reporter
A sensor based device using Raspberry Pi 3b+ SBC. Intended use is for the automotive domain.
The device should be powered via usb through the vehicle power outlet.
The device will sense and provide enrinonmental data such as vehicle/device acceleration using the Raspberry Pi sense hat.
This data will be sent to an IOT platform via HTTP protocol. If the data meets certain criteria such as 
a substantial change in the device acceleration in a short period of time eg the vehicle is pushed/shunted/collides with something. 
Someone will be notified there may have been a road traffic accident and prompted to check up on the vehicle owner/driver.

## Tools, Technologies and Equipment
Hardware: 	
			Raspberry pi 3b+
			Raspberry pi camera v2 module
			Sensehat for raspberry pi
			Mini black hat hack3r
			Push buttons
			Leds'
			Jumper wires
			USB to micro USB cable
			Car power outlet to USB adapter
			Mobile phone with tethered internet connection

Technologies: 
            Firebase - realtime DB and cloud storage
			IOT Platform - 	Thinsgpeak via HTTP request protocol
							Wia.io via MQTT protocol
							Blynk restful API				
			React/Notification - Email via IFTTT webhooks service HTTP request on event(potential RTA)

API's:		Openweathermap.org - Used to obtain current location weather for Glitch web app
			Telegram - Telegram BOT API - Messaging, images, location, photo and video
			Google maps API


Languages:	Python
            Bash
            HTML
            CSS
            Javascript

IDE:		Thonny
Editor: 	Nano
            Glitch web application service



## Project Repository
https://github.com/mullins1989/autopi



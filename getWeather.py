#!/usr/bin/python3

import requests
import time


#Return current weather
def getWeather(lat, long):
	url = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=b26824f3dcfff9452e021ea3efe73979".format(lat=lat, long=long)
	response = requests.get(url)
	json = response.json()

	main=json['weather']
	zero=main[0]
	description = zero['main']

	clouds=json['clouds']
	coverage=clouds['all']

	temp=json['main']
	temperature=round((temp['temp']-273.15),2)

	weather=[description,coverage,temperature]
	return weather

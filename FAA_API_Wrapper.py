#!/usr/bin/env python

import urllib2
import json

class UnknownAirportException(Exception):
	def __init__(self, code):
		self.code = code
	def __str__(self):
		error = "The airport code: " + self.code + " is not recognized."
		return repr(self.value)


class NoAirportInCityException(Exception):
	def __init__(self):
		self.code = code
	def __str__(self):
		error = "There is no known airport at the requested city."
		return repr(self.value)



class FAA_API:

	"""
	Example return for LAX airport
	{
			    "IATA": "LAX",
			    "ICAO": "KLAX",
			    "city": "Los Angeles",
			    "delay": "false",
			    "name": "Los Angeles International",
			    "state": "California",
			    "status": {
			        "avgDelay": "",
			        "closureBegin": "",
			        "closureEnd": "",
			        "endTime": "",
			        "maxDelay": "",
			        "minDelay": "",
			        "reason": "No known delays for this airport.",
			        "trend": "",
			        "type": ""
			    },
			    "weather": {
			        "meta": {
			            "credit": "NOAA's National Weather Service",
			            "updated": "9:53 PM Local",
			            "url": "http://weather.gov/"
			        },
			        "temp": "67.0 F (19.4 C)",
			        "visibility": 10.0,
			        "weather": "A Few Clouds",
			        "wind": "West at 8.1mph"
			    	}
				}
"""

	def __init__(self):
		self.code = None
		self.info = None
	
	def get_airport_data(self, airport):
		request_str = "http://services.faa.gov/airport/status/%s.json" % airport
		r = urllib2.urlopen(request_str)
		json_string = r.read()
		self.code = airport
		self.info = json.loads(json_string)
		r.close()
		print "result is:", json.dumps(self.info, indent=4, sort_keys=True)
		return self.info


	def get_airport_IATA(self, airport=None):
		if airport:
			self.get_airport_info(airport)
		if self.info:
			return self.info['IATA']

	def get_airport_ICAO(self, airport=None):
		if airport:
			self.get_airport_info(airport)
		if self.info:
			return self.info['ICAO']

	def get_airport_city(self, airport=None):
		if airport:
			self.get_airport_info(airport)
		if self.info:
			return self.info['city']

	def is_airport_ground_delayed(self, airport=None):
		if airport:
			self.get_airport_info(airport)

		if self.info['delay'] == 'true':
			delay = True
		else:
			delay = False
		return delay
	

	def get_airport_name(self, airport=None):
		if airport:
			self.get_airport_info(airport)
		if self.info:
			return self.info['name']

	def get_airport_state(self, airport=None):
		if airport:
			self.get_airport_info(airport)
		if self.info:
			return self.info['state']

	def get_airport_status(self, airport=None):
		if airport:
				self.get_airport_info(airport)

		if self.info:
			return self.info['status']


	def get_airport_weather(self, airport=None):
		if airport:
			self.get_airport_info(airport)

		if self.info:
			return self.info['weather']


	def get_airport_weather_description(self, airport=None):
		#Returns weather json
		weather = self.info['weather']
		return weather



if __name__ == "__main__":
	client = FAA_API()
	client.get_airport_data("LAX")
	print client.get_airport_IATA()
	print client.get_airport_ICAO()
	print client.get_airport_city()
	print client.is_airport_ground_delayed()
	print client.get_airport_name()
	print client.get_airport_state()
	print client.get_airport_status()
	print client.get_airport_weather()
	print client.get_airport_weather_description()

import json
import turtle
import urllib.request
from helper import *
import time

#get names of astronauts
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read()) #json.loads convert json string to python dictionary
print("The number of people on the space station: {}".format(result["number"]))
people = result["people"]
for p in people:
  print(p["name"])

while(True):
  url = 'http://api.open-notify.org/iss-now.json'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read()) #json.loads convert json string to python dictionary
  #print(type(result))
  #print(result)

  location = result['iss_position']
  #print(location)
  lat = float(location['latitude'])
  #print(type(lat))
  lon = float(location['longitude'])
  #print(type(lon))

  setbackground("map.gif")
  newturtle("iss.gif")
  setheading(90)
  penup()
  goto(lon,lat)
  time.sleep(5)
  #print("{} time through loop".format(i + 1))

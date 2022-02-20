from turtle import * 
from random import randint

screen = Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
# image source:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
#screen.bgpic('map.gif')


# Change background to new image
def setbackground(image): 
  screen.bgpic(image)

# Change turtle to new image 
def newturtle(image): 
  screen.addshape(image)
  shape(image)
  penup()


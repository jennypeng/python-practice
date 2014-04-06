from Turtle import Turtle
from Vector import *
from Color import *
class Circle(Turtle):       #### Inherit behavior from Turtle
    """Represents a circle of radius RADIUS. """
    def __init__(self, position, heading, radius, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.radius = radius
    
    def getshape(self):
        """Return a list of vectors representing circle with a scaling factor
        of SCALE and radius RADIUS."""
        forward = unit(self.heading) # creates a unit of facing degree
        right = unit(self.heading + 90) 
        coords = []
        for i in range(360):
        	degree = unit(self.heading + i)
        	length = self.scale * self.radius # 100 * 1 for diameter of 2 
        	coords.append(self.position + degree * length)
        return coords
       
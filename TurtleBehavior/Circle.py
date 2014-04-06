from Turtle import Turtle
from Vector import *
from Color import *

class Circle(ScalableFigure):       #### Inherit behavior from Turtle
    """Represents a circle. """
    def __init__(self, position, heading, scale, fill=blue, **style):
        ScalableFigure.__init__(self, position, heading, scale, fill=fill, **style)
    
    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        forward = unit(self.heading) # creates a unit of facing degree
        right = unit(self.heading + 90) 
        return [self.position + forward*15,
                self.position - forward*8 - right*8,
                self.position - forward*5,
                self.position - forward*8 + right*8]
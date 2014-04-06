from Turtle import Turtle
from Vector import *
from Color import *

class ScalableFigure(Turtle):       #### Inherit behavior from Turtle
    """Represents a turtle graphic with a choosen scaling factor."""

    def __init__(self, position, heading, scale, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.scale = scale * 100
from Turtle import Turtle
from Vector import *
from Color import *
import math
class Mouse(Turtle):       #### Inherit behavior from Turtle
    """This mouse walks in a straight line forever."""

    def __init__(self, position, speed, orbit, debug_flag, degree, fill=red, **style):
    	heading = (position - orbit.position).direction() - 90 # set degree of mouse to face direction it's heading
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed
        self.orbit = orbit
        self.degree = degree # the degree of location of mouse relative to orbit
        self.debug = debug_flag

    def getnextstate(self):
        """Advance straight ahead."""
        center = self.orbit.position # the center of the circle
        radius = self.orbit.radius # the radius of the circle
        mouse_angle = (self.position - center).direction() # the angle of the mouse relative to the statue ex left = 270 deg
        mouse_x = self.position.x - center.x # mouse x relative to orbit center
        mouse_y = self.position.y - center.y # mouse y relative to orbit center
        rad_change = self.speed * pi/180 # mouse is moving by this many radians
        # (s,t) = (u,v) where u = scos(0) + tsin(0), v = -ssin(0) + tcos(0)
        new_x = mouse_x * math.cos(rad_change) + mouse_y * math.sin(rad_change)
        new_y = -mouse_x * math.sin(rad_change) + mouse_y * math.cos(rad_change)
        self.position = Vector(center.x + new_x, center.y + new_y)
        self.heading = (self.position - center).direction() - 90 #ex: if mouse relative 270, then should be facing 180
        
        return self.position, self.heading

    

        
from Turtle import Turtle
from Vector import *
from Color import *
import math
class Cat(Turtle):       #### Inherit behavior from Turtle
    """The cat walks in a straight line forever."""

    def __init__(self, position, speed, orbit, mouse, arena, radius, debug_flag, degree, fill= yellow, **style):
    	heading = (position - orbit.position).direction() - 90 # set degree of mouse to face direction it's heading
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed
        self.orbit = orbit
        self.degree = degree # the degree of location of mouse relative to orbit
        self.debug = debug_flag
        self.mouse = mouse
        self.cat_rad = radius + self.orbit.radius
        self.moved = -1
        self.arena = arena

    def getAngle(self):
        """ Returns the angle of the cat relative to the statue. EX left = 270"""
        return (self.position - self.orbit.position).direction()

    def reachedCircle(self):
        """ Returns whether the cat has reached the circle or not. """
        print("cat has radius of " + str(self.cat_rad))
        #print("orbit is " + str(self.orbit.radius))
        return float(self.cat_rad) <= float(self.orbit.radius)
    
    def caughtMouse(self):
        """ Returns whether the cat has caught the mouse. """
        #print("cat angle is " + str(float(self.getAngle())))
        #print("mouse angle is " + str(float(self.mouse.getAngle())))
        same_angle = float(self.getAngle()) <= float(self.mouse.getAngle() + 5) and float(self.getAngle()) >= float(self.mouse.getAngle() - 5)
        #print("same angle? " + str(same_angle))
        #print("reached circle?" + str(float(self.cat_rad) <= float(self.orbit.radius)))
        return same_angle and self.reachedCircle()

    def getnextstate(self):
        """Advance straight ahead."""
        sees_mouse = 1.0 <= self.cat_rad * math.cos((self.getAngle() - self.mouse.getAngle()) * pi/180) #does cat see mouse
        #print("cat sees: " + str(sees_mouse))
        center = self.orbit.position # the center of the circle
        radius = self.orbit.radius # the radius of the circle
        if self.caughtMouse():
            self.arena.stop()
            print("Mouse caught.")
        if self.moved == -1 and sees_mouse:
            #print("the cat has seen the cat")
            self.moved = 0
            self.heading = (self.position - center).direction() - 180
        if self.moved >= 0:
            #print("currently moving")
            self.moved += 1
            if self.moved == self.scale:
                #print("reached end of move")
                self.moved = -1
            #print ("moved is " + str(self.moved))
            new_pos = self.position + unit(self.heading)*self.speed
            self.cat_rad = (self.orbit.position - new_pos).length()/self.scale
            if self.reachedCircle():
                self.moved == -1
                return self.position, self.heading # the cat stays still if reached circle
            #print("cat rad is " + str(self.cat_rad)) # cat's radius from center
            else:
                return new_pos, self.heading
        if not sees_mouse and self.moved == -1: # if cat sees the mouse it moves one meter toward statue, else 1.25 counter clockwise
           
            mouse_angle = (self.position - center).direction() # the angle of the mouse relative to the statue ex left = 270 deg
            mouse_x = self.position.x - center.x # mouse x relative to orbit center
            mouse_y = self.position.y - center.y # mouse y relative to orbit center
            rad_change = self.speed * 3.25 * pi/180 # mouse is moving by this many radians
            # (s,t) = (u,v) where u = scos(0) + tsin(0), v = -ssin(0) + tcos(0)
            new_x = mouse_x * math.cos(rad_change) + mouse_y * math.sin(rad_change)
            new_y = -mouse_x * math.sin(rad_change) + mouse_y * math.cos(rad_change)
            self.position = Vector(center.x + new_x, center.y + new_y)
            self.heading = (self.position - center).direction() - 90 #ex: if mouse relative 270, then should be facing 180
            return self.position, self.heading
        # else:
        #     self.heading = (self.position - center).direction() - 180 
        #     new_pos = self.position + unit(self.heading)*self.speed, self.heading
        #     #self.cat_rad = math.hypot(new_pos[0].x - center.x, new_pos[1].y - center.y) - center.radius # find distance between circle outline and cat 
        #     return new_pos
        # self.heading = (self.position - center).direction() - 180 
        # new_pos = self.position + unit(self.heading)*self.speed, self.heading
        #     #self.cat_rad = math.hypot(new_pos[0].x - center.x, new_pos[1].y - center.y) - center.radius # find distance between circle outline and cat 
        # return new_pos
    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward*30,
                self.position - forward*16 - right*16,
                self.position - forward*10,
                self.position - forward*16 + right*16]

    

        
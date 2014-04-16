from Turtle import Turtle
from Vector import *
from Color import *
import math
import doctest
from Circle  import Circle
from Mouse import Mouse
from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena
class Cat(Turtle):       #### Inherit behavior from Turtle
    """The cat walks in a straight line forever."""

    def __init__(self, position, speed, orbit, mouse, arena, radius, debug_flag, degree, fill= yellow, **style):
    	heading = (position - orbit.position).direction() - 90 # set degree of mouse to face direction it's heading
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed
        self.orbit = orbit
        self.degree = degree # the degree of location of cat relative to orbit
        self.debug = debug_flag
        self.mouse = mouse
        self.cat_rad = radius #+ self.orbit.radius
        self.moved = -1  # state represents wheter mouse is seen
        self.arena = arena
        self.iter = 0

    def getAngle(self, debug = False):
        """ Returns the angle of the cat relative to the statue. EX left = 270
        >>> test_cat.getAngle(True)
        Angle is 270
        """
        angle = (self.position - self.orbit.position).direction()
        if debug:
            print("Angle is " + str(angle))
        return angle

    def reachedCircle(self, debug = False):
        """ Returns whether the cat has reached the circle or not. 
        >>> test_cat.reachedCircle(True)
        Cat has not reached the circle.
        """
        print("cat rad is " + str(self.cat_rad))
        print("orbit rad is " + str(self.orbit.radius))
        reached = float(self.cat_rad) <= float(self.orbit.radius)
        if debug and reached:
            print("Cat has reached the circle.")
        print ("reached ? " + str(reached))
        return reached
    
    def caughtMouse(self, debug = False):
        """ Returns whether the cat has caught the mouse. """
        print("cat angle is " + str(self.getAngle()))
        print("mouse angle is " + str(self.mouse.getAngle()))
        same_angle = float(self.getAngle()) <= float(self.mouse.getAngle() + 35) and float(self.getAngle()) >= float(self.mouse.getAngle() - 35)
        print("reached circle " + str(self.reachedCircle()))
        print ("caught mouse? " + str(same_angle and self.reachedCircle()))
        return same_angle and self.reachedCircle()

    def getnextstate(self):
        """Advance straight ahead."""
        print(str(self.iter))
        self.iter += 1
        # does th cat see the mouse?
        sees_mouse = 1.0 <= self.cat_rad * math.cos((self.getAngle() - self.mouse.getAngle()) * pi/180 * self.scale) #does cat see mouse
        
        center = self.orbit.position # the center of the circle
        radius = self.orbit.radius # the radius of the circle
        
        if self.caughtMouse():
            self.arena.stop()
            print("Mouse caught.")

        if self.moved == -1 and sees_mouse: # the cat sees the mouse
            self.moved = 0
            self.heading = (self.position - center).direction() - 180 # makes the cat face direction it's heading
        if self.moved >= 0: # the cat is currently moving
            self.moved += self.scale
            if self.moved == self.scale: # has the cat moved one meter yet?
                self.moved = -1
            new_pos = self.position + unit(self.heading) * self.speed * self.scale
            self.cat_rad = (self.orbit.position - new_pos).length()/self.scale # adjust the new cat radius
            if not self.reachedCircle(): # if the cat has reached the circle
                return new_pos, self.heading
                #self.moved == -1
                #return self.position, self.heading # the cat stays still if reached circle
            else:
                #return new_pos, self.heading
                mouse_angle = (self.position - center).direction() # the angle of the mouse relative to the statue ex left = 270 deg
                mouse_x = self.position.x - center.x # mouse x relative to orbit center
                mouse_y = self.position.y - center.y # mouse y relative to orbit center
                rad_change = self.speed * 1.25 * self.scale * pi/180 # mouse is moving by this many radians
                # (s,t) = (u,v) where u = scos(0) + tsin(0), v = -ssin(0) + tcos(0)
                new_x = mouse_x * math.cos(rad_change) + mouse_y * math.sin(rad_change)
                new_y = -mouse_x * math.sin(rad_change) + mouse_y * math.cos(rad_change)
                self.position = Vector(center.x + new_x, center.y + new_y)
                self.heading = (self.position - center).direction() - 90 #ex: if mouse relative 270, then should be facing 180
                return self.position, self.heading

        if not sees_mouse and self.moved == -1: # if cat sees the mouse it moves one meter toward statue, else 1.25 counter clockwise
           
            mouse_angle = (self.position - center).direction() # the angle of the mouse relative to the statue ex left = 270 deg
            mouse_x = self.position.x - center.x # mouse x relative to orbit center
            mouse_y = self.position.y - center.y # mouse y relative to orbit center
            rad_change = self.speed * 1.25 * self.scale * pi/180 # mouse is moving by this many radians
            # (s,t) = (u,v) where u = scos(0) + tsin(0), v = -ssin(0) + tcos(0)
            new_x = mouse_x * math.cos(rad_change) + mouse_y * math.sin(rad_change)
            new_y = -mouse_x * math.sin(rad_change) + mouse_y * math.cos(rad_change)
            self.position = Vector(center.x + new_x, center.y + new_y)
            self.heading = (self.position - center).direction() - 90 #ex: if mouse relative 270, then should be facing 180
            return self.position, self.heading

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        # forward = unit(self.heading)
        # right = unit(self.heading + 90)
        # return [self.position + forward*30,
        #         self.position - forward*16 - right*16,
        #         self.position - forward*10,
        #         self.position - forward*16 + right*16]
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward*15,
                self.position - forward*8 - right*8,
                self.position - forward*5,
                self.position - forward*8 + right*8]
# def setUpTest(cat_angle, mouse_angle, cat_radius):
#     """ Sets up testing environment for program, using cat_angle, mouse_angle, and cat_radius."""
#     tk = Tk()                              # Create a Tk top-level widget
#     arena = Arena(tk, width = 1000, height = 700)                      # Create an Arena widget, arena
#     arena.pack() 
#     statue = Circle(Vector(200, 200), 0, radius = 1)
#     mouse = Mouse(statue.position + unit(statue.heading + mouse_angle) * statue.radius * statue.scale, speed = 1, orbit = statue, debug_flag = True, degree = mouse_angle)
#     cat = Cat(statue.position + unit(statue.heading + cat_angle) * (statue.radius + cat_radius) * statue.scale, speed = 1, orbit = statue, mouse = mouse, arena = arena, radius = statue.radius + cat_radius, debug_flag = True, degree = cat_angle)
#     doctest.testmod(extraglobs={'test_statue': statue, 'test_mouse': mouse, 'test_cat': cat})

    
if __name__ == "__main__":
    tk = Tk()                              # Create a Tk top-level widget
    arena = Arena(tk, width = 1000, height = 700)                      # Create an Arena widget, arena
    arena.pack() 
    statue = Circle(Vector(200, 200), 0, radius = 1)
    mouse = Mouse(statue.position + mouse_start * statue.radius * statue.scale, speed = 1, orbit = statue, debug_flag = True, degree = 0)
    cat = Cat(statue.position + unit(statue.heading + 270) * (statue.radius + 1) * statue.scale, speed = 1, orbit = statue, mouse = mouse, arena = arena, radius = statue.radius + 1, debug_flag = True, degree = 270)
    doctest.testmod(extraglobs={'test_statue': statue, 'test_mouse': mouse, 'test_cat': cat})


    

        
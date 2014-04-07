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
        of SCALE and radius RADIUS.
        >>> 
        """
        forward = unit(self.heading) # creates a unit of facing degree
        right = unit(self.heading + 90) 
        coords = []
        for i in range(360):
        	degree = unit(self.heading + i)
        	length = self.scale * self.radius # 100 * 1 for diameter of 2 
        	coords.append(self.position + degree * length)
        return coords
# if __name__ == "__main__":
#     tk = Tk()                              # Create a Tk top-level widget
#     arena = Arena(tk, width = 1000, height = 700)                      # Create an Arena widget, arena
#     arena.pack() 
#     statue = Circle(Vector(200, 200), 0, radius = 1)
#     mouse = Mouse(statue.position + mouse_start * statue.radius * statue.scale, speed = 1, orbit = statue, debug_flag = True, degree = 0)
#     cat = Cat(statue.position + unit(statue.heading + 270) * (statue.radius + 1) * statue.scale, speed = 1, orbit = statue, mouse = mouse, arena = arena, radius = statue.radius + 1, debug_flag = True, degree = 270)
#     doctest.testmod(extraglobs={'test_statue': statue, 'test_mouse': mouse, 'test_cat': cat})


       
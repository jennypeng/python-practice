"""
step - moves forward one step in the simulator, 
-- asks each turtle to get its next state
-- -- new_state = turtle.getnextstate()
-- asks each turtle to set their state to next state
-- -- turtle.setstate(new_state) *simulates parallel behavior
run -  loops over step over and over again
stop - stop running
quit - quit the program 
"""

from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from Circle  import Circle             # Import our Turtle
from Mouse import Mouse
from Cat import Cat
from Vector  import *                  # Import everything from our Vector
from random import randrange

tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk, width = 1000, height = 700)                      # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen
'''
Turtle(position, heading, outline, fill, width)
position - vector telling where turtle to be placed
heading - degrees, north = 0, east 90
outline - color, default to black
fill - color of turtle, default white
width - width of outline
'''
def initializeStatue(center_x, center_y, radius):
	"""
	Creates a circular statue centered at CENTER_X and CENTER_Y 
	with a radius of RADIUS.
	Returns the statue
	"""
	statue = Circle(Vector(center_x, center_y), 0, radius = radius)
	arena.add(statue)
	return statue

def initializeMouse(orbit, offset, speed):
	"""
	Creates a mouse which runs around ORBIT, with an OFFSET.
	Returns the mouse.
	"""
	deg = randrange(0, 360, 1) # create a random degree for mouse to start orbit at
	mouse_start = unit(orbit.heading + deg) # what degree to initialize mouse
	mouse = Mouse(orbit.position + mouse_start * (orbit.radius + offset) * orbit.scale, speed = speed, orbit = orbit, debug_flag = True, degree = deg)
	arena.add(mouse)
	return mouse

def initializeCat(mouse, statue, speed):
	cat_rad = 1.9
	#cat_rad = randrange(0, 5, 1) # the cat starts at a random radius
	cat_deg = randrange(0, 360, 1) # the cat starts at a random degree
	cat_start = unit(statue.heading + cat_deg)
	cat = Cat(statue.position + cat_start * (statue.radius + cat_rad) * statue.scale, speed = speed, orbit = statue, mouse = mouse, arena = arena, radius = statue.radius + cat_rad, debug_flag = True, degree = cat_deg)
	arena.add(cat)
	return cat
statue = initializeStatue(500, 350, 1.0)
mouse = initializeMouse(statue, 0, 1)
cat = initializeCat(mouse, statue, 1)


tk.mainloop()   

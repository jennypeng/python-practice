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
from Vector  import *                  # Import everything from our Vector
from random import randrange

tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk)                      # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen
'''
Turtle(position, heading, outline, fill, width)
position - vector telling where turtle to be placed
heading - degrees, north = 0, east 90
outline - color, default to black
fill - color of turtle, default white
width - width of outline
'''
                       
def initializeMouse(orbit, offset):
	deg = randrange(0, 360, 1)
	print("deg is " + str(deg))
	mouse_start = unit(statue.heading + deg) # what degree to initialize mouse
	arena.add(Mouse(statue.position + mouse_start * (statue.radius + offset) * statue.scale, speed = 1, orbit = statue, debug_flag = True, degree = deg))

statue = Circle(Vector(200,200), 0, radius = 1)
arena.add(statue)
initializeMouse(statue, 0.3)


tk.mainloop()   

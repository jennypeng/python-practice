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
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector

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
arena.add(Turtle(Vector(200,200), 0))  # Add a very simple, basic turtle
tk.mainloop()                          # Enter the Tkinter event loop

"""
Sometimes its a good idea to wrap code in one or more classes
"""
from Tkinter import * 

class App:
	def __init__(self, master):
		frame = Frame(master) # a frame is a simple container, to hold other widgets 
		frame.pack() # call pack to make frame visible

		self.button = Button( # fg = foreground
			frame, text="QUIT", fg="red", command=frame.quit
			)
		self.button.pack(side=LEFT) # pack returns none

		self.hi_there = Button(frame, text="Hello", command=self.say_hi)
		self.hi_there.pack(side=LEFT)
	def say_hi(self):
		print "hi there, everyone!"
root = Tk()
app = App(root)

root.mainloop()




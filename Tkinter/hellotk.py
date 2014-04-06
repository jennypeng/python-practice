from Tkinter import * # import everything into module namespace
# root must be initialized before any other widgets
root = Tk() # root widget, ordinary window, only one root widget per program
#create a label as a child to the root window
w = Label(root, text = "Hello, world!") # use text optioin to specify which text to display
w.pack() # pack to tell the widget to sie itself to fit the given text. 

root.mainloop() # start tkinter event loop 

# the event loop handles user interaction and also tkinter operations. 
from Tkinter import *
from math import sin, cos, pi
from Vector import *
import copy

class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""

    def __init__(self, parent, width=400, height=400, **options):
        Frame.__init__(self, parent, **options)
        self.width, self.height = width, height
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        self.time = 0
        parent.title("UC Bereley CS9H Turtle Arena")
        Button(self, text='step', command=self.step).pack(side=LEFT)
        Button(self, text='run', command=self.run).pack(side=LEFT)
        Button(self, text='stop', command=self.stop).pack(side=LEFT)
        Button(self, text='quit', command=parent.quit).pack(side=LEFT)
        Button(self, text='reset', command=self.reset).pack(side=LEFT)
        # create labels
        self.time_str = StringVar()
        #v.set("wefaewfaef")
        Label(self, textvariable = self.time_str).pack(side=LEFT) # how many steps
        Label(self, text='CatRadius: ').pack(side=LEFT)
        Label(self, text='CatAngle: ').pack(side=LEFT)
        Label(self, text='MouseAngle: ').pack(side=LEFT)
        self.time_str.set("Time: " + str(self.getTime()))
        # create menu
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        #menubar.add_command(label='File') # when selected shows About... and Quit 
        filemenu.add_command(label='About...')
        filemenu.add_command(label='Quit', command=parent.quit)
        menubar.add_cascade(label='File', menu=filemenu)
        parent.config(menu=menubar)
        self.turtles = []
        self.original_turtles = []
        self.items = {}
        self.running = 0
        self.period = 10 # milliseconds
        self.canvas.bind('<ButtonPress>', self.press)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<ButtonRelease>', self.release)
        self.dragging = None
        #self.time = 0
    def getTime(self):
        ''' Returns the time elapsed. '''
        return self.time

    def press(self, event):
        dragstart = Vector(event.x, event.y)
        for turtle in self.turtles:
            if (dragstart - turtle.position).length() < 10:
                self.dragging = turtle
                self.dragstart = dragstart
                self.start = turtle.position
                return

    def motion(self, event):
        drag = Vector(event.x, event.y)
        if self.dragging:
            self.dragging.position = self.start + drag - self.dragstart
            self.update(self.dragging)

    def release(self, event):
        self.dragging = None

    def update(self, turtle):
        """Update the drawing of a turtle according to the turtle object."""
        item = self.items[turtle]
        vertices = [(v.x, v.y) for v in turtle.getshape()]
        self.canvas.coords(item, sum(vertices, ()))
        self.canvas.itemconfigure(item, **turtle.style)

    def add(self, turtle):
        """Add a new turtle to this arena."""
        self.turtles.append(turtle)
        self.original_turtles.append(copy.copy(turtle)) # we add the turtle a
        self.items[turtle] = self.canvas.create_polygon(0, 0)
        self.update(turtle)

    def step(self, stop=1):
        """Advance all the turtles one step."""
        nextstates = {}
        for turtle in self.turtles:
            nextstates[turtle] = turtle.getnextstate()
            #self.time += 1
            self.time_str.set("Time: " + str(self.getTime()))
            self.time += 1
        for turtle in self.turtles:
            turtle.setstate(nextstates[turtle])
            self.update(turtle)
        if stop:
            self.running = 0
    def reset(self):
        new_turtles = []
        for turtle in self.original_turtles:
            new_turtles.append(turtle)
        self.turtles = new_turtles

        #self.turtles = self.original_turtles
        #self.turtles = copy.copy(self.original_turtles) # need to make deep copy, turtle info isn't changing.
        self.stop()

    def run(self):
        """Start the turtles running."""
        self.running = 1
        #self.original_turtles = copy.copy(self.turtles)
        self.loop()

    def loop(self):
        """Repeatedly advance all the turtles one step."""
        self.step(0)
        if self.running:
            self.tk.createtimerhandler(self.period, self.loop)

    def stop(self):
        """Stop the running turtles."""
        self.running = 0
        self.time = 0
        self.time_str.set("Time: " + str(self.getTime()))


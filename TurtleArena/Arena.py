from Tkinter import *
from math import sin, cos, pi
from Vector import *
import copy
from Color import *

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
        #rest
        Button(self, text='reset', command=self.reset).pack(side=LEFT)
        # create labels
        self.time_str = StringVar()
        self.cat_rad = StringVar()
        self.cat_ang = StringVar()
        self.mouse_ang = StringVar()
        #v.set("wefaewfaef")
        #timelabel
        Label(self, textvariable = self.time_str).pack(side=LEFT) # how many steps
        #cat radius
        Label(self, textvariable=self.cat_rad).pack(side=LEFT)
        #cat angle
        Label(self, textvariable=self.cat_ang).pack(side=LEFT)
        #mouse angle
        Label(self, textvariable=self.mouse_ang).pack(side=LEFT)
        # create menu
        var = IntVar()

        c = Checkbutton(master, text="Expand", variable=var)
        c.pack()
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        #menubar.add_command(label='File') # when selected shows About... and Quit 
        filemenu.add_command(label='About...', command=self.about)
        filemenu.add_command(label='Quit', command=parent.quit)
        menubar.add_cascade(label='File', menu=filemenu)
        parent.config(menu=menubar)

        self.turtles = []
        self.items = {}
        self.running = 0
        self.period = 10 # milliseconds
        self.canvas.bind('<ButtonPress>', self.press)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<ButtonRelease>', self.release)
        self.dragging = None
        
        #self.time = 0
    def about(self):
        ''' creates about menu '''
        top = Toplevel()
        top.title("About this application...")
        about_message = ""
        msg = Message(top, text=about_message)
        msg.pack()
        photo = PhotoImage(file="turtle.gif")
        pic = Label(top, image=photo).pack(side=TOP)
        Label(top, text='Turtle Arena - Jenny').pack(side=TOP)

        button = Button(top, text="Okay", command=top.destroy)
        button.pack()
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
        print("motion happening")
        cat = self.turtles[2]
        statue = self.turtles[1]
        drag = Vector(event.x, event.y)
        print(str(event.x) + " " + str(event.y))
        print("cat" + str(cat.position.x) + " " + str(cat.position.y))
        if (drag - cat.position).length() < 10:
            cat.style['fill'] = black
        else:
            cat.style['fill'] = yellow
        self.update(cat)
        if self.dragging:
            self.dragging.position = self.start + drag - self.dragstart
            cat.position = self.dragging.position
            cat.heading = (cat.position - cat.orbit.position).direction() - 180
            cat.cat_rad = (cat.orbit.position - cat.position).length()/30
            self.cat_rad.set("CatRadius: " + str(cat.getRadius()))
            self.cat_ang.set("CatAngle: " + str(cat.getAngle()))
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
        self.items[turtle] = self.canvas.create_polygon(0, 0)
        self.update(turtle)

    def step(self, stop=1):
        """Advance all the turtles one step."""
        nextstates = {}
        for turtle in self.turtles:
            nextstates[turtle] = turtle.getnextstate()
            
            self.time += 1
        for turtle in self.turtles:
            turtle.setstate(nextstates[turtle])
            self.update(turtle)
        if stop:
            self.running = 0
        self.setLabels()
    def setLabels(self):
        mouse = self.turtles[1]
        cat = self.turtles[2]
        self.time_str.set("Time: " + str(self.getTime()))
        self.cat_rad.set("CatRadius: " + str(cat.getRadius()/30))
        self.cat_ang.set("CatAngle: " + str(cat.getAngle()))
        self.mouse_ang.set("MouseAngle: " + str(mouse.getAngle()))

    def reset(self):
        self.time = 0
        self.running = 0
        for turtle in self.turtles:
            turtle.setstate(turtle.getfirststate())
            self.update(turtle)

    def run(self):
        """Start the turtles running."""
        self.running = 1
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


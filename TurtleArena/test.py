from Tkinter import *
clicks=0

def clicker():
    global clicks
    clicks += 1
    lab.config(text=clicks)

Button(text="Click me", command=clicker).pack()
lab = Label(text=clicks)
lab.pack(side=LEFT)
Label(text=" clicks").pack(side=LEFT)

mainloop()
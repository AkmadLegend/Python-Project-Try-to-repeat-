import tkinter
import tkinter.messagebox
import turtle
from tkinter import *
top=tkinter.Tk()
t=turtle.Pen()
currenttcolour="red"
brushsize=10

def Upgrade_colour(colour):
    global currenttcolour
    currenttcolour=colour
def Upgrade_size(size):
    global brushsize
    brushsize=size

def hello():
    master=tkinter.Toplevel(top)
    master.title("paint")
    canvas = Canvas(master, width=500, height=500, bg="black")
    canvas.pack()
    redbutton = Button(master, text="Red", command=lambda: Upgrade_colour("red"))
    redbutton.pack(side=LEFT)

    orangebutton = Button(master, text="Orange", command=lambda: Upgrade_colour("orange"))
    orangebutton.pack(side=LEFT)

    yellowbutton = Button(master, text="Yellow", command=lambda: Upgrade_colour("yellow"))
    yellowbutton.pack(side=LEFT)

    greenbutton = Button(master, text="Green", command=lambda: Upgrade_colour("green"))
    greenbutton.pack(side=LEFT)

    smallbutton = Button(master, text="small", command=lambda: Upgrade_size(1))
    smallbutton.pack(side=RIGHT)
    mediumbutton = Button(master, text="medium", command=lambda: Upgrade_size(5))
    mediumbutton.pack(side=RIGHT)
    largebutton = Button(master, text="large", command=lambda: Upgrade_size(10))
    largebutton.pack(side=RIGHT)
    def draw(event):
        x, y = event.x, event.y
        canvas.create_oval(x - brushsize, y - brushsize, x + brushsize, y + brushsize, fill=currenttcolour, outline="")

    canvas.bind("<B1-Motion>", draw)
    master.mainloop()

w = tkinter.Button(top,text="Try to repeat.",command=hello)
w.pack()
for x in range(1000000000):
    t.forward(x)
    #t.circle(x)
    t.left(90)
    t.right(1000)
    t.speed(10000000000000000000000)
turtle.pack()



top.mainloop()
turtle.mainloop()

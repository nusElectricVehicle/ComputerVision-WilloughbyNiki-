from tkinter import *
import tkinter as tk

import tkinter.messagebox
import tkinter.font as font
import cv2
import d
import math

#myFont = font.Font(family='Helvetica')

root = tk.Tk() #the initialisation of the window
root.title("NUS Eco Car") #the title of the window
root.geometry("300x200") #the size of the window (in pixels) rmbr its a string

def scaledChoice():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)
   
def helloCallBack():
    tkinter.messagebox.showinfo("Hello Python", "Hello World")
    print("Hello button pressed")

def openFile():
    capture = cv2.VideoCapture(0)
    dddd = tk.Tk() #the initialisation of the window
    dddd.title("NUS")
    dddd.after(300, lambda: dddd.destroy()) # Destroy the widget after 30 seconds
    
    _, frame = capture.read()
        
    if _:
        cv2.imshow("Frame", frame)

def getSquareRoot():
    print(entry1)
    x = entry1.get()
    y = float(x)
    print(math.sqrt(y))

w = tk.Label(root, text="Hello Tkinter!")
e = tk.Button(root,
              text ="Snap Picture",
              #font=myFont,
              bg='orange',
              fg='black',
              command = openFile)

checkStats = tk.Button(root,
              text ="Car Statistics",
              #font=myFont,
              bg='orange',
              fg='black',
              command = helloCallBack)

var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(padx=5, pady=10, side=tk.LEFT)

button = Button(root, text = "Get Scale Value", command = scaledChoice)
button.pack(padx=5, pady=20, side=tk.LEFT)


track = Scale(root, from_=0, to=42)
track.pack(anchor = CENTER)
ttraa = tk.Scale(root, from_=0, to=200, orient=HORIZONTAL)
ttraa.pack()

entry1 = tk.Entry(root)
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)

print(entry1)
print(e)
w.pack()
e.pack()
checkStats.pack()
entry1.pack()
button1.pack()


root.mainloop()

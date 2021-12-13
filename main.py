# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:28:54 2020

@authors: Emily and Lili 
"""

import tkinter as tk 
from functools import partial 
import math 
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Cylinder class
class Cylinder(): 
    # constructor method to create a cylinder with a radius of r and a height of h
    # the height and radius will grow similarly as the volume/SA/radius changes (hence the ratio)
    def __init__(self,r,h): 
        self.r = r
        self.h = h
        self.ratio = self.h / self.r
    
    # calculates the function of the rate of change of the volume with respect to the radius
    def changeInVolume(self, changeinr): 
        dv = lambda r: math.pi * self.ratio * 3 * r**2 * changeinr
        return dv
    
    # calculates the function of the rate of change of the surface area with respect to the radius
    def changeInSA(self, changeinr): 
        dSA = lambda r: (4 * math.pi * r) * (changeinr + self.ratio * changeinr)
        return dSA
    
    # calculates the function of the rate of change of the radius with respect to the radius
    def changeInRadius(self, volumeChange):
        dr = lambda r: volumeChange / (3 * math.pi * self.ratio * r**2) 
        return dr

 
# Sphere class
class Sphere(): 
    
    # constructor rmethod to create a sphere with a radius of r
    def __init__(self, r):
        self.r = r
    
    # calculates the function of the rate of change of the volume with respect to the radius
    def changeInVolume(self, changeinr): 
        dv = lambda r: 4 * math.pi * r**2 * changeinr
        return dv
    
    # calculates the function of the rate of change of the surface area with respect to the radius
    def changeInSA(self, radiusChange):
        dSA = lambda r: 8 * math.pi * r * radiusChange
        return dSA
    
    # calculates the function of the rate of change of the radius with respect to the radius
    def changeInRadius(self, volumeChange):
        dr = lambda r: volumeChange / (4 * math.pi * r ** 2)
        return dr


# Cone class    
class Cone():
    # constructor method to create a cone with a height of h and a raidus of r
    # the height and radius will grow similarly as the volume/SA/radius changes (hence the ratio)
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.ratio = self.h / self.r
    
    # calculates the function of the rate of change of the volume with respect to the radius
    def changeInVolume(self, radiusChange):
        dv = lambda r: math.pi * self.ratio * r**2 * radiusChange
        return dv
    
    # calculates the function of the rate of change of the surface area with respect to the radius
    def changeInSA(self, radiusChange):
        dSA = lambda r: (2 * math.pi * r * radiusChange) + (2 * r * math.pi * math.sqrt(self.ratio**2 + 1) * radiusChange)
        return dSA
    
    # calculates the function of the rate of change of the radius with respect to the radius
    def changeInRadius(self, volumeChange):
        dr = lambda r: volumeChange / (self.ratio * math.pi * r**2)
        return dr


# Cube class
class Cube():
    # constructor that creates a cube with a side length of l
    def __init__(self, l):
        self.l = l

    # calculates the function of the rate of change of the volume with respect to the length
    def changeInVolume(self, lengthChange):
        dv = lambda l: 3 * l ** 2 * lengthChange
        return dv

    # calculates the function of the rate of change of the surface area with respect to the length    
    def changeInSA(self, lengthChange):
        dSA = lambda l: 12 * l * lengthChange
        return dSA

    # calculates the function of the rate of change of the length with respect to the length    
    def changeInLength(self, volumeChange):
        dl = lambda l: volumeChange / (3 * l ** 2)
        return dl
    



# creating the GUI window and resizing it
window = tk.Tk()
window.geometry("1000x1000")
window['background'] = '#D2F4FF'


# welcome message
welcome = tk.Label(text = "Welcome to Lili and Emily's Related Rates Program!", justify = "center")
welcome.place(x = 10, y = 5)

        
    
# Figures Section where the user selects the figure they want from a dropdown menu
objectLabel = tk.Label(text = "Choose a figure!")
objectLabel.place(x = 10, y = 30)
option = tk.StringVar(window)
option.set('Figures') # set the default option
menu = tk.OptionMenu(window, option, 'Cylinder','Sphere','Cone', 'Cube')
menu.place(x=10, y = 60)


# Quantity Section where the user selects the quantity they want to caclulate from a dropdown menu
quantitylabel = tk.Label(text = "Quantity to find the rate of change for")
quantitylabel.place(x = 10, y = 90)
quantity = tk.StringVar(window)
quantity.set("Quantities")
quantitymenu = tk.OptionMenu(window, quantity, 'Volume', 'Surface Area', 'Radius', 'Length')
quantitymenu.place(x=10, y = 110)



# Value Section where the user enters the values needed to caclulate the quantity
valuelabel = tk.Label(text = "Please use only the text boxes applicable.")

# Volume label and text entry section
valuelabel1 = tk.Label(text = "Change in Volume")
volumeentry = tk.Entry(window)
volumeentry.place(x = 130, y = 170)

# Radius label and text entry section
valuelabel2 = tk.Label(text = "Change in Radius")
radiusentry = tk.Entry(window)
radiusentry.place(x = 130, y = 190)

# Length label and text entry section
valuelabel3 = tk.Label(text = "Change in Length")
lengthentry = tk.Entry(window)

# Placing all of the labels/text entry boxes in the window
lengthentry.place(x = 130, y = 210)
valuelabel.place(x = 10, y = 150)
valuelabel1.place(x = 10, y = 170)
valuelabel2.place(x = 10, y  = 190)
valuelabel3.place(x = 10, y = 210)



#Current Value section where the user enters the value of the radius/length/height of the initial figure

# radius/length label and entry box
currentValueLabel = tk.Label(text = "Enter the current value of the radius/length.")
currentValueLabel.place(x = 10, y = 250)
currententry = tk.Entry(window)
currententry.place(x= 10, y = 270)

# height label and entry box
heightValueLabel = tk.Label(text = "Enter the current value of the height if applicable.")
heightValueLabel.place(x = 10, y = 300)
heightEntry = tk.Entry(window)
heightEntry.place(x = 10, y = 320)



# function called when the enter buttin is pressed
# the function displays the graph of the rate of change selected near the initial radius/length
# the function displays the rate of change at the initial radius/height 
def getInfo(message, e1, e2, e3, e4, e5): 
    # get the name of the figure and the quantity selected
    figure = option.get()
    quantityy = quantity.get()
    
    # default function that is later updated
    f = lambda x:  x

    xLabel = "Radius"   # default label of the x-axis
    currentX = float(e4.get())  # initial radius/length
    
    #Cube is chosen 
    if( figure == "Cube"): 
        length = currentX
        cube = Cube(length) #creating the cube with length entered
        xLabel = "Length"
        if(quantityy == "Volume"):  # if volume chosen
            dlength = float(e3.get())
            f = cube.changeInVolume(dlength)
            
        if quantityy == "Surface Area": # if surface area chosen
            dlength = float(e3.get())
            f = cube.changeInSA(dlength)
            
        if quantityy == "Length":   # if length chosen
            dvolume = float(e1.get())
            f = cube.changeInLength(dvolume)
            
    elif (figure == "Cylinder") :   # if cylinder chosen
        radius = currentX
        height = float(e5.get())
        cylinder = Cylinder(radius,height)  # creating the cylinder with radius and height entered
        
        if(quantityy == "Volume"):   # if volume chosen
            dRadius = float(e2.get())
            f = cylinder.changeInVolume(dRadius)
        
        if(quantityy == "Surface Area"):    # if surface area chosen
            dRadius = float(e2.get())
            f = cylinder.changeInSA(dRadius)
            
        if(quantityy == "Radius"):  # if radius chosen
            dVolume = float(e1.get())
            f = cylinder.changeInRadius(dVolume)
            

    elif (figure == "Sphere"):  # if sphere chosen
        radius = currentX
        
        sphere = Sphere(radius) # creating the sphere with the entered radius
        if(quantityy == "Volume"):  # if volume chosen
            dRadius = float(e2.get())
            f = sphere.changeInVolume(dRadius)
        
        if(quantityy == "Surface Area" ):   # if surface area chosen
            dRadius = float(e2.get())
            f = sphere.changeInSA(dRadius)
        
        if(quantityy == "Radius"):   # if radius chosen
            dVolume = float(e1.get())
            f = sphere.changeInRadius(dVolume)
        
    #Cone Selected
    else : 
        cone = Cone(currentX, float(e5.get()))  # creating the cone with the entered radius and height
        if(quantityy == "Volume"):  # if volume chosen
            dRadius = float(e2.get())
            f = cone.changeInVolume(dRadius)
        
        if(quantityy == "Surface Area"):    # if surface area chosen
            dRadius = float(e2.get())
            f = cone.changeInVolume(dRadius)
            
        if(quantityy == "Radius"):  # if radius chosen
            dVolume = float(e1.get())
            f = cone.changeInRadius(dVolume)
            
    # making sure that the radius/ length is positive and a divide by zero error does not occur        
    if(currentX-10<0): 
        currentX = 11
    
    
    # plotting the rate of change function
    # making the x-axis range from ten before the initial radius/length to ten after    
    x = np.linspace(currentX - 10, currentX + 10, 10)
     
    ylabel = "Change in " +  quantityy   
    figure = Figure(figsize = (6, 5), dpi = 100)
    plot = figure.add_subplot(1,1,1)
    canvas = FigureCanvasTkAgg(figure, window)
    canvas.get_tk_widget().place(x = 400, y = 0)
    plot.set_xlabel(xLabel)
    plot.set_ylabel(ylabel)
    plot.set_title("Rate of Change")
    plot.plot(x, [f(i) for i in x])
    
    # displaying the rate of change at the the initial value on the graph and in text
    message.config(text = "The rate of change at " + str(e4.get()) + " is " + str(f(float(e4.get()))) )
    plot.plot(float(e4.get()), f(float(e4.get())), 'bo')
    
    

# setting up the message that will display the rate of change at the inital radius/length        
message = tk.Label()
displayanswer = partial(getInfo, message, volumeentry, radiusentry, lengthentry, currententry, heightEntry)
message.place(x = 10, y = 500)

# the enter button
enterbutton = tk.Button(window, text = "Enter", command = displayanswer)
enterbutton.place(x=10, y=400)
    
# running the tkinter window
window.mainloop()

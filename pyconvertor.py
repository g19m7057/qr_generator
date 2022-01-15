import tkinter
from tkinter import *
from tokenize import String

# first window
m = tkinter.Tk() #creates the window
m.title("unit convertor") #window title

#units for selection
units = ["inches", "centimeters"] #, "kilograms", "pounds", "yards", "feet"]

# unit to convert from
unit1 = tkinter.StringVar(m) #the var the selected unit will be stored in
unit1.set("convert from") # placeholder text

# unit to convert to
unit2 = tkinter.StringVar(m)
unit2.set("convert to")

# dropdown menu for the first unit
# OptionMenu(window, optionSelectedVariable, theOPtions2Select)
drop1 = tkinter.OptionMenu(m, unit1, *units) 

# pack( pack_options ) is a geometry mananger 
# that organises widgets into blocks
drop1.pack() 

# dropdown menu for the second unit
drop2 = tkinter.OptionMenu(m, unit2, *units)
drop2.pack()

# callled to print the option selected
def pr():
    print(unit1.get()) # gets the value selected
    print(unit2.get())
    print(e.get())

# text widget to display result


# the number to convert
e = Entry(m, width = 5)
e.pack()

# Functionality
# convert inch to centimeter


def con():
    # second window
    sw = tkinter.Tk()
    sw.title("result of your convetion")

    if(unit1.get() == "centimeters"):
        if(unit2.get() == "inches"):
            l = tkinter.Label(sw, height = 3, text = float(e.get())/2.54)
    else:
        l = tkinter.Label(sw, height = 3, text = float(e.get())*2.54)
    l.pack()    
    
    exit_button = tkinter.Button(sw, text="exit", command = m.destroy)
    exit_button.pack()

#button to submit 
submit_button = tkinter.Button(m, text='Submit', command = con and m.destroy)
submit_button.pack()

exit_button = tkinter.Button(m, text="exit", command = m.destroy)
exit_button.pack()

m.mainloop()
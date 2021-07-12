# Importing Modules :-

from tkinter import *  # For GUI
from tkinter.ttk import *  # For GUI
from time import strftime  # For Calculating and Displaying the Time


# Defining a Function to Display the Time using the Time Module :-

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


# Creating a Basic GUI :-

root = Tk()  # Creating an instance of Tk Class
root.title("Clock")  # Creating Title


# Displaying the time in the Window in the Form of a Label
label = Label(root, font=("Arial", 80), background="black", foreground="cyan")
label.pack(anchor='center')

# Calling the Time Function
time()

# Creating MainLoop
root.mainloop()

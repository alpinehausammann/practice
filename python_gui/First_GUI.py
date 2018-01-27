import tkinter as tk

# ttk("themed tk") generates better looking widgets
from tkinter import ttk


#initializes window frame
win = tk.Tk()

# Adds a title to window
win.title("First Python GUI")

# Disable resizing of window
# First false is x dimension and second is y.
### win.resizable(False,False)

# Creates a label. First argument selects frame
first_label = ttk.Label(win, text="A label")
first_label.grid(column=0, row=0)

def click_me():
    """Controls event on click"""
    action.configure(text="I've been clicked!")
    first_label.configure(foreground="red")
    first_label.configure(text="A red label")

def on_click():
action = ttk.Button(win, text="click me!", command=click_me)
action.grid(column=2, row=0)
# Starts the window frame
win.mainloop()

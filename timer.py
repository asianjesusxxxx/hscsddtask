# Import necessary modules
from tkinter import *
import tkinter as tk
import time

# Create the Tkinter root window
root = Tk()
root.title('Timer')
root.geometry("300x200")


counting = False

def count_down(sec):
    global counting
    counting = True
    while sec:
        mins, secs = divmod(sec, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs)
        second_var.set(time_format)
        time.sleep(1)
        sec = sec - 1
    print("stop")


# Create a StringVar to hold the time value
second_var = tk.StringVar(value='00:00')

# Create a Label to display the timer
second_lbl = tk.Label(root, font=('Arial', 50), textvariable=second_var)
second_lbl.pack()

# Define a function to start the countdown
def start_countdown():
    count_down(10)  # Change 10 to the desired countdown time in seconds

# Create a button to start the countdown
start_btn = Button(root, text="Start Countdown", command=start_countdown)
start_btn.pack()

# Run the Tkinter event loop
root.mainloop()

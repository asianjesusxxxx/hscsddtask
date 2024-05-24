import tkinter as tk
import tkinter as ttk
import time 

root = tk.Tk()

counting = False

def conut_down():
    counting = True
    

second_var = tk.StringVar(value=' 00 ')

second_lbl = tk.Label(font=('Arial', 50), textvariable=second_var)

second_lbl.grid(row=0, column=0)



root.mainloop()
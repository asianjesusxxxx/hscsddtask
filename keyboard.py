# from tkinter import *


# root = Tk()

# page1 = Frame(root)
# page2 = Frame(root)

# page1.grid(row=0, column=0)
# page2.grid(row=0, column=0)

# page2.forget()


# def clicked(event):
#     print("you pressed enter")
#     page1.forget()
#     lambda: page2.tkraise()
#     page2.grid(row=0, column=0)

    

# page1.bind("<Return>", clicked)

# label = Label(page1, text="press enter")
# label.grid(row=0, column=1)

# label2 = Label(page2, text="you pressed")

# root.mainloop()

from tkinter import *

root = Tk()

page1 = Frame(root)
page2 = Frame(root)

page1.grid(row=0, column=0)
page2.grid(row=0, column=0)

page2.forget()  # This is actually not necessary and can be removed

def clicked(event):
    print("you pressed enter")
    page1.forget()
    page2.tkraise()

root.bind("<Return>", clicked)

label = Label(page1, text="press enter")
label.grid(row=0, column=1)

label2 = Label(page2, text="you pressed")
label2.grid(row=0, column=1)

page1.tkraise()  # Ensure page1 is visible at start

root.mainloop()

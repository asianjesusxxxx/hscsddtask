from tkinter import *
from tkinter import ttk
import tkinter as tk 
from gtts import gTTS
from io import BytesIO
import pygame
from PIL import ImageTk, Image 
import customtkinter 


root = customtkinter.CTk()
root.title('triangles')
# root.geometry("2000x600")
# root.state('zoomed')
# root.resizable(False, False) 

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

width = root.winfo_screenwidth()
height = root.winfo_screenheight() 

#creating all frames
openpage = customtkinter.CTkFrame(root, width=1000, height=600)
page1 =  customtkinter.CTkFrame(root, width=1000, height=600)
page2 =  customtkinter.CTkFrame(root, width=1000, height=600)
page3 =  customtkinter.CTkFrame(root, width=1000, height=600)
page4 =  customtkinter.CTkFrame(root, width=1000, height=600)
page5 =  customtkinter.CTkFrame(root, width=1000, height=600)
page6 =  customtkinter.CTkFrame(root, width=1000, height=600)
page7 =  customtkinter.CTkFrame(root, width=1000, height=600)
page8 =  customtkinter.CTkFrame(root, width=1000, height=600)

def changemode():
    val=switch.get()
    if val:
        customtkinter.set_appearance_mode("dark")
        switch.configure(text="dark mode")
    else:
        customtkinter.set_appearance_mode("light")
        switch.configure(text="light mode")


switch = customtkinter.CTkSwitch(page1, text="", 
                   onvalue=1,
                   offvalue=0,
                   command=changemode)

switch = customtkinter.CTkSwitch(page2, text="", 
                   onvalue=1,
                   offvalue=0,
                   command=changemode)

switch.grid(row=0, column=3)
print(switch.get())

customtkinter.set_appearance_mode("light")
switch.configure(text="light mode")
customtkinter.set_default_color_theme("dark-blue")


#using grid to place the frames onto the gui
openpage.grid(row=0,column=0)
openpage.configure(width=1000, height=600)
openpage.grid_propagate(False)

#using grid_forget() so that only openpage will be displayed
page1.grid_forget()
page2.grid_forget()
page3.grid_forget()
page4.grid_forget()
page5.grid_forget()
page6.grid_forget()
page7.grid_forget()
page8.grid_forget()

#setting initial font size and colour
default_font = ("Arial", 30)

#defining function to change font size
def change_font_size(event):
    size = int(selected_size.get())
    t1.configure(font=("Arial", size))
    t2.configure(font=("Arial", size))
    butt1.configure(font=("Arial", size))
    sbutt3.configure(font=("Arial", size))
    bbutt1.configure(font=("Arial", size))
    fontsize_combo1.configure(font=("Arial", size))
    fontsize_combo2.configure(font=("Arial", size))
    playbutt1.configure(font=("Arial", size))
    playbutt2.configure(font=("Arial", size))
    playbutt3.configure(font=("Arial", size))
    playbutt4.configure(font=("Arial", size))
    playbutt5.configure(font=("Arial", size))
    playbutt6.configure(font=("Arial", size))
    l1.configure(font=("Arial", size))
    l2.configure(font=("Arial", size))
    l3.configure(font=("Arial", size))
    l4.configure(font=("Arial", size))
    l5.configure(font=("Arial", size))
    l6.configure(font=("Arial", size)) 
    ent.configure(font=("Arial", size))
    subutt.configure(font=("Arial", size)) 
    scorelbl.configure(font=("Arial", size)) 
    correct.configure(font=("Arial", size)) 
    incorrect.configure(font=("Arial", size)) 
    equi_button.configure(font=("Arial", size)) 
    iso_button.configure(font=("Arial", size)) 
    sca_button.configure(font=("Arial", size)) 
    switch.configure(font=("Arial", size)) 
    incorrect.configure(font=("Arial", size)) 
    correct.configure(font=("Arial", size)) 



#defining function for text to speech
def play(text):
    tts = gTTS(text)
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)

    audio_stream.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

#defining functions for keyboard events
def clicked(event):
    remove()
    page1.grid(row=0, column=0)
    page1.configure(width=1000, height=600)
    page1.grid_propagate(False)


def contclicked(event):
    remove()
    page4.grid(row=0, column=0)
    page4.configure(width=1000, height=600)
    page4.grid_propagate(False)


def unbind_return_key():
    root.unbind("<Button-3>")
    print("Return key unbound")


#defining functions to display different frames
def show_page2():
    remove()
    page2.grid(row=0, column=0)
    page2.configure(width=1000, height=600)
    page2.grid_propagate(False)

root.bind("<Return>", clicked)

def show_page1():
    remove()
    page1.grid(row=0, column=0) 
    page1.configure(width=1000, height=600)
    page1.grid_propagate(False)


def show_page3():
    remove()
    page3.grid(row=0, column=0) 
    page3.configure(width=1000, height=600)
    page3.grid_propagate(False)

def show_page4():
    remove()
    page4.grid(row=0, column=0) 
    page4.configure(width=1000, height=600)
    page4.grid_propagate(False)
    updateq()

def show_page8():
    remove()
    page8.grid(row=0, column=0) 
    page8.configure(width=1000, height=600)
    page8.grid_propagate(False)

def remove():
    openpage.grid_forget()
    page1.grid_forget()
    page2.grid_forget()
    page3.grid_forget()
    page4.grid_forget()
    page5.grid_forget()
    page6.grid_forget()
    page7.grid_forget()
    page8.grid_forget()

#updating the question
def updateq():
    qlbl.configure(text=questions[current_q_index]["question"])
    image_path = questions[current_q_index].get("image")
    if image_path:
        image = Image.open(image_path)
        resized_image = image.resize((300, 300), Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image
    
#checking answer
def checkanswer():
    global current_q_index, score
    user_answer = ent.get().lower().strip()
    correct_answer = questions[current_q_index]["answer"]
    if user_answer == correct_answer:
        score+=1
        root.bind("<Button-3>", contclicked)
        show_page5()
    else:
        show_page6()
        incorrect.configure(text = f"your answer is incorrect!!!The answer was {correct_answer}")
        root.bind("<Button-3>", contclicked) 
    ent.delete(0, END)
    nextq()

#defining result pages
def show_page5():
    remove()
    page5.grid(row=0, column=0)  
    page5.configure(width=1000, height=600)
    page5.grid_propagate(False)

def show_page6():
    remove()
    page6.grid(row=0, column=0) 
    page6.configure(width=1000, height=600)
    page6.grid_propagate(False)


#defining function to show next question or score
def nextq():
    global current_q_index, score 
    current_q_index += 1
    if current_q_index <= total_q:
        updateq()
    else:
        show_page7()
        scorelbl.configure(text=f"You scored {score} out of {total_q}")
        
    
def show_page7():
    page7.grid(row=0, column=0) 
    lambda: page7.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page4.grid_forget()
    page5.grid_forget()
    page6.grid_forget()
    openpage.grid_forget()
        

# open page 
imagepath = "triangle2 open page.png"
firstimg = ImageTk.PhotoImage(Image.open(imagepath))
fi = Label(openpage, image=firstimg, text="")
fi.grid(row=1, column=1)


label = customtkinter.CTkLabel(openpage, text= "press enter")
label.grid(row=3, column=1)

# Configure the rows and columns
openpage.grid_rowconfigure(0, weight=1)  # Top spacer
openpage.grid_rowconfigure(1, weight=0)  # Image row
openpage.grid_rowconfigure(2, weight=0)  # Spacer between image and label
openpage.grid_rowconfigure(3, weight=0)  # Label row
openpage.grid_rowconfigure(4, weight=1)  # Bottom spacer

openpage.grid_columnconfigure(0, weight=1)  # Left spacer
openpage.grid_columnconfigure(1, weight=0)  # Image and label column
openpage.grid_columnconfigure(2, weight=1)  # Right spacer

lbl1 = customtkinter.CTkLabel(page1, text="instructions", font = ("Arial", 40)) 
lbl1.grid(row=1, column=1)

t1= customtkinter.CTkLabel(page1, text="""
         a triangle will be shown to you. 
         identify the type of triangle.
         if your answer is correct then you will earn 1 point.
         """, font = default_font)
t1.grid(row=2, column=1)

butt1 = customtkinter.CTkButton(page1, text="next",command=show_page2, font = default_font)
butt1.grid(row=4, column=2)

imagepath = "speakericon.png"
speakerimg = customtkinter.CTkImage(Image.open(imagepath))

playbutt1 = customtkinter.CTkButton(page1, text="", image=speakerimg, width=12, height=12, command=lambda: play("instructions part 1"), font = default_font)
playbutt1.grid(row=0, column=2)

playbutt2 = customtkinter.CTkButton(page1, text="", image=speakerimg, width=12, height=12, font = default_font, command=lambda: play("a triangle will be shown to you. calculate angle and identify the triangle.if your answer is correct then you will earn 1 point. if the answer is wrong no points will be deducted. answer every question before the 60 second timer runs out"))
playbutt2.grid(row=3, column=1)


# Configure the rows and columns
page1.grid_rowconfigure(0, weight=1)  # spacer
page1.grid_rowconfigure(1, weight=0)  # title
page1.grid_rowconfigure(2, weight=0)  # a triangle shown to u label 
page1.grid_rowconfigure(3, weight=0)  # next and playbutt2
page1.grid_rowconfigure(4, weight=1)  # Bottom spacer

page1.grid_columnconfigure(0, weight=1)  # 
page1.grid_columnconfigure(1, weight=0)  # Image and label column
page1.grid_columnconfigure(2, weight=1)  # Right spacer


def show_equi_instructions():
    destroy()
    # equi_button.grid(row=1, column=1)
    show_page3()
    t2.grid(row=1, column=0)
    l1.grid(row=1, column=2)
    l4.grid(row=1, column=3)
    playbutt4.grid(row=1, column=4)

def show_iso_instructions():
    destroy()
    # iso_button.grid(row=1, column=1)
    show_page3()
    t3.grid(row=1, column=0)
    l2.grid(row=1, column=2)
    l5.grid(row=1, column=3)
    playbutt5.grid(row=1, column=4)

def show_sca_instructions():
    destroy()
    # sca_button.grid(row=1, column=1)
    show_page3()
    t4.grid(row=1, column=0)
    l3.grid(row=1, column=2)
    l6.grid(row=1, column=3)
    playbutt6.grid(row=1, column=4)

def destroy():
    # equi_button.grid_forget()
    t2.grid_forget()
    l1.grid_forget()
    l4.grid_forget()
    playbutt4.grid_forget()

    # iso_button.grid_forget()
    t3.grid_forget()
    l2.grid_forget()
    l5.grid_forget()
    playbutt5.grid_forget()

    # sca_button.grid_forget()
    t4.grid_forget()
    l3.grid_forget()
    l6.grid_forget()
    playbutt6.grid_forget()



#instructions page 2 - buttons, labels and images
lbl2 = customtkinter.CTkLabel(page2, text="lessons", font = ("Arial", 40))
lbl2.grid(row=1, column=1)

sbutt3 = customtkinter.CTkButton(page2, text="start",command=show_page4, font = default_font)
sbutt3.grid(row=4, column=2)

bbutt2 = customtkinter.CTkButton(page2, text="back",command=show_page1, font = default_font)
bbutt2.grid(row=4, column=0)

# equilateral triangle
equi_button = customtkinter.CTkButton(page2, text="equilateral", command=show_equi_instructions)
equi_button.grid(row=2,column=0)

# isoscles triangle
iso_button = customtkinter.CTkButton(page2, text="isoceles", command=show_iso_instructions)
iso_button.grid(row=2,column=1)

# scalene triangle
sca_button = customtkinter.CTkButton(page2, text="scalene", command=show_sca_instructions)
sca_button.grid(row=2,column=2)

playbutt3 = customtkinter.CTkButton(page2, text="", image=speakerimg, width=12, height=12, command=lambda: play("instructions part 2"), font = default_font)
playbutt3.grid(row=0, column=2)

# Configure the rows and columns
page2.grid_rowconfigure(0, weight=1)  # spacer
page2.grid_rowconfigure(1, weight=0)  # lessons
page2.grid_rowconfigure(2, weight=1)  # buttons
page2.grid_rowconfigure(3, weight=0)  # 
page2.grid_rowconfigure(4, weight=1)  # start back

page2.grid_columnconfigure(0, weight=1)  # 
page2.grid_columnconfigure(0, weight=1)  # Left spacer
page2.grid_columnconfigure(1, weight=0)  # Image and label column
page2.grid_columnconfigure(2, weight=1)  # Right spacer


# page3 
# equilateral
imagepath = "ins2triangles1-removebg.png"
img1 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page3, image=img1, text="")

l1 = customtkinter.CTkLabel(page3, text = "equilateral triangle", font = default_font)

l4 = customtkinter.CTkLabel(page3, text = "3 equal sides", font = default_font)

playbutt4 = customtkinter.CTkButton(page3, text="", image=speakerimg, width=12, height=12, command=lambda: play("an equilateral triangle has three equal sides"), font = default_font)

# isosceles
imagepath = "ins2triangles2-removebg.png"
img2 = ImageTk.PhotoImage(Image.open(imagepath))
t3 = Label(page3, image=img2, text="")

l2 = customtkinter.CTkLabel(page3, text = "isosceles triangle", font = default_font)

l5 = customtkinter.CTkLabel(page3, text = "two equal sides", font = default_font)

playbutt5 = customtkinter.CTkButton(page3, text="", image=speakerimg, width=12, height=12, command=lambda: play("an isosceles triangle has two equal sides"), font = default_font)

# scalene
imagepath = "ins2triangles3-removebg.png"
img3 = ImageTk.PhotoImage(Image.open(imagepath))
t4 = Label(page3, image=img3, text="")

l3 = customtkinter.CTkLabel(page3, text = "scalene triangle", font = default_font)

l6 = customtkinter.CTkLabel(page3, text = "no equal sides", font = default_font)

playbutt6 = customtkinter.CTkButton(page3, text="", image=speakerimg, width=12, height=12, command=lambda: play("a scalene triangle has no equal sides"), font = default_font)


sbutt3 = customtkinter.CTkButton(page3, text="start",command=show_page4, font = default_font)
sbutt3.grid(row=4, column=3)

bbutt1 = customtkinter.CTkButton(page3, text="back",command=show_page2, font = default_font)
bbutt1.grid(row=4, column=0)

# Configure the rows and columns
page3.grid_rowconfigure(0, weight=0)  # ttle and playbutt3
page3.grid_rowconfigure(1, weight=1)  # spacer
page3.grid_rowconfigure(2, weight=0)  # 
page3.grid_rowconfigure(3, weight=0)  # iso, equi, sca buttons
page3.grid_rowconfigure(4, weight=1)  # start, back 

page3.grid_columnconfigure(0, weight=1)  # 
page3.grid_columnconfigure(0, weight=1)  # Left spacer
page3.grid_columnconfigure(1, weight=0)  # Image and label column
page3.grid_columnconfigure(2, weight=1)  # Right spacer

#page4 - quiz
questions = [ 
    {"question": "1. what type of triangle is this?", "answer": "equilateral", "image": "equi1.png"},
    {"question": "2. what type of triangle is this?", "answer": "scalene", "image": "scal1.png"},
    {"question": "3. what type of triangle is this?", "answer": "isosceles", "image": "iso1.png"},
    {"question": "4. what type of triangle is this?", "answer": "scalene", "image": "scal2.png"},
    {"question": "5. what type of triangle is this?", "answer": "equilateral", "image": "equi2.png"},
    {"question": "6. what type of triangle is this?", "answer": "scalene", "image": "scal3.png"},
    {"question": "7. what type of triangle is this?", "answer": "isosceles", "image": "iso2.png"},
    {"question": "8. what type of triangle is this?", "answer": "isosceles", "image": "iso3.png"},
    {"question": "9. what type of triangle is this?", "answer": "equilateral", "image": "equi3.png"}, 
        ]

current_q_index = 0
total_q = len(questions)
score = 0

#question label
qlbl = customtkinter.CTkLabel(page4, text="", font = ("Arial", 40))
qlbl.grid(row=1, column=0)

#entry widget
ent = customtkinter.CTkEntry(page4, font = default_font)
ent.grid(row=2, column=0)

#submit button
subutt = customtkinter.CTkButton(page4, text="submit", command=checkanswer, font = default_font)
subutt.grid(row=3, column=0)

image_label = Label(page4)
image_label.grid(row=2, column=2)

# Configure the rows and columns
page4.grid_rowconfigure(0, weight=1)  # spacer
page4.grid_rowconfigure(1, weight=0)  # qlbl
page4.grid_rowconfigure(2, weight=0)  # entry
page4.grid_rowconfigure(3, weight=0)  # subutt
page4.grid_rowconfigure(4, weight=1)  # spacer

page4.grid_columnconfigure(0, weight=1)  # 
page4.grid_columnconfigure(0, weight=1)  # Left spacer
page4.grid_columnconfigure(1, weight=0)  # Image and label column
page4.grid_columnconfigure(2, weight=1)  # Right spacer


#page5 - correct answer
correct = customtkinter.CTkLabel(page5, text = "your answer is correct!!!", font = default_font)
correct.grid(row=1, column=1)
cont1 = customtkinter.CTkLabel(page5, text = "right click to continue", font = default_font)
cont1.grid(row=2, column=1)


# Configure the rows and columns
page5.grid_rowconfigure(0, weight=1)  # spacer
page5.grid_rowconfigure(1, weight=0)  # qlbl
page5.grid_rowconfigure(2, weight=0)  # entry
page5.grid_rowconfigure(3, weight=0)  # subutt
page5.grid_rowconfigure(4, weight=1)  # spacer

page5.grid_columnconfigure(0, weight=1)  # 
page5.grid_columnconfigure(0, weight=1)  # Left spacer
page5.grid_columnconfigure(1, weight=0)  # Image and label column
page5.grid_columnconfigure(2, weight=1) 

#page6 - incorrect answer
incorrect = customtkinter.CTkLabel(page6, text = "", font = default_font)
incorrect.grid(row=1, column=1)
cont2 = customtkinter.CTkLabel(page6, text = "right click to continue", font = default_font)
cont2.grid(row=2, column=1)

# Configure the rows and columns
page6.grid_rowconfigure(0, weight=1)  # spacer
page6.grid_rowconfigure(1, weight=0)  # qlbl
page6.grid_rowconfigure(2, weight=0)  # entry
page6.grid_rowconfigure(3, weight=0)  # subutt
page6.grid_rowconfigure(4, weight=1)  # spacer

page6.grid_columnconfigure(0, weight=1)  # 
page6.grid_columnconfigure(0, weight=1)  # Left spacer
page6.grid_columnconfigure(1, weight=0)  # Image and label column
page6.grid_columnconfigure(2, weight=1) 

#page7 - score
scorelbl = customtkinter.CTkLabel(page7, text="", font = default_font)
scorelbl.grid(row=2, column=1)

page7.grid_rowconfigure(0, weight=1)  # spacer
page7.grid_rowconfigure(1, weight=0)  # qlbl
page7.grid_rowconfigure(2, weight=0)  # entry
page7.grid_rowconfigure(3, weight=0)  # subutt
page7.grid_rowconfigure(4, weight=1)  # spacer

page7.grid_columnconfigure(0, weight=1)  # 
page7.grid_columnconfigure(0, weight=1)  # Left spacer
page7.grid_columnconfigure(1, weight=0)  # Image and label column
page7.grid_columnconfigure(2, weight=1) 

imagepath = "settingsicon.png"
settingsimg = customtkinter.CTkImage(Image.open(imagepath))

settingsbutton = customtkinter.CTkButton(page1, image=settingsimg, text="", width=100, height=100)
settingsbutton.grid(row=3, column=4)



# mymenu = Menu(root)
# root.configure(menu=mymenu)

# def mycommand():
#     pass

# filemenu = Menu(mymenu)
# mymenu.add_cascade(label="settings", menu=filemenu)
# # filemenu.add_command(label="font size", command=mycommand)
# # filemenu.add_command(label="speech", command=mycommand)
# # filemenu.add_command(label="mode", command=mycommand)
# filemenu.add_separator()
# filemenu.add_command(label="exit", command=root.quit)

# filemenu = Menu(mymenu)
# mymenu.add_cascade(label="settings", menu=filemenu)
# filemenu.add_command(label="font size", command=mycommand)

# filemenu.add_separator()
# filemenu.add_command(label="exit", command=root.quit)

#font size
font_sizes = [28, 30, 32, 34]
selected_size = StringVar()
fontsize_combo1 = ttk.Combobox(page1, textvariable=selected_size, values=font_sizes, width=2, font = default_font)
fontsize_combo2 = ttk.Combobox(page2, textvariable=selected_size, values=font_sizes, width=2, font = default_font)

fontsize_combo1.current(1)  
fontsize_combo2.current(1)  

fontsize_combo1.bind("<<ComboboxSelected>>", change_font_size)
fontsize_combo2.bind("<<ComboboxSelected>>", change_font_size)

fontsize_combo1.grid(row=0, column=4)
fontsize_combo2.grid(row=0, column=4)

page1.grid_propagate(False)
page2.grid_propagate(False)
page3.grid_propagate(False)
page4.grid_propagate(False)
page5.grid_propagate(False)
page6.grid_propagate(False)
page7.grid_propagate(False)
page8.grid_propagate(False)

root.mainloop()
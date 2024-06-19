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
root.geometry("1000x800")


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


def changemode():
    val=switch.get()
    if val:
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")


switch = customtkinter.CTkSwitch(root, text="dark mode", 
                   onvalue=1,
                   offvalue=0,
                   command=changemode)

switch.grid(row=0, column=6)
print(switch.get())

# root.mainloop()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

width = root.winfo_screenwidth()
height = root.winfo_screenheight() 

#creating all frames
openpage = customtkinter.CTkFrame(root)
page1 =  customtkinter.CTkFrame(root)
page2 =  customtkinter.CTkFrame(root)
page4 =  customtkinter.CTkFrame(root)
page5 =  customtkinter.CTkFrame(root)
page6 =  customtkinter.CTkFrame(root)
page7 =  customtkinter.CTkFrame(root)
page8 =  customtkinter.CTkFrame(root)

#using grid to place the frames onto the gui
openpage.grid(row=0, column=0)
page1.grid(row=0, column=0)
page2.grid(row=0, column=0)
page4.grid(row=0, column=0)
page5.grid(row=0, column=0)
page6.grid(row=0, column=0)
page7.grid(row=0, column=0)
page8.grid(row=0, column=0)

#using grid_forget() so that only openpage will be displayed
page1.grid_forget()
page2.grid_forget()
page4.grid_forget()
page5.grid_forget()
page6.grid_forget()
page7.grid_forget()
page8.grid_forget()

#setting initial font size and colour
default_font = ("Arial", 28)
# default_fontcolor = "black"

#defining function to change font size
def change_font_size(event):
    size = int(selected_size.get())
    lbl.configure(font=("Arial", size))
    lbl1.configure(font=("Arial", size))
    lbl2.configure(font=("Arial", size))
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
    qlbl.configure(font=("Arial", size))
    reslbl.configure(font=("Arial", size)) 
    ent.configure(font=("Arial", size))
    subutt.configure(font=("Arial", size)) 
    scorelbl.configure(font=("Arial", size)) 
    correct.configure(font=("Arial", size)) 
    incorrect.configure(font=("Arial", size)) 



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
    page1.grid(row=0, column=0)
    lambda: page1.tkraise()
    page2.grid_forget()
    page4.grid_forget()
    page6.grid_forget()
    page5.grid_forget()
    page7.grid_forget()
    page8.grid_forget()
    openpage.grid_forget()

def contclicked(event):
    page4.grid(row=0, column=0)
    lambda: page4.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page6.grid_forget()
    page5.grid_forget()
    page7.grid_forget()
    page8.grid_forget()
    openpage.grid_forget()

#defining functions to display different frames
def show_page2():
    page2.grid(row=0, column=0)
    lambda: page2.tkraise()
    page1.grid_forget()
    page4.grid_forget()
    page6.grid_forget()
    page5.grid_forget()
    page7.grid_forget()
    page8.grid_forget()
    openpage.grid_forget()


def show_page1():
    page1.grid(row=0, column=0) 
    lambda: page1.tkraise()
    page2.grid_forget()
    page4.grid_forget()
    page6.grid_forget()
    page5.grid_forget()
    page7.grid_forget()
    page8.grid_forget()
    openpage.grid_forget()

def show_page4():
    page4.grid(row=0, column=0) 
    lambda: page4.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page6.grid_forget()
    page5.grid_forget()
    page7.grid_forget()
    page8.grid_forget()
    openpage.grid_forget()
    updateq()

def show_page8():
    page8.grid(row=0, column=0) 
    lambda: page8.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page4.grid_forget()
    page6.grid_forget()
    page5.grid_forget()
    page7.grid_forget()
    page8.grid_forget()
    openpage.grid_forget()

#updating the question
def updateq():
    qlbl.configure(text=questions[current_q_index]["question"])
    image_path = questions[current_q_index].get("image")
    if image_path:
        image = Image.open(image_path)
        resized_image = image.resize((200, 200), Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image
    
#checking answer
def checkanswer():
    global current_q_index, score
    user_answer = ent.get()
    correct_answer = questions[current_q_index]["answer"]
    if user_answer == correct_answer:
        score+=1
        show_page5()
    else:
        show_page6()
        incorrect.configure(text = f"your answer is incorrect!!!The answer was {correct_answer}")

        
    ent.delete(0, END)
    nextq()

#defining result pages
def show_page5():
    page5.grid(row=0, column=0) 
    lambda: page5.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page4.grid_forget()
    page6.grid_forget()
    openpage.grid_forget()

def show_page6():
    page6.grid(row=0, column=0) 
    lambda: page6.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page4.grid_forget()
    page5.grid_forget()
    openpage.grid_forget()

#defining function to show next question or score
def nextq():
    global current_q_index, score 
    current_q_index += 1
    if current_q_index < total_q:
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
        

root.bind("<Return>", clicked)

# open page 
imagepath = "triangle2 open page.png"
firstimg = ImageTk.PhotoImage(Image.open(imagepath))
fi = Label(openpage, image=firstimg, text="")
fi.grid(row=1, column=1) 

label = customtkinter.CTkLabel(openpage, text= "press enter")
label.grid(row=2, column=1)

openpage.tkraise() 

# instructions page 1 - buttons and labels
lbl = customtkinter.CTkLabel(page1, text="            ")
lbl.grid(row=2, column=0)

lbl1 = customtkinter.CTkLabel(page1, text="instructions:part 1", font = default_font) 
lbl1.grid(row=0, column=1)

t1= customtkinter.CTkLabel(page1, text="""
         a triangle will be shown to you. 
         identify the type of triangle.
         if your answer is correct then you will earn 1 point.
         """, font = default_font)
t1.grid(row=1, column=1)

butt1 = customtkinter.CTkButton(page1, text="next",command=show_page2, font = default_font)
butt1.grid(row=2, column=2)

playbutt1 = customtkinter.CTkButton(page1, text="Instructions", command=lambda: play("instructions part 1"), font = default_font)
playbutt1.grid(row=0, column=2)

playbutt2 = customtkinter.CTkButton(page1, text="Instructions", font = default_font, command=lambda: play("a triangle will be shown to you. calculate angle and identify the triangle.if your answer is correct then you will earn 1 point. if the answer is wrong no points will be deducted. answer every question before the 60 second timer runs out"))
playbutt2.grid(row=2, column=1)


#instructions page 2 - buttons, labels and images
lbl2 = customtkinter.CTkLabel(page2, text="instructions:part 2", font = default_font)
lbl2.grid(row=0, column=1)

imagepath = "ins2triangles1-removebg.png"
img1 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img1, text="")
t2.grid(row=1, column=1) 

imagepath = "ins2triangles2-removebg.png"
img2 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img2, text="")
t2.grid(row=2, column=1) 

imagepath = "ins2triangles3-removebg.png"
img3 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img3, text="")
t2.grid(row=3, column=1) 


sbutt3 = customtkinter.CTkButton(page2, text="start",command=show_page4, font = default_font)
sbutt3.grid(row=4, column=2)

bbutt1 = customtkinter.CTkButton(page2, text="back",command=show_page1, font = default_font)
bbutt1.grid(row=4, column=0)

l1 = customtkinter.CTkLabel(page2, text = "equilateral triangle", font = default_font)
l1.grid(row=1, column=2)

l2 = customtkinter.CTkLabel(page2, text = "isosceles triangle", font = default_font)
l2.grid(row=2, column=2)

l3 = customtkinter.CTkLabel(page2, text = "scalene triangle", font = default_font)
l3.grid(row=3, column=2)

l4 = customtkinter.CTkLabel(page2, text = "3 equal sides", font = default_font)
l4.grid(row=1, column=3)

l5 = customtkinter.CTkLabel(page2, text = "two equal sides", font = default_font)
l5.grid(row=2, column=3)

l6 = customtkinter.CTkLabel(page2, text = "no equal sides", font = default_font)
l6.grid(row=3, column=3)

playbutt3 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("instructions part 2"), font = default_font)
playbutt3.grid(row=0, column=2)

playbutt4 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("an equilateral triangle has three equal sides"), font = default_font)
playbutt4.grid(row=1, column=4)

playbutt5 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("an isosceles triangle has two equal sides"), font = default_font)
playbutt5.grid(row=2, column=4)

playbutt6 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("a scalene triangle has no equal sides"), font = default_font)
playbutt6.grid(row=3, column=4)


#page4 - quiz
questions = [ 
    {"question": "what type of triangle is this?", "answer": "equilateral", "image": "equi1.png"},
    {"question": "what type of triangle is this?", "answer": "scalene", "image": "scal1.png"},
    {"question": "what type of triangle is this?", "answer": "isosceles", "image": "iso1.png"},
    {"question": "what type of triangle is this?", "answer": "scalene", "image": "scal2.png"},
    {"question": "what type of triangle is this?", "answer": "equilateral", "image": "equi2.png"},
    {"question": "what type of triangle is this?", "answer": "scalene", "image": "scal3.png"},
    {"question": "what type of triangle is this?", "answer": "isosceles", "image": "iso2.png"},
    {"question": "what type of triangle is this?", "answer": "isosceles", "image": "iso3.png"},
    {"question": "what type of triangle is this?", "answer": "equilateral", "image": "equi3.png"}, 
        ]

current_q_index = 0
total_q = len(questions)
score = 0

#question label
qlbl = customtkinter.CTkLabel(page4, text="what type of triangle is this?", font = default_font)
qlbl.grid(row=0, column=0)

#result label
reslbl = customtkinter.CTkLabel(page4, text="", font = default_font)
reslbl.grid(row=3, column=0)

#entry widget
ent = customtkinter.CTkEntry(page4, font = default_font)
ent.grid(row=1, column=0)

#submit button
subutt = customtkinter.CTkButton(page4, text="submit", command=checkanswer, font = default_font)
subutt.grid(row=2, column=0)

image_label = Label(page4)
image_label.grid(row=2, column=3)

#page5 - correct answer
correct = customtkinter.CTkLabel(page5, text = "your answer is correct!!!", font = default_font)
correct.grid(row=1, column=1)
cont1 = customtkinter.CTkLabel(page5, text = "right click to continue", font = default_font)
cont1.grid(row=2, column=1)

root.bind("<Button-3>", contclicked)

#page6 - incorrect answer
incorrect = customtkinter.CTkLabel(page6, text = "", font = default_font)
incorrect.grid(row=1, column=1)
cont2 = customtkinter.CTkLabel(page6, text = "right click to continue", font = default_font)
cont2.grid(row=2, column=1)

#page7 - score
scorelbl = customtkinter.CTkLabel(page7, text="", font = default_font)
scorelbl.grid(row=2, column=1)


#font size
font_sizes = [24, 26, 28, 32, 34]
selected_size = StringVar()
fontsize_combo1 = ttk.Combobox(page1, textvariable=selected_size, values=font_sizes, width=2, font = default_font)
fontsize_combo2 = ttk.Combobox(page2, textvariable=selected_size, values=font_sizes, width=2, font = default_font)

fontsize_combo1.current(2)  
fontsize_combo2.current(2)  

fontsize_combo1.bind("<<ComboboxSelected>>", change_font_size)
fontsize_combo2.bind("<<ComboboxSelected>>", change_font_size)

fontsize_combo1.grid(row=0, column=3)
fontsize_combo2.grid(row=0, column=3)


root.mainloop()
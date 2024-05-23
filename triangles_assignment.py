from tkinter import *
from tkinter import ttk
import tkinter as tk 
from gtts import gTTS
from io import BytesIO
import pygame
from PIL import ImageTk, Image 
import googletrans 
import textblob 
import customtkinter 
# from tkinter import messagebox
root = Tk()
root.title('triangles')

# c= Canvas(root, bg="", height=200, width=200)
# c.place(y=100, x=0)

selected_size = StringVar(value = "24")


page1 = customtkinter.CTkFrame(root)
page2 = customtkinter.CTkFrame(root)
page3 = customtkinter.CTkFrame(root)
page4 = customtkinter.CTkFrame(root)

page1.grid(row=0, column=0)
page2.grid(row=0, column=0)
page3.grid(row=0, column=0)
page4.grid(row=0, column=0)

page2.grid_forget()
page3.grid_forget()



def change_font_size(event):
    size = int(selected_size.get())
    lbl.configure(font=("Arial", size))
    lbl1.configure(font=("Arial", size))
    lbl2.configure(font=("Arial", size))
    lbl3.configure(font=("Arial", size))
    t1.configure(font=("Arial", size))
    t2.configure(font=("Arial", size))
    t3.configure(font=("Arial", size))
    t4.configure(font=("Arial", size))
    butt1.configure(font=("Arial", size))
    butt2.configure(font=("Arial", size))
    sbutt3.configure(font=("Arial", size))
    bbutt1.configure(font=("Arial", size))
    bbutt2.configure(font=("Arial", size))
    fontsize_combo1.configure(font=("Arial", size))
    fontsize_combo2.configure(font=("Arial", size))
    fontsize_combo3.configure(font=("Arial", size))
    fontsize_combo4.configure(font=("Arial", size))
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



def trans(event):
    selected_lang = event.widget.get() 
    lbl1.configure(lang = selected_lang)
    # lbl1.configure(lang=())
    # lbl2.configure(lang=())
    # lbl3.configure(lang=())
 
lang = googletrans.LANGUAGES
langlist = list(lang.values())


def play(text):
    tts = gTTS(text)
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)

    audio_stream.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

def show_page2():
    page2.grid(row=0, column=0)
    lambda: page2.tkraise()
    page1.grid_forget()
    page3.grid_forget()
    page4.grid_forget()


def show_page1():
    page1.grid(row=0, column=0)
    lambda: page1.tkraise()
    page2.grid_forget()
    page3.grid_forget()
    page4.grid_forget()


def show_page3():
    page3.grid(row=0, column=0)
    lambda: page3.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page4.grid_forget()


def show_page4():
    page4.grid(row=0, column=0)
    lambda: page4.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page3.grid_forget()
    updateq()


def updateq():
    qlbl.configure(text=questions[current_q_index]["question"])
    image_path = questions[current_q_index].get("image")
    if image_path:
        image = Image.open(image_path)
        resized_image = image.resize((200, 200), Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

def checkanswer():
    global current_q_index, score 
    user_answer = ent.get()
    correct_answer = questions[current_q_index]["answer"]
    if user_answer == correct_answer:
        reslbl.configure(text="correct")
        score+=1
    else:
        reslbl.configure(text=f"incorrect! The correct answer was {correct_answer}")
        # image_label.configure(image="")
        
  
    ent.delete(0, END)
    nextq()


def nextq():
    global current_q_index
    current_q_index += 1
    if current_q_index < total_q:
        updateq()
    else:
        qlbl.configure(text=f"You scores {score} out of {total_q}")
    


# instructions page 1 
lbl = customtkinter.CTkLabel(page1, text="            ")
lbl.grid(row=2, column=0)

lbl1 = customtkinter.CTkLabel(page1, text="instructions:part 1")
lbl1.grid(row=0, column=1)

t1= customtkinter.CTkLabel(page1, text="""
         a triangle will be shown to you. 
         calculate angle and identify the triangle.
         if your answer is correct then you will earn 1 point. 
         if the answer is wrong no points will be deducted. 
         answer every question before the 60 second timer runs out
         """)
t1.grid(row=1, column=1)

butt1 = customtkinter.CTkButton(page1, text="next",command=show_page2)
butt1.grid(row=2, column=2)

playbutt1 = customtkinter.CTkButton(page1, text="Instructions", command=lambda: play("instructions part 1"))
playbutt1.grid(row=0, column=2)

playbutt2 = customtkinter.CTkButton(page1, text="Instructions", command=lambda: play("a triangle will be shown to you. calculate angle and identify the triangle.if your answer is correct then you will earn 1 point. if the answer is wrong no points will be deducted. answer every question before the 60 second timer runs out"))
playbutt2.grid(row=2, column=1)

#instructions page 2
lbl2 = customtkinter.CTkLabel(page2, text="instructions:part 2")
lbl2.grid(row=0, column=1)

imagepath = "C:/Users/praja/OneDrive/Desktop/ins2triangles1-removebg.png"
img1 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img1, text="")
t2.grid(row=1, column=1) 

imagepath = "C:/Users/praja/OneDrive/Desktop/ins2triangles2-removebg.png"
img2 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img2, text="")
t2.grid(row=2, column=1) 

imagepath = "C:/Users/praja/OneDrive/Desktop/ins2triangles3-removebg.png"
img3 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img3, text="")
t2.grid(row=3, column=1) 

butt2 = customtkinter.CTkButton(page2, text="next",command=show_page3)
butt2.grid(row=4, column=2)

bbutt1 = customtkinter.CTkButton(page2, text="back",command=show_page1)
bbutt1.grid(row=4, column=0)

l1 = customtkinter.CTkLabel(page2, text = "equilateral triangle")
l1.grid(row=1, column=2)

l2 = customtkinter.CTkLabel(page2, text = "isosceles triangle")
l2.grid(row=2, column=2)

l3 = customtkinter.CTkLabel(page2, text = "scalene triangle")
l3.grid(row=3, column=2)

l4 = customtkinter.CTkLabel(page2, text = "3 equal sides")
l4.grid(row=1, column=3)

l5 = customtkinter.CTkLabel(page2, text = "two equal sides")
l5.grid(row=2, column=3)

l6 = customtkinter.CTkLabel(page2, text = "no equal sides")
l6.grid(row=3, column=3)

playbutt3 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("instructions part 2"))
playbutt3.grid(row=0, column=4)

playbutt4 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("an equilateral triangle has three equal sides"))
playbutt4.grid(row=1, column=4)

playbutt5 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("an isosceles triangle has two equal sides"))
playbutt5.grid(row=2, column=4)

playbutt6 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("a scalene triangle has no equal sides"))
playbutt6.grid(row=3, column=4)

# instructions page 3
lbl3 = customtkinter.CTkLabel(page3, text="instructions:part 3")
lbl3.grid(row=0, column=1)


imagepath = "C:/Users/praja/OneDrive/Desktop/ins3_tri-removebg.png"
img4 = ImageTk.PhotoImage(Image.open(imagepath))
t3 = Label(page3, image=img4, text="")
t3.grid(row=1, column=1) 

t4 = customtkinter.CTkLabel(page3, text="""
           angle sum of a triangle is 180 
                 90+45+45=180
           """)
t4.grid(row=1, column=2)

sbutt3 = customtkinter.CTkButton(page3, text="start",command=show_page4)
sbutt3.grid(row=4, column=2)

bbutt2 = customtkinter.CTkButton(page3, text="back",command=show_page2)
bbutt2.grid(row=4, column=0)

page1.tkraise()



questions = [ 
    {"question": "what type of triangle is this?", "answer": "equilateral", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/equi1.png"},
    {"question": "what type of triangle is this?", "answer": "scalene", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/scal1.png"},
    {"question": "what type of triangle is this?", "answer": "isosceles", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/iso1.png"},
    {"question": "what type of triangle is this?", "answer": "scalene", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/scal2.png"},
    {"question": "what type of triangle is this?", "answer": "equilateral", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/equi2.png"},
    {"question": "what type of triangle is this?", "answer": "scalene", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/scal3.png"},
    {"question": "what type of triangle is this?", "answer": "isosceles", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/iso2.png"},
    {"question": "what type of triangle is this?", "answer": "isosceles", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/iso3.png"},
    {"question": "what type of triangle is this?", "answer": "equilateral", "image": "C:/users/praja/OneDrive/Desktop/12sdd/images/equi3.png"}, 
        ]

current_q_index = 0
total_q = len(questions)
score = 0

qlbl = customtkinter.CTkLabel(page4, text="")
qlbl.grid(row=0, column=0)

reslbl = customtkinter.CTkLabel(page4, text="")
reslbl.grid(row=3, column=0)

ent = customtkinter.CTkEntry(page4)
ent.grid(row=1, column=0)

subutt = customtkinter.CTkButton(page4, text="submit", command=checkanswer)
subutt.grid(row=2, column=0)

image_label = Label(page4)
image_label.grid(row=2, column=3)


#font size
font_sizes = [18, 20, 24, 28, 32]
selected_size = StringVar(value = "24")
fontsize_combo1 = ttk.Combobox(page1, textvariable=selected_size, values=font_sizes, width=2)
fontsize_combo2 = ttk.Combobox(page2, textvariable=selected_size, values=font_sizes, width=2)
fontsize_combo3 = ttk.Combobox(page3, textvariable=selected_size, values=font_sizes, width=2)
fontsize_combo4 = ttk.Combobox(page4, textvariable=selected_size, values=font_sizes, width=2)

# selected_size.set(font_sizes[2])
fontsize_combo1.current(2)  
fontsize_combo2.current(2)  
fontsize_combo3.current(2)  
fontsize_combo4.current(2)  


fontsize_combo1.bind("<<ComboboxSelected>>", change_font_size)
fontsize_combo2.bind("<<ComboboxSelected>>", change_font_size)
fontsize_combo3.bind("<<ComboboxSelected>>", change_font_size)
fontsize_combo4.bind("<<ComboboxSelected>>", change_font_size)

fontsize_combo1.grid(row=0, column=3)
fontsize_combo2.grid(row=0, column=3)
fontsize_combo3.grid(row=0, column=3)
fontsize_combo4.grid(row=0, column=3)




# translator
transcombo1 = ttk.Combobox(page1, width=10, value=langlist)
transcombo2 = ttk.Combobox(page2, width=10, value=langlist)
transcombo3 = ttk.Combobox(page3, width=10, value=langlist)
transcombo4 = ttk.Combobox(page4, width=10, value=langlist)

transcombo1.current(21)
transcombo2.current(21)
transcombo3.current(21)
transcombo4.current(21)

transcombo1.bind("<<ComboboxSelected>>", trans)
transcombo2.bind("<<ComboboxSelected>>", trans)
transcombo3.bind("<<ComboboxSelected>>", trans)
transcombo4.bind("<<ComboboxSelected>>", trans)


transcombo1.grid(row=0, column=4)
transcombo2.grid(row=0, column=4)
transcombo3.grid(row=0, column=4)
transcombo4.grid(row=0, column=4)
 





root.mainloop()
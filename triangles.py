from tkinter import *
from tkinter import ttk
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
root.geometry("800x800")

# c= Canvas(root, bg="", height=200, width=200)
# c.place(y=100, x=0)

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
    fontsize_combo.configure(font=("Arial", size))
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



def trans():
    lbl.configure(lang=())
    lbl1.configure(lang=())
    lbl2.configure(lang=())
    lbl3.configure(lang=())
 
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

def checkanswer():
    user_answer = ent.get()
    correct_answer = questions[current_q_index]["answer"]
    if user_answer == correct_answer:
        reslbl.configure(text="correct")
    else:
        reslbl.configure(text="incorect")
  
    ent.delete(0, END)
    nextq()


def nextq():
    global current_q_index
    current_q_index += 1
    if current_q_index < total_q:
        updateq()


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
t2 = customtkinter.CTkLabel(page2, image=img1)
t2.grid(row=1, column=1) 

imagepath = "C:/Users/praja/OneDrive/Desktop/ins2triangles2-removebg.png"
img2 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = customtkinter.CTkLabel(page2, image=img2)
t2.grid(row=2, column=1) 

imagepath = "C:/Users/praja/OneDrive/Desktop/ins2triangles3-removebg.png"
img3 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = customtkinter.CTkLabel(page2, image=img3)
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
t3 = customtkinter.CTkLabel(page3, image=img4)
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
    {"question": "what is 2 + 2", "answer": "4"},
    {"question": "what is 3 + 3", "answer": "6"}, 
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


#font size
font_sizes = [8, 10, 12, 14, 16, 18, 20, 24, 28, 32]
selected_size = StringVar()
fontsize_combo = ttk.Combobox(root, textvariable=selected_size, values=font_sizes, width=2)
fontsize_combo.current(2)  
fontsize_combo.bind("<<ComboboxSelected>>", change_font_size)
fontsize_combo.grid(row=0, column=2)

# translator
transcombo = ttk.Combobox(root, width=10, value=langlist)
transcombo.current(21)
transcombo.bind("<<ComboboxSelected>>", trans)
transcombo.grid(row=0, column=3)
 





root.mainloop()
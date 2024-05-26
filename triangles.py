from tkinter import *
from tkinter import ttk
import tkinter as tk 
from gtts import gTTS
from io import BytesIO
import pygame
from PIL import ImageTk, Image 
import customtkinter 
from deep_translator import GoogleTranslator
import time 


root = Tk()
root.title('triangles')
root.geometry("1600x800")

customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("dark-blue")  

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

width = root.winfo_screenwidth()
height = root.winfo_screenheight() 

#creating all frames
openpage = customtkinter.CTkFrame(root, width=100, height=100, fg_color = "transparent")
page1 =  customtkinter.CTkFrame(root, width=100, height=100, fg_color = "transparent")
page2 =  customtkinter.CTkFrame(root, width=100, height=100, fg_color = "transparent")
page4 =  customtkinter.CTkFrame(root, width=100, height=100, fg_color = "transparent")
page5 =  customtkinter.CTkFrame(root, width=100, height=100, fg_color = "transparent")
page6 =  customtkinter.CTkFrame(root, width=100, height=100, fg_color = "transparent")
page7 =  customtkinter.CTkFrame(root, width=100, height=100, fg_color = "transparent")
page8 =  customtkinter.CTkFrame(root, width=100, height=100, fg_color = "transparent")

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
default_fontcolor = "black"

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

#defining function to set new language
def update_language(event=None):
    global score, total_q
    selected_language_code = langlist[language_var.get()]
    translator = GoogleTranslator(source='auto', target=selected_language_code)

    translated_lbl1 = translator.translate("instructions:part 1")
    translated_lbl2 = translator.translate("instructions:part 2")
    translated_lbl3 = translator.translate("instructions:part 3") 

    translated_t1 = translator.translate("""
         a triangle will be shown to you. 
         identify the type of triangle.
         if your answer is correct then you will earn 1 point. 
        
         """)
    translated_playbutt1 = translator.translate("Instructions")
    translated_playbutt2 = translator.translate("Instructions")
    translated_playbutt3 = translator.translate("Instructions")
    translated_playbutt4 = translator.translate("Instructions")
    translated_playbutt5 = translator.translate("Instructions")
    translated_playbutt6 = translator.translate("Instructions")

    translated_butt1 = translator.translate("next")
    translated_butt2 = translator.translate("next")

    translated_bbutt1 = translator.translate("back")
    translated_bbutt2 = translator.translate("back")

    translated_l1 = translator.translate("equilateral triangle")
    translated_l2 = translator.translate("isosceles triangle")
    translated_l3 = translator.translate("scalene triangle")
    translated_l4 = translator.translate("three equal sides")
    translated_l5 = translator.translate("two equal sides")
    translated_l6 = translator.translate("no equal sides")

    translated_qlbl = translator.translate("what type of triangle is this?")

    translated_subutt = translator.translate("submit")
    translated_sbutt = translator.translate("start") 

    translated_scorelbl = translator.translate(f"You scored {score} out of {total_q}")
    translated_correct = translator.translate("your answer is correct!!!")
    translated_incorrect = translator.translate("your answer is incorrect")

    lbl1.configure(text=translated_lbl1)
    lbl2.configure(text=translated_lbl2)

    t1.configure(text=translated_t1)

    playbutt1.configure(text=translated_playbutt1)
    playbutt2.configure(text=translated_playbutt2)
    playbutt3.configure(text=translated_playbutt2)
    playbutt4.configure(text=translated_playbutt4)
    playbutt5.configure(text=translated_playbutt5)
    playbutt6.configure(text=translated_playbutt6)

    butt1.configure(text=translated_butt1)

    bbutt1.configure(text= translated_bbutt1)

    sbutt3.configure(text=translated_sbutt)
    subutt.configure(text=translated_subutt)

    qlbl.configure(text=translated_qlbl)

    l1.configure(text=translated_l1)
    l2.configure(text=translated_l2)
    l3.configure(text=translated_l3)
    l4.configure(text=translated_l4)
    l5.configure(text=translated_l5)
    l6.configure(text=translated_l6)

    scorelbl.configure() 
    correct.configure() 
    incorrect.configure() 


langlist = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese': 'zh-CN',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru'
}

current_mode = "light"
#defining function to change theme
def change_theme():
    global current_mode
    if current_mode == "light" :
        customtkinter.set_appearance_mode("dark")
        current_mode = "dark"
        page1.configure(fg_color="black")
        page2.configure(fg_color="black")
        page8.configure(fg_color="black")

        lbl1.configure(text_color="white")
        lbl2.configure(text_color="white")
        t1.configure(text_color="white")
        t2.configure(text_color="white")
        butt1.configure(text_color="white")
        sbutt3.configure(text_color="white")
        bbutt1.configure(text_color="white")
        fontsize_combo1.configure(text_color="white")
        fontsize_combo2.configure(text_color="white")
        playbutt1.configure(text_color="white")
        playbutt2.configure(text_color="white")
        playbutt3.configure(text_color="white")
        playbutt4.configure(text_color="white")
        playbutt5.configure(text_color="white")
        playbutt6.configure(text_color="white")
        l1.configure(text_color="white")
        l2.configure(text_color="white")
        l3.configure(text_color="white")
        l4.configure(text_color="white")
        l5.configure(text_color="white")
        l6.configure(text_color="white")
        qlbl.configure(text_color="white")
        reslbl.configure(text_color="white") 
        ent.configure(text_color="white")
        subutt.configure(text_color="white") 
        

    else:
        customtkinter.set_appearance_mode("light")
        current_mode = "light" 
        page1.configure(fg_color="white")
        page2.configure(fg_color="white")
        page8.configure(fg_color="white")

        lbl1.configure(text_color="black")
        lbl2.configure(text_color="black")
        t1.configure(text_color="black")
        t2.configure(text_color="black")
        butt1.configure(text_color="black")
        sbutt3.configure(text_color="black")
        bbutt1.configure(text_color="black")
        fontsize_combo1.configure(text_color="black")
        fontsize_combo2.configure(text_color="black")
        playbutt1.configure(text_color="black")
        playbutt2.configure(text_color="black")
        playbutt3.configure(text_color="black")
        playbutt4.configure(text_color="black")
        playbutt5.configure(text_color="black")
        playbutt6.configure(text_color="black")
        l1.configure(text_color="black")
        l2.configure(text_color="black")
        l3.configure(text_color="black")
        l4.configure(text_color="black")
        l5.configure(text_color="black")
        l6.configure(text_color="black")
        qlbl.configure(text_color="black")
        reslbl.configure(text_color="black") 
        ent.configure(text_color="black")
        subutt.configure(text_color="black") 
        



root.bind("<Return>", clicked)

# open page 
imagepath = "triangle2 open page.png"
firstimg = ImageTk.PhotoImage(Image.open(imagepath))
fi = Label(openpage, image=firstimg, text="")
fi.grid(row=1, column=1) 

label = customtkinter.CTkLabel(openpage, text= "press enter", text_color=default_fontcolor)
label.grid(row=2, column=1)

openpage.tkraise() 

# instructions page 1 - buttons and labels
lbl = customtkinter.CTkLabel(page1, text="            ")
lbl.grid(row=2, column=0)

lbl1 = customtkinter.CTkLabel(page1, text="instructions:part 1", font = default_font, text_color=default_fontcolor) 
lbl1.grid(row=0, column=1)

t1= customtkinter.CTkLabel(page1, text="""
         a triangle will be shown to you. 
         identify the type of triangle.
         if your answer is correct then you will earn 1 point.
         """, font = default_font, text_color=default_fontcolor)
t1.grid(row=1, column=1)

butt1 = customtkinter.CTkButton(page1, text="next",command=show_page2, font = default_font, text_color=default_fontcolor)
butt1.grid(row=2, column=2)

playbutt1 = customtkinter.CTkButton(page1, text="Instructions", command=lambda: play("instructions part 1"), font = default_font, text_color=default_fontcolor)
playbutt1.grid(row=0, column=2)

playbutt2 = customtkinter.CTkButton(page1, text="Instructions", text_color=default_fontcolor, font = default_font, command=lambda: play("a triangle will be shown to you. calculate angle and identify the triangle.if your answer is correct then you will earn 1 point. if the answer is wrong no points will be deducted. answer every question before the 60 second timer runs out"))
playbutt2.grid(row=2, column=1)


#instructions page 2 - buttons, labels and images
lbl2 = customtkinter.CTkLabel(page2, text="instructions:part 2", font = default_font, text_color=default_fontcolor)
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


sbutt3 = customtkinter.CTkButton(page2, text="start",command=show_page4, font = default_font, text_color=default_fontcolor)
sbutt3.grid(row=4, column=2)

bbutt1 = customtkinter.CTkButton(page2, text="back",command=show_page1, font = default_font, text_color=default_fontcolor)
bbutt1.grid(row=4, column=0)

l1 = customtkinter.CTkLabel(page2, text = "equilateral triangle", font = default_font, text_color=default_fontcolor)
l1.grid(row=1, column=2)

l2 = customtkinter.CTkLabel(page2, text = "isosceles triangle", font = default_font, text_color=default_fontcolor)
l2.grid(row=2, column=2)

l3 = customtkinter.CTkLabel(page2, text = "scalene triangle", font = default_font, text_color=default_fontcolor)
l3.grid(row=3, column=2)

l4 = customtkinter.CTkLabel(page2, text = "3 equal sides", font = default_font, text_color=default_fontcolor)
l4.grid(row=1, column=3)

l5 = customtkinter.CTkLabel(page2, text = "two equal sides", font = default_font, text_color=default_fontcolor)
l5.grid(row=2, column=3)

l6 = customtkinter.CTkLabel(page2, text = "no equal sides", font = default_font, text_color=default_fontcolor)
l6.grid(row=3, column=3)

playbutt3 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("instructions part 2"), font = default_font, text_color=default_fontcolor)
playbutt3.grid(row=0, column=2)

playbutt4 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("an equilateral triangle has three equal sides"), font = default_font, text_color=default_fontcolor)
playbutt4.grid(row=1, column=4)

playbutt5 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("an isosceles triangle has two equal sides"), font = default_font, text_color=default_fontcolor)
playbutt5.grid(row=2, column=4)

playbutt6 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("a scalene triangle has no equal sides"), font = default_font, text_color=default_fontcolor)
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
qlbl = customtkinter.CTkLabel(page4, text="what type of triangle is this?", font = default_font, text_color=default_fontcolor)
qlbl.grid(row=0, column=0)

#result label
reslbl = customtkinter.CTkLabel(page4, text="", font = default_font, text_color=default_fontcolor)
reslbl.grid(row=3, column=0)

#entry widget
ent = customtkinter.CTkEntry(page4, font = default_font)
ent.grid(row=1, column=0)

#submit button
subutt = customtkinter.CTkButton(page4, text="submit", command=checkanswer, font = default_font, text_color=default_fontcolor)
subutt.grid(row=2, column=0)

image_label = Label(page4)
image_label.grid(row=2, column=3)

#page5 - correct answer
correct = customtkinter.CTkLabel(page5, text = "your answer is correct!!!", font = default_font, text_color=default_fontcolor)
correct.grid(row=1, column=1)
cont1 = customtkinter.CTkLabel(page5, text = "right click to continue", font = default_font, text_color=default_fontcolor)
cont1.grid(row=2, column=1)

root.bind("<Button-3>", contclicked)

#page6 - incorrect answer
incorrect = customtkinter.CTkLabel(page6, text = "", font = default_font, text_color=default_fontcolor)
incorrect.grid(row=1, column=1)
cont2 = customtkinter.CTkLabel(page6, text = "right click to continue", font = default_font, text_color=default_fontcolor)
cont2.grid(row=2, column=1)

#page7 - score
scorelbl = customtkinter.CTkLabel(page7, text="", font = default_font, text_color=default_fontcolor)
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

#language 
language_var = tk.StringVar()

language_dropdown1 = ttk.Combobox(page1, textvariable=language_var, width=6, font = default_font)
language_dropdown2 = ttk.Combobox(page2, textvariable=language_var, width=6, font = default_font)

language_dropdown1['values'] = list(langlist.keys())
language_dropdown2['values'] = list(langlist.keys())

language_dropdown1.grid(row=0, column=4, columnspan=2, padx=10, pady=10)
language_dropdown2.grid(row=0, column=4, columnspan=2, padx=10, pady=10)

language_dropdown1.bind('<<ComboboxSelected>>', update_language)
language_dropdown2.bind('<<ComboboxSelected>>', update_language)

language_var.set('English')

#appearance
theme = customtkinter.CTkButton(page1, text="theme", font = default_font, command=change_theme)
theme.grid(row=0, column=6)
theme = customtkinter.CTkButton(page2, text="theme", font = default_font, command=change_theme)
theme.grid(row=0, column=7)




root.mainloop()
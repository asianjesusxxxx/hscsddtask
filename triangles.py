from tkinter import *
from tkinter import ttk
import tkinter as tk 
from gtts import gTTS
from io import BytesIO
import pygame
from PIL import ImageTk, Image 
# import googletrans 
# import textblob 
import customtkinter 
# from tkinter import font as tkFont
# import customtkinter as ctk
from deep_translator import GoogleTranslator
import time 
# from tkinter import messagebox

root = Tk()
root.title('triangles')
root.geometry("1600x800")

customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

width = root.winfo_screenwidth()
height = root.winfo_screenheight() 

# root.geometry('%dx%d+0+0' % (width,height))

# c= Canvas(root, bg="red", height=200, width=200)
# c.grid(row=200, column=200)

openpage = Frame(root, width=100, height=100)
page1 =  Frame(root, width=100, height=100)
page2 =  Frame(root, width=100, height=100)
page3 =  Frame(root, width=100, height=100)
page4 =  Frame(root, width=100, height=100)

openpage.grid(row=0, column=0)
page1.grid(row=0, column=0)
page2.grid(row=0, column=0)
page3.grid(row=0, column=0)
page4.grid(row=0, column=0)

page1.grid_forget()
page2.grid_forget()
page3.grid_forget()
page4.grid_forget()

default_font = ("Arial", 28)

# # timer 
# counting = False

# def conut_down(sec):
#     counting = True
#     while sec:
#         mins, secs = divmod(sec, 60)
#         time_format = "{:2d}:{:2d}".format(mins, secs)
#         print(time_format)
#         time.sleep(1)
#         sec = sec - 1
#     print("stop")

# conut_down(5)



# second_var = tk.StringVar(value=' 00 ')
# second_lbl = tk.Label(page4, font=('Arial', 50), textvariable=second_var)
# second_lbl.grid(row=0, column=0)


def change_font_size(event):
    size = int(selected_size.get())
    lbl.configure(font=("Arial", size))
    lbl1.configure(font=("Arial", size))
    lbl2.configure(font=("Arial", size))
    lbl3.configure(font=("Arial", size))
    t1.configure(font=("Arial", size))
    t2.configure(font=("Arial", size))
    # t3.configure(font=("Arial", size))
    # t4.configure(font=("Arial", size))
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




def play(text):
    tts = gTTS(text)
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)

    audio_stream.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

def clicked(event):
    print("you pressed enter")
    page1.grid(row=0, column=0)
    lambda: page1.tkraise()
    page2.grid_forget()
    page3.grid_forget()
    page4.grid_forget()
    openpage.grid_forget()

def show_page2():
    page2.grid(row=0, column=0)
    lambda: page2.tkraise()
    page1.grid_forget()
    page3.grid_forget()
    page4.grid_forget()
    openpage.grid_forget()



def show_page1():
    page1.grid(row=0, column=0) 
    lambda: page1.tkraise()
    page2.grid_forget()
    page3.grid_forget()
    page4.grid_forget()
    openpage.grid_forget()


def show_page3():
    page3.grid(row=0, column=0) 
    lambda: page3.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page4.grid_forget()
    openpage.grid_forget()


def show_page4():
    page4.grid(row=0, column=0) 
    lambda: page4.tkraise()
    page1.grid_forget()
    page2.grid_forget()
    page3.grid_forget()
    openpage.grid_forget()
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
        reslbl.configure(text=f"""incorrect! 
                          The answer was {correct_answer}""")
        # image_label.configure(image="")
        
    ent.delete(0, END)
    nextq()


def nextq():
    global current_q_index
    current_q_index += 1
    if current_q_index < total_q:
        updateq()
    else:
        reslbl.configure(text=" ")
        image_label.configure(text=" ")
        qlbl.configure(text=f"You scores {score} out of {total_q}")
    


def update_language(event=None):
    selected_language_code = langlist[language_var.get()]
    translator = GoogleTranslator(source='auto', target=selected_language_code)

    translated_lbl1 = translator.translate("instructions:part 1")
    translated_l1 = translator.translate("""
         a triangle will be shown to you. 
         calculate angle and identify the triangle.
         if your answer is correct then you will earn 1 point. 
         if the answer is wrong no points will be deducted. 
         answer every question before the 60 second timer runs out
         """)
    translated_playbutt1 = translator.translate("Instructions")
    translated_butt1 = translator.translate("next")
  

    lbl1.configure(text=translated_lbl1)
    t1.configure(text=translated_l1)
    playbutt1.configure(text=translated_playbutt1)
    butt1.configure(text=translated_butt1)


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



root.bind("<Return>", clicked)

# open page 
imagepath = "C:/Users/praja/OneDrive/Desktop/12sdd/triangle2 open page.png"
firstimg = ImageTk.PhotoImage(Image.open(imagepath))
fi = Label(openpage, image=firstimg, text="")
fi.grid(row=1, column=1) 

label = customtkinter.CTkLabel(openpage, text= "press enter")
label.grid(row=2, column=1)


openpage.tkraise() 


# open page 
openpage.bind("<Return>", clicked)
imagepath = "C:/Users/praja/OneDrive/Desktop/12sdd/triangle2 open page.png"
firstimg = ImageTk.PhotoImage(Image.open(imagepath))
fi = Label(openpage, image=firstimg, text="")
fi.grid(row=1, column=1) 

label = customtkinter.CTkLabel(openpage, text= "press enter to start")
label.grid(row=2, column=1)




# instructions page 1 
lbl = customtkinter.CTkLabel(page1, text="            ")
lbl.grid(row=2, column=0)

lbl1 = customtkinter.CTkLabel(page1, text="instructions:part 1", font = default_font) 
lbl1.grid(row=0, column=1)

t1= customtkinter.CTkLabel(page1, text="""
         a triangle will be shown to you. 
         calculate angle and identify the triangle.
         if your answer is correct then you will earn 1 point. 
         if the answer is wrong no points will be deducted. 
         answer every question before the 60 second timer runs out
         """, font = default_font)
t1.grid(row=1, column=1)

butt1 = customtkinter.CTkButton(page1, text="next",command=show_page2, font = default_font)
butt1.grid(row=2, column=2)

playbutt1 = customtkinter.CTkButton(page1, text="Instructions", command=lambda: play("instructions part 1"), font = default_font)
playbutt1.grid(row=0, column=2)

playbutt2 = customtkinter.CTkButton(page1, text="Instructions", font = default_font, command=lambda: play("a triangle will be shown to you. calculate angle and identify the triangle.if your answer is correct then you will earn 1 point. if the answer is wrong no points will be deducted. answer every question before the 60 second timer runs out"))
playbutt2.grid(row=2, column=1)

#instructions page 2
lbl2 = customtkinter.CTkLabel(page2, text="instructions:part 2", font = default_font)
lbl2.grid(row=0, column=1)

imagepath = "C:/Users/praja/OneDrive/Desktop/12sdd/New folder/ins2triangles1-removebg.png"
img1 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img1, text="")
t2.grid(row=1, column=1) 

imagepath = "C:/Users/praja/OneDrive/Desktop/12sdd/New folder/ins2triangles2-removebg.png"
img2 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img2, text="")
t2.grid(row=2, column=1) 

imagepath = "C:/Users/praja/OneDrive/Desktop/12sdd/New folder/ins2triangles3-removebg.png"
img3 = ImageTk.PhotoImage(Image.open(imagepath))
t2 = Label(page2, image=img3, text="")
t2.grid(row=3, column=1) 

butt2 = customtkinter.CTkButton(page2, text="next",command=show_page3, font = default_font)
butt2.grid(row=4, column=2)

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
playbutt3.grid(row=0, column=4)

playbutt4 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("an equilateral triangle has three equal sides"), font = default_font)
playbutt4.grid(row=1, column=4)

playbutt5 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("an isosceles triangle has two equal sides"), font = default_font)
playbutt5.grid(row=2, column=4)

playbutt6 = customtkinter.CTkButton(page2, text="Instructions", command=lambda: play("a scalene triangle has no equal sides"), font = default_font)
playbutt6.grid(row=3, column=4)

# instructions page 3
lbl3 = customtkinter.CTkLabel(page3, text="instructions:part 3", font = default_font)
lbl3.grid(row=0, column=1)

sbutt3 = customtkinter.CTkButton(page3, text="start",command=show_page4, font = default_font)
sbutt3.grid(row=4, column=2)

bbutt2 = customtkinter.CTkButton(page3, text="back",command=show_page2, font = default_font)
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

qlbl = customtkinter.CTkLabel(page4, text="", font = default_font)
qlbl.grid(row=0, column=0)

reslbl = customtkinter.CTkLabel(page4, text="", font = default_font)
reslbl.grid(row=3, column=0)

ent = customtkinter.CTkEntry(page4, font = default_font)
ent.grid(row=1, column=0)

subutt = customtkinter.CTkButton(page4, text="submit", command=checkanswer, font = default_font)
subutt.grid(row=2, column=0)

image_label = Label(page4)
image_label.grid(row=2, column=3)




#font size
font_sizes = [24, 26, 28, 32, 34]
selected_size = StringVar()
fontsize_combo1 = ttk.Combobox(page1, textvariable=selected_size, values=font_sizes, width=2, font = default_font)
fontsize_combo2 = ttk.Combobox(page2, textvariable=selected_size, values=font_sizes, width=2, font = default_font)
fontsize_combo3 = ttk.Combobox(page3, textvariable=selected_size, values=font_sizes, width=2, font = default_font)
fontsize_combo4 = ttk.Combobox(page4, textvariable=selected_size, values=font_sizes, width=2, font = default_font)

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

 
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(page1, textvariable=language_var, width=6, font = default_font)
language_dropdown['values'] = list(langlist.keys())
language_dropdown.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
language_dropdown.bind('<<ComboboxSelected>>', update_language)
language_var.set('English')


root.mainloop()
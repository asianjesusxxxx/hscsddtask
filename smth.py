import customtkinter as ctk
from PIL import Image, ImageTk

# Initialize the customtkinter application
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Quiz Application")

# Define questions and answers
questions = [
    {"question": "What is 2 + 2?", "answer": "4", "image": "C:/Users/praja/OneDrive/Pictures/Screenshots/Screenshot 2023-05-24 001325.png"},
    # {"question": "What is the capital of France?", "answer": "Paris", "image": "path/to/image2.png"},
    # {"question": "What is 5 * 3?", "answer": "15", "image": "path/to/image3.png"},
    # {"question": "What is the largest ocean?", "answer": "Pacific", "image": "path/to/image4.png"},
    # {"question": "What is the square root of 81?", "answer": "9", "image": "path/to/image5.png"},
    # {"question": "What is the capital of Italy?", "answer": "Rome", "image": "path/to/image6.png"},
    # {"question": "What is 7 + 6?", "answer": "13", "image": "path/to/image7.png"},
    # {"question": "What is the largest planet?", "answer": "Jupiter", "image": "path/to/image8.png"},
    # {"question": "What is the boiling point of water?", "answer": "100", "image": "path/to/image9.png"},
    # {"question": "What is the capital of Japan?", "answer": "Tokyo", "image": "path/to/image10.png"},
]


# C:/Users/praja/OneDrive/Pictures/Screenshots 

current_q_index = 0
score = 0

# Function to update the question and image
def update_question():
    global current_q_index
    question_data = questions[current_q_index]
    question_label.configure(text=question_data["question"])
    
    # Load and resize the image
    image = Image.open(question_data["image"])
    resized_image = image.resize(200, 200, Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(resized_image)
    
    image_label.configure(image=tk_image)
    image_label.image = tk_image  # Keep a reference to avoid garbage collection

# Function to check the answer
def check_answer():
    global current_q_index, score
    user_answer = answer_entry.get()
    correct_answer = questions[current_q_index]["answer"]
    if user_answer.lower().strip() == correct_answer.lower().strip():
        result_label.configure(text="Correct!", fg="green")
        score += 1
    else:
        result_label.configure(text=f"Incorrect! The correct answer was {correct_answer}", fg="red")
    answer_entry.delete(0, ctk.END)
    
    # Move to the next question
    current_q_index += 1
    if current_q_index < len(questions):
        update_question()
    else:
        # Show the final score
        question_label.configure(text=f"You scored {score} out of {len(questions)}")
        image_label.configure(image="")
        answer_entry.grid_remove()
        submit_button.grid_remove()

# Create widgets
question_label = ctk.CTkLabel(app, text="", font=("Arial", 20))
question_label.pack(pady=20)

image_label = ctk.CTkLabel(app)
image_label.pack(pady=20)

answer_entry = ctk.CTkEntry(app)
answer_entry.pack(pady=10)

submit_button = ctk.CTkButton(app, text="Submit", command=check_answer)
submit_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
result_label.pack(pady=20)

# Initialize the first question
update_question()

# Start the application
app.mainloop()

import tkinter as tk
import customtkinter

# Initialize the main window
root = tk.Tk()
root.title('Triangles')
root.geometry("1600x800")

# Set initial appearance mode and color theme
customtkinter.set_appearance_mode("system")  # Use system settings initially
customtkinter.set_default_color_theme("green")

# Initialize the current appearance mode
current_mode = customtkinter.get_appearance_mode()

# Define the function to change the theme
def change_theme():
    global current_mode
    if current_mode == "light":
        customtkinter.set_appearance_mode("dark")
        current_mode = "dark"
    else:
        customtkinter.set_appearance_mode("light")
        current_mode = "light"

# Create a page for the button
page1 = tk.Frame(root)
page1.grid(row=0, column=0, sticky="nsew")

# Create and place the theme toggle button
theme_button = customtkinter.CTkButton(page1, text="Theme", font=("Arial", 12), command=change_theme)
theme_button.grid(row=0, column=6, padx=10, pady=10)

# Run the main event loop
root.mainloop()

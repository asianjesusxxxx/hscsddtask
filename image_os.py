import os
from tkinter import *
from PIL import Image, ImageTk

# Initialize the Tkinter root
root = Tk()

# Set up paths
script_dir = os.path.dirname(__file__)
image_dir = os.path.join(script_dir, 'images')

# List of image filenames
image_files = [
    'ins2triangles1-removebg.png',
    'ins2triangles2-removebg.png',
    'ins2triangles3-removebg.png'
]

# Function to load and display images
def load_and_display_images(image_files):
    images = []
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(image_dir, image_file)
        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue
        img = ImageTk.PhotoImage(Image.open(image_path))
        images.append(img)
        label = Label(root, image=img)
        label.grid(row=i + 1, column=1)
    return images

# Load and display images
images = load_and_display_images(image_files)

# Start the Tkinter main loop
root.mainloop()

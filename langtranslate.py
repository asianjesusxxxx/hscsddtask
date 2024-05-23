import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

# Function to update translations based on selected language
def update_language(event=None):
    selected_language_code = languages[language_var.get()]
    translator = GoogleTranslator(source='auto', target=selected_language_code)

    translated_label1 = translator.translate("Label 1")
    translated_label2 = translator.translate("Label 2")
    translated_entry1 = translator.translate("Entry 1:")
    translated_entry2 = translator.translate("Entry 2:")
    translated_entry2 = translator.translate("Entry 2:")



    label1.config(text=translated_label1)
    label2.config(text=translated_label2)
    entry1_label.config(text=translated_entry1)
    entry2_label.config(text=translated_entry2)

# Main application window
root = tk.Tk()
root.title("Multi-language GUI")

# Variables
language_var = tk.StringVar()

# Language options (ISO 639-1 codes)
languages = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese': 'zh-CN',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru'
}

# Label widgets
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=1, column=0, padx=10, pady=10)

# Entry widgets with labels
entry1_label = tk.Label(root, text="Entry 1:")
entry1_label.grid(row=2, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=2, column=1, padx=10, pady=10)

entry2_label = tk.Label(root, text="Entry 2:")
entry2_label.grid(row=3, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=3, column=1, padx=10, pady=10)

# Dropdown for language selection
language_dropdown = ttk.Combobox(root, textvariable=language_var)
language_dropdown['values'] = list(languages.keys())
language_dropdown.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
language_dropdown.bind('<<ComboboxSelected>>', update_language)

# Default language
language_var.set('English')

# Start the main event loop
root.mainloop()

from tkinter import *
from tkinter import ttk
from googletrans import Translator

# Window create
root = Tk()
root.title("Language Translator")
root.geometry("600x500")
root.config(bg="lightblue")

# Translator object
translator = Translator()

# Languages dictionary
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Hindi": "hi",
    "Arabic": "ar"
}

# Translate function
def translate_text():
    text = input_text.get("1.0", END)

    source_lang = languages[source_combo.get()]
    target_lang = languages[target_combo.get()]

    translated = translator.translate(
        text,
        src=source_lang,
        dest=target_lang
    )

    output_text.delete("1.0", END)
    output_text.insert(END, translated.text)

# Copy function
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", END))

# Heading
heading = Label(
    root,
    text="Language Translator",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
heading.pack(pady=10)

# Input label
input_label = Label(
    root,
    text="Enter Text",
    font=("Arial", 12),
    bg="lightblue"
)
input_label.pack()

# Input text box
input_text = Text(root, height=7, width=50)
input_text.pack(pady=5)

# Source language
source_combo = ttk.Combobox(
    root,
    values=list(languages.keys())
)
source_combo.pack(pady=5)
source_combo.set("English")

# Target language
target_combo = ttk.Combobox(
    root,
    values=list(languages.keys())
)
target_combo.pack(pady=5)
target_combo.set("Urdu")

# Translate button
translate_btn = Button(
    root,
    text="Translate",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=translate_text
)
translate_btn.pack(pady=10)

# Output label
output_label = Label(
    root,
    text="Translated Text",
    font=("Arial", 12),
    bg="lightblue"
)
output_label.pack()

# Output text box
output_text = Text(root, height=7, width=50)
output_text.pack(pady=5)

# Copy button
copy_btn = Button(
    root,
    text="Copy Text",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    command=copy_text
)
copy_btn.pack(pady=10)

# Run app
root.mainloop()
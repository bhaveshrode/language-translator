import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator

# Create the translator instance
translator = Translator()

# Create language dictionary: name -> code
language_dict = {language.title(): code for code, language in LANGUAGES.items()}
languages = list(language_dict.keys())
languages.sort()

# GUI Setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("700x400")
root.resizable(False, False)

def translate_text():
    try:
        src_lang_name = source_lang_combo.get()
        dest_lang_name = target_lang_combo.get()
        input_text = text_input.get("1.0", tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Input Needed", "Please enter text to translate.")
            return
            
        src_code = 'auto' if src_lang_name == "Auto Detect" else language_dict.get(src_lang_name)
        dest_code = language_dict.get(dest_lang_name)
        
        translation = translator.translate(input_text, src = src_code, dest = dest_code)
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, translation.text)
        
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Labels
tk.Label(root, text = "Enter Text: ", font = ("Helvetica", 12)).place(x = 30, y = 60)
tk.Label(root, text = "Translated Text: ", font = ("Helvetica", 12)).place(x = 370, y = 60)

# Dropdowns
tk.Label(root, text = "From: ", font = ("Helvetica", 10)).place(x = 30, y = 30)
source_lang_combo = ttk.Combobox(root, values = ["Auto Detect"] + languages, width = 20)
source_lang_combo.set("Auto Detect")
source_lang_combo.place(x = 75, y = 30)

tk.Label(root, text = "To: ", font = ("Helvetica", 10)).place(x = 370, y = 30)
target_lang_combo = ttk.Combobox(root, values = languages, width = 20)
target_lang_combo.set("Hindi")
target_lang_combo.place(x = 410, y = 30)

# Text Boxes
text_input = tk.Text(root, height = 10, width = 35, wrap = "word")
text_input.place(x = 30, y = 90)

translated_text = tk.Text(root, height = 10, width = 35, wrap = "word")
translated_text.place(x = 370, y = 90)

# Translate Button
translate_button = tk.Button(root, text = "Translate", font = ("Helvetica", 12, "bold"), bg = "grey", fg = "white", command = translate_text)
translate_button.place(x = 300, y = 320)

# Run App
root.mainloop()
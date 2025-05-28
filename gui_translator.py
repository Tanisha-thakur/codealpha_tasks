import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src_lang = source_lang_entry.get().strip()
    dest_lang = target_lang_entry.get().strip()

    if not text or not dest_lang:
        messagebox.showerror("Input Error", "Please enter text and target language code.")
        return

    try:
        translator = Translator()
        translated = translator.translate(text, src=src_lang or 'auto', dest=dest_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x400")
root.config(padx=10, pady=10)

tk.Label(root, text="Enter Text:", font=("Arial", 12, "bold")).pack(anchor="w")
input_text = tk.Text(root, height=5, width=60)
input_text.pack()

tk.Label(root, text="Source Language Code (e.g., 'en' or leave blank for auto):").pack(anchor="w")
source_lang_entry = tk.Entry(root, width=30)
source_lang_entry.insert(0, "auto")
source_lang_entry.pack()

tk.Label(root, text="Target Language Code (e.g., 'fr', 'es', 'hi'):", font=("Arial", 10)).pack(anchor="w")
target_lang_entry = tk.Entry(root, width=30)
target_lang_entry.pack()

tk.Button(root, text="Translate", command=translate_text, bg="lightblue").pack(pady=10)

tk.Label(root, text="Translated Text:", font=("Arial", 12, "bold")).pack(anchor="w")
output_text = tk.Text(root, height=5, width=60)
output_text.pack()

root.mainloop()

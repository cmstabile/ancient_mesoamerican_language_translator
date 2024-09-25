import tkinter as tk
import os


def load_nahuatl_words():
    words = {}  # Now a dictionary for word:definition pairs
    with open("Nahuatl-Word-List.txt", "r", encoding="latin-1") as f:
        for line in f:
            if ',' in line:  # Check if line contains a comma
                word, definition = line.strip().split(",", 1)  # Assuming comma-separated format
                words[word] = definition
            else:
                print(f"Skipping line due to format issue: {line.strip()}")
    return words


# Define the translation function before it is used
def translate():
    selected_word = word_var.get()
    definition = nahuatl_words.get(selected_word)

    output_text.delete("1.0", "end-1c")
    if definition:
        output_text.insert("1.0", definition)
    else:
        output_text.insert("1.0", "Definition not found.")


nahuatl_words = load_nahuatl_words()
root = tk.Tk()
root.title("Language Translator")

# Language selector dropdown
languages = ["Nahuatl", "Aztec", "Taino"]
language_var = tk.StringVar()
language_var.set(languages[0])  # Default to Nahuatl
language_dropdown = tk.OptionMenu(root, language_var, *languages)
language_dropdown.pack()

# Nahuatl word dropdown
word_var = tk.StringVar()
word_dropdown = tk.OptionMenu(root, word_var, *nahuatl_words.keys())  # Use keys for dropdown list
word_dropdown.pack()

# Output text box
output_text = tk.Text(root, height=5, width=40)
output_text.pack()

# Translation button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

root.mainloop()
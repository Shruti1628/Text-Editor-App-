import tkinter as tk
from tkinter import filedialog, messagebox

# Main Window
root = tk.Tk()
root.title("Shruti's Simple TextEditor")
root.geometry("800x600")

# Create Text Area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Consolas", 18),
    insertbackground="white",
    selectbackground="#5d5269",
    selectforeground="#D41C50",
    undo=True
)
text.pack(expand=True, fill=tk.BOTH)

# Main Logic

# Function 1: Create a New File
def new_file():
    if messagebox.askyesno("New File", "Clear the current text?"):
        text.delete("1.0", tk.END)

# Function 2: Open a File
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()

            text.delete("1.0", tk.END)
            text.insert(tk.END, content)
        except OSError as error:
            messagebox.showerror("Error", f"Could not open file:\n{error}")

# Function 3: Save a File
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text.get("1.0", "end-1c"))

            messagebox.showinfo("Success", "File saved successfully!")
        except OSError as error:
            messagebox.showerror("Error", f"Could not save file:\n{error}")

# Function 4: Save As
def save_as():
    save_file()

# Create Menu Bar
menu = tk.Menu(root)
root.config(menu=menu)

# File Menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit Menu
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)
edit_menu.add_separator()

edit_menu.add_command(
    label="Cut",
    command=lambda: text.event_generate("<<Cut>>")
)
edit_menu.add_command(
    label="Copy",
    command=lambda: text.event_generate("<<Copy>>")
)
edit_menu.add_command(
    label="Paste",
    command=lambda: text.event_generate("<<Paste>>")
)
edit_menu.add_command(
    label="Select All",
    command=lambda: text.tag_add("sel", "1.0", "end-1c")
)

# Format Menu
format_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Format", menu=format_menu)

format_menu.add_command(
    label="Change Background",
    command=lambda: text.config(bg="lightyellow")
)
format_menu.add_command(
    label="Change Text Color",
    command=lambda: text.config(fg="blue")
)
format_menu.add_command(
    label="Increase Font Size",
    command=lambda: text.config(font=("Consolas", 20))
)

# Help Menu
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About",
        "Shruti's Simple TextEditor\nCreated using Python Tkinter"
    )
)

# Start Application
root.mainloop()
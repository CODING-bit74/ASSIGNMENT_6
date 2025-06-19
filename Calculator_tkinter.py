from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont

# Create the main window
window = Tk()
window.title("Calculator")
window.geometry("420x700")
window.resizable(False, False)
window.configure(bg="lightgray")

# Create a label for the title
title_label = Label(window, text="Simple Calculator", font=("Arial", 24), bg="lightgray", fg="black")
title_label.place(x=50, y=10, width=300, height=40)

# Entry widget to store the input
E = Entry(window, font=("Arial", 20, "bold"), bd=8, relief=SUNKEN, justify='right', bg="white", fg="black", insertbackground="black")
E.place(x=10, y=60, width=380, height=60)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(E.get())
        E.delete(0, END)
        E.insert(0, str(result))
        update_status("Success")
    except:
        messagebox.showerror("Error", "Invalid Input")
        update_status("Error")

# Function to update the status bar
def update_status(message):
    status_bar.config(text=message)

# Function to handle backspace
def backspace():
    current = E.get()
    if current:
        E.delete(len(current) - 1, END)

# Button specifications: (text, x, y)
buttons = [
    ("1", 10, 140), ("2", 110, 140), ("3", 210, 140), ("C", 310, 140),
    ("4", 10, 240), ("5", 110, 240), ("6", 210, 240), ("⌫", 310, 240),
    ("7", 10, 340), ("8", 110, 340), ("9", 210, 340), (".", 310, 340),
    ("+", 10, 440), ("0", 110, 440), ("-", 210, 440), ("*", 310, 440),
    ("/", 10, 540), ("(", 110, 540), (")", 210, 540), ("=", 310, 540)
]

for (text, x, y) in buttons:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = lambda: E.delete(0, END)
    elif text == "⌫":
        cmd = backspace
    else:
        cmd = lambda t=text: E.insert(END, t)

    Button(window, text=text, font=("Arial", 18), padx=10, pady=10,
           relief=GROOVE, command=cmd, bg="lightblue", fg="black").place(x=x, y=y, width=90, height=90)

# Status bar
status_bar = Label(window, text="Calculator Ready", bd=1, relief=SUNKEN, anchor=W, bg="lightgray", fg="black")
status_bar.place(x=0, y=650, width=400, height=30)

# Menu bar
menu_bar = Menu(window)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: E.delete(0, END))
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Simple Calculator\nVersion 1.1\nCreated by OpenAI"))
menu_bar.add_cascade(label="Help", menu=help_menu)

# Attach menu bar
window.config(menu=menu_bar)

# Set default font
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=12)

# Run the application
window.mainloop()

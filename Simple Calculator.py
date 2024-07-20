import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

# Create main window
window = tk.Tk()
window.title('Personalized Calculator')
window.config(bg='lightblue')

# Create a frame for the calculator
frame = tk.Frame(master=window, bg="skyblue", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Entry widget for displaying calculations
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=5)

# Function to handle button clicks
def myclick(number):
    entry.insert(tk.END, number)

# Function to evaluate the expression
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Button creation function
def create_button(text, row, column, width=3, columnspan=1, command=None):
    button = tk.Button(master=frame, text=text, padx=15, pady=5, width=width, font=('Arial', 12), command=command, bg='white')
    button.grid(row=row, column=column, columnspan=columnspan, pady=5)
    return button

# Create buttons
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1),
    ('+', 5, 0), ('-', 5, 1), ('*', 5, 2), ('/', 6, 0),
    ('clear', 6, 1, 12, 2, clear),
    ('=', 7, 0, 9, 4, equal)
]

# Add buttons to the frame
for (text, row, col, *args) in buttons:
    width = args[0] if args else 3
    columnspan = args[1] if len(args) > 1 else 1
    command = args[2] if len(args) > 2 else lambda t=text: myclick(t)
    create_button(text, row, col, width, columnspan, command)

# Run the application
window.mainloop()

import tkinter as tk
from tkinter import messagebox

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + event.widget.cget("text"))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display calculations
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_value = 1
col_value = 0

for button in buttons:
    b = tk.Button(root, text=button, font=('Arial', 18), width=4, height=2)
    b.grid(row=row_value, column=col_value)
    
    if button == "=":
        b.bind('<Button-1>', lambda event: calculate())
    elif button == "C":
        b.bind('<Button-1>', lambda event: clear())
    else:
        b.bind('<Button-1>', click)
    
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Run the application
root.mainloop()

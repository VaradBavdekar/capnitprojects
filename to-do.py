import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to update a selected task
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, entry.get())
        entry.delete(0, tk.END)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Function to handle closing the app
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Create entry widget for input
entry = tk.Entry(root, width=40, font=('Arial', 14))
entry.grid(row=0, column=0, padx=20, pady=10, columnspan=3)

# Add Task button
add_button = tk.Button(root, text="Add Task", width=10, font=('Arial', 12), command=add_task)
add_button.grid(row=0, column=3, padx=10)

# Listbox to display tasks
task_listbox = tk.Listbox(root, height=10, width=50, font=('Arial', 14), selectmode=tk.SINGLE)
task_listbox.grid(row=1, column=0, columnspan=4, padx=20, pady=10)

# Update and Delete buttons
update_button = tk.Button(root, text="Update Task", width=12, font=('Arial', 12), command=update_task)
update_button.grid(row=2, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", width=12, font=('Arial', 12), command=delete_task)
delete_button.grid(row=2, column=2, padx=10, pady=10)

# Clear All button
clear_button = tk.Button(root, text="Clear All Tasks", width=14, font=('Arial', 12), command=clear_tasks)
clear_button.grid(row=3, column=0, columnspan=4, padx=20, pady=10)

# Handle closing the app
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the main event loop
root.mainloop()

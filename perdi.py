import tkinter as tk
from tkinter import messagebox, filedialog

# Function to save diary entry
def save_entry():
    text = diary_text.get("1.0", tk.END)
    
    if text.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save Diary Entry")
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
            messagebox.showinfo("Success", "Diary entry saved successfully!")
    else:
        messagebox.showwarning("Input Error", "Diary entry is empty! Please write something before saving.")

# Function to open an existing diary entry
def open_entry():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt")],
                                           title="Open Diary Entry")
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            diary_text.delete("1.0", tk.END)
            diary_text.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Personal Diary")

# Create a Text widget for diary entry
diary_text = tk.Text(root, wrap="word", font=("Arial", 14), width=50, height=20)
diary_text.pack(padx=10, pady=10)

# Frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Save button
save_button = tk.Button(button_frame, text="Save Entry", font=("Arial", 12), command=save_entry)
save_button.grid(row=0, column=0, padx=5)

# Open button
open_button = tk.Button(button_frame, text="Open Entry", font=("Arial", 12), command=open_entry)
open_button.grid(row=0, column=1, padx=5)

# Run the main event loop
root.mainloop()

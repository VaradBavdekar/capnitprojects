import tkinter as tk
from tkinter import messagebox
import random

# Function to check the user's guess
def check_guess():
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 100:
            result_label.config(text="Please enter a number between 1 and 100.")
        else:
            global attempts
            attempts += 1
            if guess < secret_number:
                result_label.config(text="Too low! Try again.")
            elif guess > secret_number:
                result_label.config(text="Too high! Try again.")
            else:
                result_label.config(text=f"Correct! You guessed it in {attempts} attempts.")
                guess_button.config(state="disabled")  # Disable the button after guessing
    except ValueError:
        result_label.config(text="Invalid input! Please enter a number.")

# Function to start a new game
def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Guess a number between 1 and 100.")
    entry.delete(0, tk.END)
    guess_button.config(state="normal")  # Enable the guess button

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Game introduction
intro_label = tk.Label(root, text="Welcome to the Number Guessing Game!", font=('Arial', 14))
intro_label.pack(pady=10)

instruction_label = tk.Label(root, text="I have selected a number between 1 and 100. Can you guess it?", font=('Arial', 12))
instruction_label.pack(pady=5)

# Entry widget for user guesses
entry = tk.Entry(root, width=10, font=('Arial', 14))
entry.pack(pady=10)

# Button to submit the guess
guess_button = tk.Button(root, text="Guess", font=('Arial', 12), command=check_guess)
guess_button.pack(pady=5)

# Label to display result and feedback
result_label = tk.Label(root, text="Guess a number between 1 and 100.", font=('Arial', 12))
result_label.pack(pady=10)

# Button to start a new game
new_game_button = tk.Button(root, text="New Game", font=('Arial', 12), command=new_game)
new_game_button.pack(pady=5)

# Initialize the game
secret_number = random.randint(1, 100)
attempts = 0

# Run the main event loop
root.mainloop()

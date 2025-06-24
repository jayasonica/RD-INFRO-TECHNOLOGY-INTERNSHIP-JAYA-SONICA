import tkinter as tk
import random
import string
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a positive integer.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.configure(bg="#f0f0f0")

# UI Elements
tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
length_entry = tk.Entry(root, width=10, font=("Arial", 12))
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, state="readonly").pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Arial", 11)).pack(pady=10)

# Run the app
root.mainloop()

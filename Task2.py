import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

# Entry fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
tk.Label(root, text="Select operation:").pack()
operation = tk.StringVar(root)
operation.set('+')  # default value

options = ['+', '-', '*', '/']
tk.OptionMenu(root, operation, *options).pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white").pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack()

# Run the app
root.mainloop()

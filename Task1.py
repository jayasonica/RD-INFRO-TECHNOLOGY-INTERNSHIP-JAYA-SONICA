import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

root.mainloop()

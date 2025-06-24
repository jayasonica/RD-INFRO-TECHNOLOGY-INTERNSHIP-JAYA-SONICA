import tkinter as tk
from tkinter import messagebox

# Contact list
contacts = []

# Add a contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        messagebox.showinfo("Success", "Contact added successfully.")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

# View all contacts
def view_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Search contacts
def search_contact():
    search_term = entry_search.get().lower()
    listbox.delete(0, tk.END)
    for contact in contacts:
        if search_term in contact["name"].lower() or search_term in contact["phone"]:
            listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Select a contact
def select_contact(event):
    index = listbox.curselection()
    if index:
        selected = contacts[index[0]]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, selected["name"])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, selected["phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, selected["email"])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, selected["address"])

# Update contact
def update_contact():
    index = listbox.curselection()
    if index:
        contacts[index[0]] = {
            "name": entry_name.get(),
            "phone": entry_phone.get(),
            "email": entry_email.get(),
            "address": entry_address.get()
        }
        messagebox.showinfo("Updated", "Contact updated successfully.")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Select Error", "Please select a contact to update.")

# Delete contact
def delete_contact():
    index = listbox.curselection()
    if index:
        del contacts[index[0]]
        messagebox.showinfo("Deleted", "Contact deleted successfully.")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Select Error", "Please select a contact to delete.")

# Clear fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x550")
root.configure(bg="#f0f0f0")

# Labels and Entries
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root, width=50)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root, width=50)
entry_address.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="#F44336", fg="white").pack(pady=5)

# Search bar
tk.Label(root, text="Search by Name or Phone").pack(pady=5)
entry_search = tk.Entry(root, width=30)
entry_search.pack()
tk.Button(root, text="Search", command=search_contact).pack()

# Contact list
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_contact)

# View All Button
tk.Button(root, text="View All Contacts", command=view_contacts).pack()

# Run the app
root.mainloop()

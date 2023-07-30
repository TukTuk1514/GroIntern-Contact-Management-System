import tkinter as tk
from tkinter import ttk
import sqlite3


conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        gender TEXT,
        age INTEGER,
        address TEXT,
        contact TEXT
    )
''')
conn.commit()

def add_contact():
    def save_contact():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        gender = entry_gender.get()
        age = entry_age.get()
        address = entry_address.get()
        contact = entry_contact.get()

        cursor.execute('''
            INSERT INTO contacts (first_name, last_name, gender, age, address, contact)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, gender, age, address, contact))
        conn.commit()

        view_contacts()
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Add New Contact")

    label_first_name = tk.Label(top, text="First Name:")
    label_first_name.grid(row=0, column=0, padx=5, pady=5)
    entry_first_name = tk.Entry(top)
    entry_first_name.grid(row=0, column=1, padx=5, pady=5)

    label_last_name = tk.Label(top, text="Last Name:")
    label_last_name.grid(row=1, column=0, padx=5, pady=5)
    entry_last_name = tk.Entry(top)
    entry_last_name.grid(row=1, column=1, padx=5, pady=5)

    label_gender = tk.Label(top, text="Gender:")
    label_gender.grid(row=2, column=0, padx=5, pady=5)
    entry_gender = tk.Entry(top)
    entry_gender.grid(row=2, column=1, padx=5, pady=5)

    label_age = tk.Label(top, text="Age:")
    label_age.grid(row=3, column=0, padx=5, pady=5)
    entry_age = tk.Entry(top)
    entry_age.grid(row=3, column=1, padx=5, pady=5)

    label_address = tk.Label(top, text="Address:")
    label_address.grid(row=4, column=0, padx=5, pady=5)
    entry_address = tk.Entry(top)
    entry_address.grid(row=4, column=1, padx=5, pady=5)

    label_contact = tk.Label(top, text="Contact:")
    label_contact.grid(row=5, column=0, padx=5, pady=5)
    entry_contact = tk.Entry(top)
    entry_contact.grid(row=5, column=1, padx=5, pady=5)

    button_save = tk.Button(top, text="Save", command=save_contact)
    button_save.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

def update_contact():
    selected_item = tree.selection()
    if not selected_item:
        return

    member_id = tree.item(selected_item)['values'][0]

    cursor.execute('SELECT * FROM contacts WHERE member_id=?', (member_id,))
    contact_data = cursor.fetchone()

    def save_update():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        gender = entry_gender.get()
        age = entry_age.get()
        address = entry_address.get()
        contact = entry_contact.get()

        cursor.execute('''
            UPDATE contacts
            SET first_name=?, last_name=?, gender=?, age=?, address=?, contact=?
            WHERE member_id=?
        ''', (first_name, last_name, gender, age, address, contact, member_id))
        conn.commit()

        view_contacts()
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Update Contact")

    label_first_name = tk.Label(top, text="First Name:")
    label_first_name.grid(row=0, column=0, padx=5, pady=5)
    entry_first_name = tk.Entry(top)
    entry_first_name.grid(row=0, column=1, padx=5, pady=5)
    entry_first_name.insert(0, contact_data[1])

    label_last_name = tk.Label(top, text="Last Name:")
    label_last_name.grid(row=1, column=0, padx=5, pady=5)
    entry_last_name = tk.Entry(top)
    entry_last_name.grid(row=1, column=1, padx=5, pady=5)
    entry_last_name.insert(0, contact_data[2])

    label_gender = tk.Label(top, text="Gender:")
    label_gender.grid(row=2, column=0, padx=5, pady=5)
    entry_gender = tk.Entry(top)
    entry_gender.grid(row=2, column=1, padx=5, pady=5)
    entry_gender.insert(0, contact_data[3])

    label_age = tk.Label(top, text="Age:")
    label_age.grid(row=3, column=0, padx=5, pady=5)
    entry_age = tk.Entry(top)
    entry_age.grid(row=3, column=1, padx=5, pady=5)
    entry_age.insert(0, contact_data[4])

    label_address = tk.Label(top, text="Address:")
    label_address.grid(row=4, column=0, padx=5, pady=5)
    entry_address = tk.Entry(top)
    entry_address.grid(row=4, column=1, padx=5, pady=5)
    entry_address.insert(0, contact_data[5])

    label_contact = tk.Label(top, text="Contact:")
    label_contact.grid(row=5, column=0, padx=5, pady=5)
    entry_contact = tk.Entry(top)
    entry_contact.grid(row=5, column=1, padx=5, pady=5)
    entry_contact.insert(0, contact_data[6])

    button_save = tk.Button(top, text="Save", command=save_update)
    button_save.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

def delete_contact():
    selected_item = tree.selection()
    if not selected_item:
        return

    member_id = tree.item(selected_item)['values'][0]
    cursor.execute('DELETE FROM contacts WHERE member_id=?', (member_id,))
    conn.commit()

    view_contacts()

def view_contacts():
    tree.delete(*tree.get_children())
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    for contact in contacts:
        tree.insert("", "end", values=contact)

root = tk.Tk()
root.title("Contact Management System")


columns = ("MemberID", "Firstname", "Lastname", "Gender", "Age", "Address", "Contact")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(padx=10, pady=10)


frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

button_add = tk.Button(frame_buttons, text="Add Contact", command=add_contact)
button_add.pack(side=tk.LEFT, padx=5)

button_update = tk.Button(frame_buttons, text="Update Contact", command=update_contact)
button_update.pack(side=tk.LEFT, padx=5)

button_delete = tk.Button(frame_buttons, text="Delete Contact", command=delete_contact)
button_delete.pack(side=tk.LEFT, padx=5)


view_contacts()

root.mainloop()


conn.close()

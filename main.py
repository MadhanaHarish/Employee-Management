from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
from db import Database

db = Database("Employee.db")

# Create the login window
def login_window():
    login_root = Tk()
    login_root.title("Login")
    login_root.geometry("400x300+500+200")
    login_root.config(bg="#2c3e50")

    username = StringVar()
    password = StringVar()

    def login():
        user = username.get()
        pwd = password.get()
        if user == "madhan" and pwd == "admin@123":
            login_root.destroy()
            main_window()
        else:
            messagebox.showerror("Error", "Invalid Username or Password", icon="warning")

    frame = Frame(login_root, bg="#2c3e50")
    frame.pack(pady=50)

    lbl_user = Label(frame, text="Username", font=("Calibri", 20, "bold"), fg="white", bg="#2c3e50")
    lbl_user.grid(row=0, column=0, padx=10, pady=10)
    txt_user = Entry(frame, textvariable=username, font=("Calibri", 15))
    txt_user.grid(row=0, column=1, padx=10, pady=10)

    lbl_pwd = Label(frame, text="Password", font=("Calibri", 20, "bold"), fg="white", bg="#2c3e50")
    lbl_pwd.grid(row=1, column=0, padx=10, pady=10)
    txt_pwd = Entry(frame, textvariable=password, show="*", font=("Calibri", 15))
    txt_pwd.grid(row=1, column=1, padx=10, pady=10)

    btn_login = Button(frame, text="Login", command=login, width=15, font=("Calibri", 15, "bold"), fg="white", bg="#16a085", bd=0)
    btn_login.grid(row=2, column=0, columnspan=2, pady=10)

    login_root.mainloop()

def main_window():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="#2c3e50")
    name = StringVar()
    age = StringVar()
    doj = StringVar()
    gender = StringVar()
    email = StringVar()
    contact = StringVar()
    search_by = StringVar()  # For search criteria
    search_text = StringVar()  # For search input

    def getData(event):
        selected_row = tv.focus()
        data = tv.item(selected_row)
        global row
        row = data["values"]
        name.set(row[1])
        age.set(row[2])
        doj.set(row[3])
        email.set(row[4])
        gender.set(row[5])
        contact.set(row[6])
        txtAddress.delete(1.0, END)
        txtAddress.insert(END, row[7])

    def dispalyAll():
        tv.delete(*tv.get_children())
        for row in db.fetch():
            tv.insert("", END, values=row)

    def add_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or txtContact.get() == "" :
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.insert(txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), gender.get(), txtContact.get(), txtAddress.get(1.0, END), )
        messagebox.showinfo("Success", "Record Inserted")
        clearAll()
        dispalyAll()

    def update_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or txtContact.get() == "" :
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.update(row[0], txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), gender.get(), txtContact.get(), txtAddress.get(1.0, END))
        messagebox.showinfo("Success", "Record Updated")
        clearAll()
        dispalyAll()

    def delete_employee():
        db.remove(row[0])
        clearAll()
        dispalyAll()

    def clearAll():
        name.set("")
        age.set("")
        doj.set("")
        gender.set("")
        email.set("")
        contact.set("")
        txtAddress.delete(1.0, END)

    def search_employee():
        tv.delete(*tv.get_children())
        search_column = search_by.get().lower()
        search_value = search_text.get()
        for row in db.fetch():
            if search_column == "name" and search_value.lower() in row[1].lower():
                tv.insert("", END, values=row)
            elif search_column == "email" and search_value.lower() in row[4].lower():
                tv.insert("", END, values=row)
            # Add other search conditions as necessary

    entries_frame = Frame(root, bg="#535c68")
    entries_frame.pack(side=TOP, fill=X)
    title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
    title.grid(row=0, columnspan=4, padx=10, pady=20, sticky="w")

    lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
    lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
    txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
    txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    lblDoj = Label(entries_frame, text="D.O.J", font=("Calibri", 16), bg="#535c68", fg="white")
    lblDoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtDoj = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
    txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
    lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
    txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
    lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
    comboGender["values"] = ("Male", "Female")
    comboGender.grid(row=3, column=1, padx=10, sticky="w")

    lblContact = Label(entries_frame, text="Contact", font=("Calibri", 16), bg="#535c68", fg="white")
    lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
    txtContact.grid(row=3, column=3, padx=10, sticky="w")

    lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAddress.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    txtAddress = Text(entries_frame, width=90, height=2, font=("Calibri", 16))
    txtAddress.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

    lblSearchBy = Label(entries_frame, text="Search By", font=("Calibri", 16), bg="#535c68", fg="white")
    lblSearchBy.grid(row=7, column=0, padx=10, pady=10, sticky="w")
    comboSearchBy = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=search_by, state="readonly")
    comboSearchBy["values"] = ("Name", "Email")  # Add other fields if needed
    comboSearchBy.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    txtSearch = Entry(entries_frame, textvariable=search_text, font=("Calibri", 16), width=30)
    txtSearch.grid(row=7, column=2, padx=10, pady=10, sticky="w")

    btnSearch = Button(entries_frame, text="Search", command=search_employee, width=15, font=("Calibri", 16, "bold"), fg="white", bg="#16a085", bd=0)
    btnSearch.grid(row=7, column=3, padx=10, pady=10, sticky="w")

    btn_frame = Frame(entries_frame, bg="#535c68")
    btn_frame.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#16a085", bd=0).grid(row=0, column=0)
    Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=10)
    Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#c0392b", bd=0).grid(row=0, column=2, padx=10)
    Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)

    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=480, width=1980, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=("Calibri", 13), rowheight=50)
    style.configure("mystyle.Treeview.Heading", font=("Calibri", 13))
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="ID")
    tv.column("1", width=5)
    tv.heading("2", text="Name")
    tv.heading("3", text="Age")
    tv.heading("4", text="D.O.J")
    tv.heading("5", text="Email")
    tv.heading("6", text="Gender")
    tv.heading("7", text="Contact")
    tv.heading("8", text="Address")
    tv["show"] = "headings"
    tv.pack(fill=X)
    tv.bind("<ButtonRelease-1>", getData)

    dispalyAll()
    root.mainloop()

# Start with the login window
login_window()

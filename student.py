import tkinter as tk
from tkinter import messagebox

# student information

root = tk.Tk()
root.title("Student Information Form")
root.geometry("400x400")
root.configure(bg="#ADD8E6")

fields = ["Student Roll No","Name","Father Name","Class","Phone"]
boxes = []

tk.Label(root, text="Search Roll No").grid(row=0, column=0, pady=5)
search = tk.Entry(root)
search.grid(row=0, column=1)

def search_student():
    if search.get() == "":
        messagebox.showwarning("Warning", "Enter Roll No")
    else:
        messagebox.showinfo("Search", "Student Found")

        tk.Button(root, text="Search", command=search_student).grid(roww=0, column=2)


for i, fields in enumerate(fields):
    tk.Label(root, text=fields).grid(row=i, column=0, pady=5)
    box = tk.Entry(root)
    box.grid(row=i, column=1)
    boxes.append(box)

def submit():
    if boxes[0].get() == "" or boxes[1].get() == "":
            messagebox.showwarning("Warning","Fill All Fields")
    else:
             messagebox.showinfo("Success","Admission Saved")
tk.Button(root, text="submit", command=submit).grid(
    row=5, column=0, columnspan=2, pady=15
)

root.mainloop()





import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Information Form")
root.geometry("400x450")
root.configure(bg="#ADD8E6")

fields = ["Student Roll No", "Name", "Father Name", "Class", "Phone"]
boxes = []

# Search
tk.Label(root, text="Search Roll No").grid(row=0, column=0, pady=5)
search = tk.Entry(root)
search.grid(row=0, column=1)

def search_student():
    if search.get() == "":
        messagebox.showwarning("Warning", "Enter Roll No")
    else:
        messagebox.showinfo("Search", "Student Found")

tk.Button(root, text="Search", command=search_student).grid(row=0, column=2)

# Form
for i, field in enumerate(fields):
    tk.Label(root, text=field).grid(row=i+1, column=0, pady=5)
    box = tk.Entry(root)
    box.grid(row=i+1, column=1)
    boxes.append(box)

def submit():
    if boxes[0].get() == "" or boxes[1].get() == "":
        messagebox.showwarning("Warning", "Fill Roll No and Name")
    else:
        messagebox.showinfo("Success", "Admission Saved")

def update():
    messagebox.showinfo("Update", "Student Updated")

tk.Button(root, text="Submit", command=submit).grid(row=6, column=0, pady=15)
tk.Button(root, text="Update", command=update).grid(row=6, column=1, pady=15)

root.mainloop()


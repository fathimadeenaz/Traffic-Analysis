from tkinter import *
from tkinter import filedialog
import mypack as mp

root=Tk()

def upload():

    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Deenaz\Pictures\FURNITURE", title="Select A File",filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    mp.foo(root.filename)

def page1(root):
    page = Frame(root)
    page.pack()
    Label(page, text = 'WELCOME', fg='red', font=("Helvetica", 16)).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text = 'VIDEO', fg='blue', command = changepage1).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text = 'IMAGE', fg='blue', command = changepage2).pack(padx=5, pady=10, side="top", fill="both", expand=True)

def page2a(root):
    page = Frame(root)
    page.pack()
    Label(page, text = 'VIDEO', fg='red', font=("Helvetica", 16)).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text = 'PROCEED', fg='blue', command = upload).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text = 'BACK', fg='blue', command = changepage1).pack(padx=5, pady=10, side="top", fill="both", expand=True)

def page2b(root):
    page = Frame(root)
    page.pack()
    Label(page, text = 'IMAGE', fg='red', font=("Helvetica", 16)).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text = 'PROCEED', fg='blue', command = upload).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text = 'BACK', fg='blue', command = changepage2).pack(padx=5, pady=10, side="top", fill="both", expand=True)

def changepage1():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        page2a(root)
        pagenum = 2
    else:
        page1(root)
        pagenum = 1

def changepage2():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        page2b(root)
        pagenum = 2
    else:
        page1(root)
        pagenum = 1

pagenum = 1

page1(root)

root.title('XXX')
root.geometry("400x250+450+200")

root.mainloop()

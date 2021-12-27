from tkinter import *
from tkinter import filedialog
import mypack as mp

root=Tk()

def upload():
    
    global res
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Deenaz\Documents\Python\MiniPro\code\videos", title="Select A File",filetypes=(("mp4 files", "*.mp4"),("all files", "*.*")))
    res = mp.foo(root.filename)
    changepage2()

def page1(root):
    page = Frame(root)
    page.pack()
    Label(page, text = 'WELCOME', fg='red', font=("Helvetica", 16)).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text = 'BEGIN', fg='blue', command = changepage1).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    #Button(page, text = 'IMAGE', fg='blue', command = changepage2).pack(padx=5, pady=10, side="top", fill="both", expand=True)

def page2(root):
    page = Frame(root)
    page.pack()
    Label(page, text = 'VIDEO', fg='red', font=("Helvetica", 16)).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text = 'UPLOAD FILE', fg='blue', command = upload).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    #Button(page, text = 'VIEW RESULT', fg='blue', command = changepage2).pack(padx=5, pady=10, side="top", fill="both", expand=True)

def page3(root):
    page = Frame(root)
    page.pack()
    Label(page, text = 'RESULTS', fg='red').grid(row = 1 , column = 3, columnspan = 2)
    Label(page, text = 'car', fg='red').grid(row = 4 , column = 2)
    Label(page, text = 'motorbike', fg='red').grid(row = 5 , column = 2)
    Label(page, text = 'bus', fg='red').grid(row = 6 , column = 2)
    Label(page, text = 'truck', fg='red').grid(row = 7 , column = 2)
    Label(page, text = 'up', fg='red').grid(row = 3 , column = 4)
    Label(page, text = res[0], fg='red').grid(row = 4 , column = 4)
    Label(page, text = res[1], fg='red').grid(row = 5 , column = 4)
    Label(page, text = res[2], fg='red').grid(row = 6 , column = 4)
    Label(page, text = res[3], fg='red').grid(row = 7 , column = 4)
    Label(page, text = 'down', fg='red').grid(row = 3 , column = 5)
    Label(page, text = res[4], fg='red').grid(row = 4 , column = 5)
    Label(page, text = res[5], fg='red').grid(row = 5 , column = 5)
    Label(page, text = res[6], fg='red').grid(row = 6 , column = 5)
    Label(page, text = res[7], fg='red').grid(row = 7 , column = 5)

    #Button(page, text = 'EXIT', fg='blue', command = root.destroy).pack(padx=5, pady=10, side="top", fill="both", expand=True)
    #Button(page, text = 'BACK', fg='blue', command = changepage2).pack(padx=5, pady=10, side="top", fill="both", expand=True)

def changepage1():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    #if pagenum == 1:
    #    page2(root)
    #    pagenum = 2
    #else:
    #    page1(root)
    #    pagenum = 1
    page2(root)

def changepage2():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
#    if pagenum == 1:
#        page2(root)
#        pagenum = 2
#    else:
#        page1(root)
#        pagenum = 1
    page3(root)

pagenum = 1

page1(root)

root.title('XXX')
root.geometry("400x250+450+200")

root.mainloop()

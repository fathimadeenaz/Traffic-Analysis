from tkinter import *
from tkinter import filedialog
import pandas as pd
import mypack as mp

root = Tk()


def upload():

    global res
    res = [2, 3, 1, 0, 3, 1, 0, 0]
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\noore\OneDrive\Desktop\miniproject",
                                               title="Select A File", filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    res = mp.foo(root.filename)
    changepage2()


def save():
    cols = ['Vehicle_Type']
    rows = ['Cars', 'Motorbikes', 'Buses', 'Trucks']
    d1 = pd.DataFrame(rows, columns=cols)
    d1['Upwards'] = res[0:4]
    d1['Downwards'] = res[4:8]
    d1.to_csv(r"C:\Users\noore\OneDrive\Desktop\miniproject\output.csv")


def showmsg(page):
    Label(page, text='File Saved!', fg='blue', font=("Helvetica", 10)).place(
        x=55, y=145)


def page1(root):
    page = Frame(root)
    page.pack()
    Label(page, text='TRAFFIC ANALYSIS', fg='blue', font=("Helvetica", 24)).pack(
        padx=5, pady=10, side="top", fill="both", expand=True)
    Label(page, text=' ', fg='blue', font=("Helvetica", 10)).pack(
        padx=5, pady=10, side="top", fill="both", expand=True)
    Label(page, text='WELCOME', fg='red', font=("Helvetica", 16)).pack(
        padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text='BEGIN', fg='blue', command=changepage1).pack(
        padx=5, pady=10, side="top", fill="both", expand=True)


def page2(root):
    page = Frame(root)
    page.pack()
    Label(page, text='VIDEO', fg='red', font=("Helvetica", 16)).pack(
        padx=5, pady=10, side="top", fill="both", expand=True)
    Button(page, text='UPLOAD FILE', fg='blue', command=upload).pack(
        padx=5, pady=10, side="top", fill="both", expand=True)


def page3(root):
    page = Frame(root)
    page.pack()
    Label(page, text='RESULTS', fg='red').grid(row=1, column=3, columnspan=2)
    Label(page, text='   ', fg='red', font=("Helvetica", 5)).grid(
        row=2, column=3, columnspan=2)
    Label(page, text='Car', fg='red').grid(row=4, column=2)
    Label(page, text='Motorbike', fg='red').grid(row=5, column=2)
    Label(page, text='Bus', fg='red').grid(row=6, column=2)
    Label(page, text='Truck', fg='red').grid(row=7, column=2)
    Label(page, text='Upwards', fg='red').grid(row=3, column=4)
    Label(page, text=res[0], fg='red').grid(row=4, column=4)
    Label(page, text=res[1], fg='red').grid(row=5, column=4)
    Label(page, text=res[2], fg='red').grid(row=6, column=4)
    Label(page, text=res[3], fg='red').grid(row=7, column=4)
    Label(page, text='Downwards', fg='red').grid(row=3, column=5)
    Label(page, text=res[4], fg='red').grid(row=4, column=5)
    Label(page, text=res[5], fg='red').grid(row=5, column=5)
    Label(page, text=res[6], fg='red').grid(row=6, column=5)
    Label(page, text=res[7], fg='red').grid(row=7, column=5)
    Button(page, text='SAVE', fg='blue', command=lambda: [save(), showmsg(page)]).grid(
        row=14, column=2)


def changepage1():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    page2(root)


def changepage2():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    page3(root)


pagenum = 1

page1(root)

root.title('Traffic Analysis')
root.geometry("400x250+450+200")

root.mainloop()

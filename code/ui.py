from tkinter import *
from tkinter import filedialog
import pandas as pd
import mypack as mp

root = Tk()
root.geometry("850x480")


def upload():

    global res
    res = [2, 3, 1, 0, 3, 1, 0, 0]
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\noore\OneDrive\Desktop\project\MiniPro\code\videos",
                                               title="Select A File", filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    res = mp.foo(root.filename)
    changepage2()


def save():
    cols = ['Vehicle_Type']
    rows = ['Cars', 'Motorbikes', 'Buses', 'Trucks']
    d1 = pd.DataFrame(rows, columns=cols)
    d1['Upwards'] = res[0:4]
    d1['Downwards'] = res[4:8]
    d1.to_csv(r"C:\Users\noore\OneDrive\Desktop\project\output.csv")


def showmsg(page):
    Label(page, text='File Saved!', fg='blue', font=("Helvetica", 15)).place(
        x=55, y=300)


def page1(root):
    bg = PhotoImage(
        file=r"C:\Users\noore\OneDrive\Desktop\project\MiniPro\code\videos\background.png")

    canvas1 = Canvas(root, width=400,
                     height=400)

    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")

    canvas1.create_text(425, 150, text="TRAFFIC ANALYSIS",
                        fill="white", font=('Helvetica 50 bold'))

    button3 = Button(root, text="       Begin       ",
                     fg='blue', font=("Helvetica", 20), command=changepage1)

    button3_canvas = canvas1.create_window(325, 270, anchor="nw",
                                           window=button3)
    root.mainloop()


def page2(root):
    page = Frame(root)
    page.pack()
    Label(page, text='VIDEO', fg='red', font=("Helvetica", 25)).pack(
        padx=5, pady=100, side="top", fill="both", expand=True)
    Button(page, text='UPLOAD FILE', fg='blue', font=("Helvetica", 15), command=upload).pack(
        padx=5, pady=100, side="top", fill="both", expand=True)


def page3(root):
    page = Frame(root)
    page.pack()
    Label(page, text='RESULTS', fg='blue', font=(
        "Helvetica", 25)).grid(row=1, column=3, columnspan=2)
    Label(page, text='   ', fg='red', font=("Helvetica", 5)).grid(
        row=2, column=3, columnspan=2)
    Label(page, text='Car', fg='red', font=(
        "Helvetica", 18)).grid(row=4, column=2)
    Label(page, text='Motorbike', fg='red', font=(
        "Helvetica", 18)).grid(row=5, column=2)
    Label(page, text='Bus', fg='red', font=(
        "Helvetica", 18)).grid(row=6, column=2)
    Label(page, text='Truck', fg='red', font=(
        "Helvetica", 18)).grid(row=7, column=2)
    Label(page, text='Upwards', fg='red', font=(
        "Helvetica", 18)).grid(row=3, column=4)
    Label(page, text=res[0], fg='red', font=(
        "Helvetica", 18)).grid(row=4, column=4)
    Label(page, text=res[1], fg='red', font=(
        "Helvetica", 18)).grid(row=5, column=4)
    Label(page, text=res[2], fg='red', font=(
        "Helvetica", 18)).grid(row=6, column=4)
    Label(page, text=res[3], fg='red', font=(
        "Helvetica", 18)).grid(row=7, column=4)
    Label(page, text='Downwards', fg='red', font=(
        "Helvetica", 18)).grid(row=3, column=5)
    Label(page, text=res[4], fg='red', font=(
        "Helvetica", 18)).grid(row=4, column=5)
    Label(page, text=res[5], fg='red', font=(
        "Helvetica", 18)).grid(row=5, column=5)
    Label(page, text=res[6], fg='red', font=(
        "Helvetica", 18)).grid(row=6, column=5)
    Label(page, text=res[7], fg='red', font=(
        "Helvetica", 18)).grid(row=7, column=5)
    Button(page, text='SAVE', fg='blue', font=("Helvetica", 18), command=lambda: [save(), showmsg(page)]).grid(
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

root.mainloop()

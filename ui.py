# with csv file


from tkinter import *
from tkinter import filedialog
import pandas as pd
import main

from tkinter import messagebox

root = Tk()
root.title('Traffic Analysis')

root.geometry("850x480")

root.resizable(False, False)

root.config(bg="#222b4f")


def upload():

    global res
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Deenaz\Documents\Python\MiniPro\videos",
                                               title="Select A File", filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    res = main.foo(root.filename)
    changepage2()


def save():
    cols = ['Vehicle_Type']
    rows = ['Cars', 'Motorbikes', 'Buses', 'Vans']
    d1 = pd.DataFrame(rows, columns=cols)
    d1['Upwards'] = res[0:4]
    d1['Downwards'] = res[4:8]
    d1.to_csv(r"C:\Users\Deenaz\Documents\Python\MiniPro\output.csv")


# def showmsg(page):
#     Label(page, text='File Saved!', fg='blue', font=("Helvetica", 10)).grid(
#         row=18, column=3, columnspan=2)

# def showmsg(root):
#     bg = PhotoImage(file=r"C:\Users\Deenaz\Downloads\bg.png")
#     canvas1 = Canvas(root, width=400, height=400)
#     canvas1.pack(fill="both", expand=True)
#     canvas1.create_image(0, 0, image=bg, anchor="nw")

#     canvas1.create_text(425, 30, text="File Saved!",
#                         fill="pink", font=("Lato", 18))
#     root.mainloop()

def showmsg():
    messagebox.showinfo("Notification", "File has been successfully saved")


def page1(root):
    bg = PhotoImage(
        file=r"C:\Users\Deenaz\Documents\Python\MiniPro\UI\bg.png")

    canvas1 = Canvas(root, width=400, height=400)

    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg, anchor="nw")

    canvas1.create_text(420, 180, text="TRAFFIC ANALYSIS",
                        fill="#d2d2d7", font=('Helvatica 50 bold'))

    button3 = Button(root, text="       Begin       ", bg="#4467fd",
                     fg="#d2d2d7", font=("Lato", 20), command=changepage1)

    button3_canvas = canvas1.create_window(
        325, 270, anchor="nw", window=button3)
    root.mainloop()


def page2(root):
    bg = PhotoImage(file=r"C:\Users\Deenaz\Documents\Python\MiniPro\UI\bg.png")

    canvas1 = Canvas(root, width=400, height=400)

    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")

    canvas1.create_text(420, 100, text="INPUT VIDEO",
                        fill="#d2d2d7", font=('Helvatica 35'))

    canvas1.create_text(420, 221, text="Select file to be uploaded",
                        fill="#d2d2d7", font=("Lato", 20))

    canvas1.create_text(420, 254, text="File uploaded must be in mp4 format",
                        fill="#d2d2d7", font=("Lato", 20))

    button3 = Button(root, text="       Browse       ", bg="#4467fd",
                     fg="#d2d2d7", font=("Lato", 20), command=upload)

    button3_canvas = canvas1.create_window(
        320, 350, anchor="nw",  window=button3)
    root.mainloop()


# def page3(root):
#     page = Frame(root)
#     page.pack()
#     Label(page, text='RESULTS', fg='blue', font=(
#         "Helvetica", 25)).grid(row=1, column=3, columnspan=2)
#     Label(page, text='   ', fg='red', font=("Helvetica", 5)).grid(
#         row=2, column=3, columnspan=2)
#     Label(page, text='Car', fg='red', font=(
#         "Helvetica", 18)).grid(row=4, column=2)
#     Label(page, text='Motorbike', fg='red', font=(
#         "Helvetica", 18)).grid(row=5, column=2)
#     Label(page, text='Bus', fg='red', font=(
#         "Helvetica", 18)).grid(row=6, column=2)
#     Label(page, text='Van', fg='red', font=(
#         "Helvetica", 18)).grid(row=7, column=2)
#     Label(page, text='Upwards', fg='red', font=(
#         "Helvetica", 18)).grid(row=3, column=4)
#     Label(page, text=res[0], fg='red', font=(
#         "Helvetica", 18)).grid(row=4, column=4)
#     Label(page, text=res[1], fg='red', font=(
#         "Helvetica", 18)).grid(row=5, column=4)
#     Label(page, text=res[2], fg='red', font=(
#         "Helvetica", 18)).grid(row=6, column=4)
#     Label(page, text=res[3], fg='red', font=(
#         "Helvetica", 18)).grid(row=7, column=4)
#     Label(page, text='Downwards', fg='red', font=(
#         "Helvetica", 18)).grid(row=3, column=5)
#     Label(page, text=res[4], fg='red', font=(
#         "Helvetica", 18)).grid(row=4, column=5)
#     Label(page, text=res[5], fg='red', font=(
#         "Helvetica", 18)).grid(row=5, column=5)
#     Label(page, text=res[6], fg='red', font=(
#         "Helvetica", 18)).grid(row=6, column=5)
#     Label(page, text=res[7], fg='red', font=(
#         "Helvetica", 18)).grid(row=7, column=5)
#     # Button(page, text='SAVE', fg='blue', font=("Helvetica", 18), command=lambda: [save(), showmsg(page)]).grid(
#     #     row=14, column=2)
#     Button(page, text='SAVE', fg='blue', command=lambda: [save(), showmsg(page)]).grid(
#         row=17, column=3, columnspan=2)

def page3(root):
    bg = PhotoImage(file=r"C:\Users\Deenaz\Documents\Python\MiniPro\UI\bg.png")

    canvas1 = Canvas(root, width=400,
                     height=400)

    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")

    canvas1.create_text(420, 100, text="RESULTS",
                        fill="#d2d2d7", font=('Helvatica 35'))

    canvas1.create_text(220, 200, text="Car",
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(220, 235, text="Motorbike",
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(220, 270, text="Bus",
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(220, 305, text="Van",
                        fill="#d2d2d7", font=("Lato", 18))

    canvas1.create_text(420, 160, text="Upwards",
                        fill="#d2d2d7", font=("Lato", 18))

    canvas1.create_text(420, 200, text=res[0],
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(420, 235, text=res[1],
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(420, 270, text=res[2],
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(420, 305, text=res[3],
                        fill="#d2d2d7", font=("Lato", 18))

    canvas1.create_text(600, 160, text="Downwards",
                        fill="#d2d2d7", font=("Lato", 18))

    canvas1.create_text(600, 200, text=res[4],
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(600, 235, text=res[5],
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(600, 270, text=res[6],
                        fill="#d2d2d7", font=("Lato", 18))
    canvas1.create_text(600, 305, text=res[7],
                        fill="#d2d2d7", font=("Lato", 18))

    button3 = Button(root, text="       SAVE       ", bg="#4467fd", fg="#d2d2d7", font=(
        "Lato", 20), command=lambda: [save(), showmsg()])

    button3_canvas = canvas1.create_window(
        330, 350, anchor="nw", window=button3)

    root.mainloop()


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

root.mainloop()

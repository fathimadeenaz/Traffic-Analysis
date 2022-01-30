# with csv file


from tkinter import *
from tkinter import filedialog
import pandas as pd
import main

root = Tk()
root.title('Traffic Analysis')

root.geometry("850x480")


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


def showmsg(page):
    Label(page, text='File Saved!', fg='blue', font=("Helvetica", 10)).grid(
        row=18, column=3, columnspan=2)

# def showmsg(page):
#     Label(page, text='File Saved!', fg='blue', font=("Helvetica", 15)).place(
#         x=55, y=300)


# def page1(root):
#     page = Frame(root)
#     page.pack()
#     Label(page, text='TRAFFIC ANALYSIS', fg='blue', font=("Helvetica", 24)).pack(
#         padx=5, pady=10, side="top", fill="both", expand=True)
#     Label(page, text=' ', fg='blue', font=("Helvetica", 10)).pack(
#         padx=5, pady=10, side="top", fill="both", expand=True)
#     Label(page, text='WELCOME', fg='red', font=("Helvetica", 16)).pack(
#         padx=5, pady=10, side="top", fill="both", expand=True)
#     Button(page, text='BEGIN', fg='blue', command=changepage1).pack(
#         padx=5, pady=10, side="top", fill="both", expand=True)


# def page2(root):
#     page = Frame(root)
#     page.pack()
#     Label(page, text='VIDEO', fg='red', font=("Helvetica", 16)).pack(
#         padx=5, pady=10, side="top", fill="both", expand=True)
#     Button(page, text='UPLOAD FILE', fg='blue', command=upload).pack(
#         padx=5, pady=10, side="top", fill="both", expand=True)


# def page3(root):
#     page = Frame(root)
#     page.pack()
#     Label(page, text='RESULTS', fg='blue').grid(row=1, column=3, columnspan=2)
#     Label(page, text='   ', fg='red', font=("Helvetica", 8)).grid(
#         row=2, column=3, columnspan=2)
#     Label(page, text='Car', fg='red').grid(row=4, column=2)
#     Label(page, text='Motorbike', fg='red').grid(row=5, column=2)
#     Label(page, text='Bus', fg='red').grid(row=6, column=2)
#     Label(page, text='Truck', fg='red').grid(row=7, column=2)
#     Label(page, text='Upwards', fg='red').grid(row=3, column=4)
#     Label(page, text=res[0], fg='red').grid(row=4, column=4)
#     Label(page, text=res[1], fg='red').grid(row=5, column=4)
#     Label(page, text=res[2], fg='red').grid(row=6, column=4)
#     Label(page, text=res[3], fg='red').grid(row=7, column=4)
#     Label(page, text='Downwards', fg='red').grid(row=3, column=5)
#     Label(page, text=res[4], fg='red').grid(row=4, column=5)
#     Label(page, text=res[5], fg='red').grid(row=5, column=5)
#     Label(page, text=res[6], fg='red').grid(row=6, column=5)
#     Label(page, text=res[7], fg='red').grid(row=7, column=5)
#     Button(page, text='SAVE', fg='blue', command=lambda: [save(), showmsg(page)]).grid(
#         row=17, column=3, columnspan=2)


def page1(root):
    # bg = PhotoImage(
    #     file=r"C:\Users\Deenaz\Downloads\output-onlinepngtools.png")

    canvas1 = Canvas(root, width=400,
                     height=400)

    canvas1.pack(fill="both", expand=True)

    # canvas1.create_image(0, 0, image=bg,
    #                      anchor="nw")

    canvas1.create_text(425, 150, text="TRAFFIC ANALYSIS",
                        fill="red", font=('Helvetica 50 bold'))

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
    # Button(page, text='SAVE', fg='blue', font=("Helvetica", 18), command=lambda: [save(), showmsg(page)]).grid(
    #     row=14, column=2)
    Button(page, text='SAVE', fg='blue', command=lambda: [save(), showmsg(page)]).grid(
        row=17, column=3, columnspan=2)


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

# root.title('Traffic Analysis')
# root.geometry("400x250+450+200")


root.mainloop()

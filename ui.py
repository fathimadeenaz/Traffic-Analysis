# Import necessary packages

from tkinter import *
from tkinter import filedialog
import pandas as pd
import main
import os

# Initialising window

print()
root = Tk()
print(os.getcwd()+r"\UI\icon.png")
root.title('Traffic Analysis')
root.geometry("850x480")
root.resizable(False, False)
root.config(bg="#222b4f")

photo = PhotoImage(
    file = os.getcwd() + r"\UI\icon.png")

root.iconphoto(False, photo)

# Function to upload input video

def upload():

    global res
    root.filename = filedialog.askopenfilename(initialdir=os.getcwd() + r"\videos",
        title = "Select A File", filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    res = main.foo(root.filename)
    changepage2()

# Function to save results to csv file

def save():
    cols = ['Vehicle_Type']
    rows = ['Cars', 'Motorbikes', 'Buses', 'Vans']
    d1 = pd.DataFrame(rows, columns=cols)
    d1['Upwards'] = res[0:4]
    d1['Downwards'] = res[4:8]
    d1.to_csv(os.getcwd() + r"\output.csv")


def showmsg(canvas1):
    canvas1.create_text(420, 440, text = "File Saved!",
        fill = "#d2d2d7", font=('Helvatica 15'))

# Home page

def page1(root):
    bg = PhotoImage(file = os.getcwd() + r"\UI\bg.png")
    canvas1 = Canvas(root, width = 400, height = 400)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image(0, 0, image = bg, anchor = "nw")

    canvas1.create_text(420, 180, text = "TRAFFIC ANALYSIS",
        fill = "#d2d2d7", font = ('Helvatica 50 bold'))

    button3 = Button(root, text="       BEGIN       ", bg = "#4467fd",
        fg = "#d2d2d7", font = ("Lato", 20), command = changepage1)
    button3_canvas = canvas1.create_window(
        325, 270, anchor = "nw", window = button3)

    root.mainloop()

# Input Video page

def page2(root):

    bg = PhotoImage(file = os.getcwd() + r"\UI\bg.png")
    canvas1 = Canvas(root, width = 400, height = 400)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image(0, 0, image = bg, anchor = "nw")

    canvas1.create_text(420, 100, text = "INPUT VIDEO",
        fill = "#d2d2d7", font = ('Helvatica 35'))

    canvas1.create_text(420, 221, text="Select file to be uploaded",
        fill = "#d2d2d7", font = ("Lato", 20))

    canvas1.create_text(420, 254, text = "File uploaded must be in mp4 format",
        fill = "#d2d2d7", font = ("Lato", 20))

    button3  =  Button(root, text = "       BROWSE       ", bg = "#4467fd",
        fg = "#d2d2d7", font = ("Lato", 20), command = upload)
    button3_canvas  =  canvas1.create_window(
        320, 350, anchor = "nw",  window = button3)

    root.mainloop()

# Results page

def page3(root):

    bg = PhotoImage(file = os.getcwd() + r"\UI\bg.png")
    canvas1 = Canvas(root, width = 400, height = 400)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image(0, 0, image = bg, anchor="nw")

    canvas1.create_text(420, 100, text = "RESULTS",
    fill = "#d2d2d7", font=('Helvatica 35'))

    canvas1.create_text(220, 200, text = "Car",
    fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(220, 235, text = "Motorbike",
    fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(220, 270, text = "Bus",
    fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(220, 305, text = "Van",
    fill = "#d2d2d7", font=("Lato", 18))

    canvas1.create_text(420, 160, text = "Upwards",
        fill = "#d2d2d7", font=("Lato", 18))

    canvas1.create_text(420, 200, text = res[0],
        fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(420, 235, text = res[1],
        fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(420, 270, text = res[2],
        fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(420, 305, text = res[3],
        fill = "#d2d2d7", font=("Lato", 18))

    canvas1.create_text(600, 160, text = "Downwards",
        fill = "#d2d2d7", font=("Lato", 18))

    canvas1.create_text(600, 200, text = res[4],
        fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(600, 235, text = res[5],
        fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(600, 270, text = res[6],
        fill = "#d2d2d7", font = ("Lato", 18))
    canvas1.create_text(600, 305, text = res[7],
        fill = "#d2d2d7", font = ("Lato", 18))

    button3 = Button(root, text = "       SAVE       ", bg = "#4467fd", fg = "#d2d2d7", font = (
        "Lato", 20), command = lambda: [save(), showmsg(canvas1)])
    button3.place(x = 320, y = 350)

    root.mainloop()

# Functions to change pages

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

# Running the app
pagenum = 1
page1(root)
root.mainloop()
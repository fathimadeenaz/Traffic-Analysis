from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

window=Tk()


lbl=Label(window, text="Welcome to Tooly!", fg='red', font=("Helvetica", 16))
lbl.pack(padx=5, pady=10)

def cam():

    return 

def tooly():

    return

def snap():
    cam()
    tooly()
    return

def upload():

    window.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Deenaz\Pictures\FURNITURE", title="Select A File",filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    #print(window.filename)
    #my_label = Label(window, text=window.filename).pack()
    #my_image = ImageTk.PhotoImage(Image.open(window.filename))
    #my_image_label = Label(image=my_image).pack()
    tooly()


btn1=Button(window, text="SNAP", fg='blue', command=snap).pack(padx=5, pady=10)

btn2=Button(window, text="UPLOAD", fg='blue',command=upload).pack(padx=5, pady=10)


window.title('tooly')
window.geometry("300x200+10+10")
window.mainloop()
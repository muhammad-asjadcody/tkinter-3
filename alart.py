from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry

def mesage():
    messagebox.showwarning("ALERTING YOU", "a big Virus has been found!")

button = Button(root, text="Scan for Virus", command=mesage)
button.place(x=40, y=80)

root.mainloop()
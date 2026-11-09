from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_key_pressing(event):
    """Print the character associated to the key pressed"""
    print(event.char)

window.bind("<Key>", handle_key_pressing)

def handle_clicking(event):
    print("\nThe Button was clicked!")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_clicking)

window.mainloop()
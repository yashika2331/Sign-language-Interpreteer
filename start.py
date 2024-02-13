from tkinter import *
import tkinter as tk

from PIL import Image, ImageTk


def next_page():
    root.destroy()
    import video


def prev_page():
    root.destroy()
    import voice


root = Tk()
root.geometry("300x300")
root.title("Interpreter")
root.state('zoomed')


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


image = Image.open('SIGN LANGUAGE INTERPRETER.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)
Display = Button(root, height=2,
                 width=20,
                 text="Sign-Text",
                 command=lambda: next_page()).place(relx=0.37, rely=0.72, anchor=W)

Display1 = Button(root, height=2,
                  width=20,
                  text="Voice/Text-Sign",
                  command=lambda: prev_page()).place(relx=0.37, rely=0.4, anchor=W)

mainloop()

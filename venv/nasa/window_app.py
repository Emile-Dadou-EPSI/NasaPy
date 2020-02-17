from tkinter import *
import APOD
from PIL import ImageTk, Image
import os

# Initialization of the frame
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)


# Close window
def close_window():
    os.remove("test.png")
    root.destroy()


# function to display image in the frame
def displayImages(self, path):
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    label = Label(self, image = render, bg = "black")
    label.image = render
    label.pack()



root = Tk()

app = Window(root)
root.wm_title("Tkinter window")
root.geometry("800x600")

button = Button(root,text = "Display image", command= lambda : displayImages(root, "test.png") )
button2 = Button(root,text = "Exit", command=close_window )
button.pack()
button2.pack()

root.mainloop()
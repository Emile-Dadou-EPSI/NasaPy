from tkinter import *
from tkinter import messagebox
import APOD
from PIL import ImageTk, Image
import os

list_path = ['']

# Initialization of the frame
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)


# Close window
def close_window(self, path_list):
    for x in path_list:
        if (x != "" and x != None):
            os.remove(x)

    root.destroy()


# function to display image in the frame
def displayImages(self, path):
    if (path == ""):
        messagebox.showinfo("The image " + path + " doesn't exist", "error")
        return
    else:
        load = Image.open(path)
        render = ImageTk.PhotoImage(load)
        label = Label(self, image = render, bg = "black")
        label.image = render
        label.pack()



root = Tk()

app = Window(root)
root.wm_title("NasaPy")
root.geometry("800x600")

path_img_1 = ""
path_img_2 = ""

# Verification that the images exists
if (os.path.exists("test.png")):
    # Open image and process it
    image = Image.open("test.png")
    processed_image = image.resize((500, 500))
    processed_image.save("test.png")
    path_img_1 = "test.png"

if (os.path.exists("test2.png")):
    image2 = Image.open("test2.png")

    processed_image2 = image2.resize((500, 500))
    processed_image2.save("test2.png")
    path_img_2 = "test2.png"

if (path_img_1 != "" and path_img_1 != None):
    list_path.append(path_img_1)

if (path_img_2 != "" and path_img_2 != None):
    list_path.append(path_img_2)

button = Button(root,text = "Display image", command= lambda : displayImages(root, path_img_1) )
button1 = Button(root, text= "Mars Image", command = lambda : displayImages(root, path_img_2))
button2 = Button(root,text = "Exit", command= lambda : close_window(root, list_path) )

button.pack()
button1.pack()
button2.pack()

root.mainloop()
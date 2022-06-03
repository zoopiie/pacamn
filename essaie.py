from tkinter import *
from PIL import ImageTk, Image, ImageOps
from threading import Timer
import keyboard
from random import *
from time import sleep


def pool():
    image = Image.open("ninja.png")
    resize_image = image.resize((40, 40))
    im_mirror = ImageOps.mirror(resize_image)
    images = im_mirror.rotate(90)

    resize_image.save("ninja.png")

def open(image):
    print('hrello')


    canvas.create_image ( 30 , 10 , image = image , anchor = "nw" )





root = Tk()
root.geometry('800x800')
root.title('dklhnjaq')
root.wm_attributes('-transparentcolor', 'grey')



canvas = Canvas(root, width=200, height=200, bg='grey')
canvas.pack(pady=20, padx=20)

img = PhotoImage(file='pacman.png')

canvas.create_image(20,20 , image=img)
pool()


root.mainloop()
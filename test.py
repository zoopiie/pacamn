from tkinter import *
from PIL import Image, ImageOps, ImageTk

root = Tk()
root.geometry('800x800')
root.title('dklhnjaq')
root.wm_attributes('-transparentcolor', 'grey')

image = Image.open("pacman.png")
resize_image = image.resize((200, 200))
images = resize_image.rotate(90)
im_mirror = ImageOps.mirror(resize_image)
im_flip = ImageOps.flip(resize_image)
imgs = ImageTk.PhotoImage(images)
img = ImageTk.PhotoImage(resize_image)
imgm = ImageTk.PhotoImage(im_mirror)
imgf = ImageTk.PhotoImage(im_flip)


label1 = Label(image=img, bg='grey')
label1.image = img
label1.place(x=0, y=0)

label2 = Label(image=imgs, bg='grey')
label2.image = imgs
label2.place(x=400, y=0)

label3 = Label(image=imgm, bg='grey')
label3.image = imgm
label3.place(x=0, y=400)

label4 = Label(image=imgf, bg='grey')
label4.image = imgf
label4.place(x=400, y=400)

root.mainloop()


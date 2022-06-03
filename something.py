from tkinter import *

x = 0
def create():
    global x
    x += 8
    canvas.create_rectangle(
        30, 20, 200 - x, 100 - 8,
        fill="red",
        tags="rect")

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x400')
ws.config(bg='grey')

canvas = Canvas(
    ws,
    height=300,
    width=400,
    bg="#fff",
)

canvas.pack()

canvas.create_rectangle(
    30, 20, 200, 100,
    fill="red",
    tags="rect")

btn4 = Button(
    ws,
    text='del_image',
    font="Times 12",
    command=create
)
btn4.pack()



btn5 = Button(
    ws,
    text='del_image',
    font="Times 12",
    command=lambda: canvas.delete("rect")
)

btn5.pack(side=LEFT, fill=X, expand=True)

ws.mainloop()
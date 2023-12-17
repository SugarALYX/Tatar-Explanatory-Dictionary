# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

ASSETS_PATH = r"assets/frame0"

window = Tk()
window.title("Татарский толковый словарь")
window.geometry("1280x720")
window.configure(bg="#504D4D")

canvas = Canvas(
    window,
    bg="#504D4D",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=f"{ASSETS_PATH}/image_1.png")
image_1 = canvas.create_image(
    665.0,
    59.0,
    image=image_image_1
)

canvas.create_text(
    295.0,
    29.0,
    anchor="nw",
    text="  Татарский толковый словарь",
    fill="#010101",
    font=("Inter SemiBold", 50 * -1)
)

button_image_1 = PhotoImage(
    file=f"{ASSETS_PATH}/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=46.0,
    y=185.0,
    width=524.0,
    height=105.0
)

button_image_2 = PhotoImage(
    file=f"{ASSETS_PATH}/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=46.0,
    y=541.0,
    width=524.0,
    height=105.0
)

button_image_3 = PhotoImage(
    file=f"{ASSETS_PATH}/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=46.0,
    y=355.0,
    width=524.0,
    height=105.0
)

image_image_2 = PhotoImage(
    file=f"{ASSETS_PATH}/image_2.png")
image_2 = canvas.create_image(
    939.0,
    415.0,
    image=image_image_2
)

canvas.create_text(
    655.0,
    576.0,
    anchor="nw",
    text="""Приложение сделал ученик 10 класса
МБОУ “Нурминская СОШ”,Шайхутдинов Абу Бакр Ильгамович""",
    fill="#171717",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    655.0,
    267.0,
    anchor="nw",
    text="Простой режим: вы вводите слово, программа \nнаходит этому слову определение\n\nСлучайный режим: вы "
         "нажимаете на кнопку и\nполучаете случайное слово с определением\n\nИгра: вам даётся случайное слово и "
         "случайное\nопределение, вы должны ответить правильно\nли подобрано определение",
    fill="#0B0B0B",
    font=("Inter SemiBold", 20 * -1)
)

image_image_3 = PhotoImage(
    file=f"{ASSETS_PATH}/image_3.png")
image_3 = canvas.create_image(
    145.0,
    80.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=f"{ASSETS_PATH}/image_4.png")
image_4 = canvas.create_image(
    1176.0,
    86.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()

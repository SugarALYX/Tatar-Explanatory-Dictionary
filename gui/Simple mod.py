import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from gui.assets.WordFind import Explain


def Find():
    entry_1.delete(1.0, tkinter.END)
    entry_1.insert(1.0, Explain(entry_2.get(), r"Words/"))


ASSETS_PATH = r"assets/frame1"

window = Tk()

window.geometry("1280x720")
window.configure(bg="#514D4D")
window.title("Татарский толковый словарь")

canvas = Canvas(
    window,
    bg="#514D4D",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(
    file=f"{ASSETS_PATH}/entry_1.png")
entry_bg_1 = canvas.create_image(
    642.0,
    457.5,
    image=entry_image_1
)
entry_1 = Text(
    font=("Inter SemiBold", 25 * -1),
    bd=0,
    bg="#6EB755",
    fg="#000716",
    highlightthickness=0,
    wrap="word"
)
entry_1.place(
    x=46.0,
    y=222.0,
    width=1192.0,
    height=469.0
)

canvas.create_rectangle(
    26.0,
    37.0,
    667.0,
    189.0,
    fill="#6EB755",
    outline="")

entry_image_2 = PhotoImage(
    file=f"{ASSETS_PATH}/entry_2.png")
entry_bg_2 = canvas.create_image(
    346.0,
    113.5,
    image=entry_image_2
)
entry_2 = Entry(
    font=("Inter SemiBold", 50 * -1),
    bd=0,
    bg="#6EB755",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=44.0,
    y=45.0,
    width=604.0,
    height=135.0
)

button_image_1 = PhotoImage(
    file=f"{ASSETS_PATH}/button_1.png")

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Find,
    relief="flat"
)
button_1.place(
    x=706.0,
    y=37.0,
    width=551.6851196289062,
    height=152.0
)

window.resizable(False, False)
window.mainloop()

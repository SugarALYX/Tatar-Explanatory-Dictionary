from tkinter import Canvas, Text, Button, PhotoImage, END, Tk, messagebox
from gui.Interface.WordFind import random_word_with_explain


class RandomModMenu:
    def __init__(self):
        ASSETS_PATH = r"Interface/assets/frame1"
        self.RandomModWindow = Tk()
        self.RandomModWindow.geometry("1280x720")
        self.RandomModWindow.configure(bg="#514D4D")
        self.RandomModWindow.title("Режим Случайности")
        self.RandomModWindow.resizable(False, False)

        self.canv = Canvas(
            self.RandomModWindow,
            bg="#514D4D",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canv.place(x=0, y=0)
        self.entry_image_1 = PhotoImage(
            file=f"{ASSETS_PATH}/entry_1.png")
        self.entry_bg_1 = self.canv.create_image(
            642.0,
            457.5,
            image=self.entry_image_1
        )
        self.Explaining = Text(
            self.RandomModWindow,
            font=("Inter SemiBold", 35 * -1),
            bd=0,
            bg="#6EB755",
            fg="#000716",
            highlightthickness=0,
            wrap="word",
        )

        self.Explaining.place(
            x=46.0,
            y=222.0,
            width=1192.0,
            height=469.0
        )

        (
            self.canv.create_rectangle(
                26.0,
                37.0,
                667.0,
                189.0,
                fill="#6EB755",
                outline="")
        )

        self.canv.create_text(
            339.0,
            113.0,
            font=("Inter SemiBold", 50 * -1),
            text="Случайное слово",
        )

        self.button_image_1 = PhotoImage(
            file=f"{ASSETS_PATH}/button_1.png")

        def Random():
            """
            Функция нахождения случайного слова с определение(которое принадлежит этому слову)
            """
            self.Explaining.delete(1.0, END)
            self.Explaining.insert(1.0, random_word_with_explain(r"Interface/Words/"))

        self.FindButton = Button(
            self.RandomModWindow,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=Random,
            relief="flat"
        )
        self.FindButton.place(
            x=706.0,
            y=37.0,
            width=551.6851196289062,
            height=152.0
        )

        self.RandomModWindow.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
            self.RandomModWindow.destroy()

    def run(self):
        self.RandomModWindow.mainloop()

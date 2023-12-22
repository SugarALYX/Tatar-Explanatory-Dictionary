from tkinter import Canvas, Entry, Text, Button, PhotoImage, END, messagebox, Tk
from gui.Interface.WordFind import Explain


class SimpleModMenu:
    def __init__(self):
        ASSETS_PATH = r"Interface/assets/frame1"
        self.SimpleModWindow = Tk()
        self.SimpleModWindow.geometry("1280x720")
        self.SimpleModWindow.configure(bg="#514D4D")
        self.SimpleModWindow.title("Простой режим")
        self.SimpleModWindow.resizable(False, False)

        self.canv = Canvas(
            self.SimpleModWindow,
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
            self.SimpleModWindow,
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

        self.canv.create_rectangle(
            26.0,
            37.0,
            667.0,
            189.0,
            fill="#6EB755",
            outline="")

        self.entry_image_2 = PhotoImage(
            file=f"{ASSETS_PATH}/entry_2.png", )
        self.entry_bg_2 = self.canv.create_image(
            346.0,
            113.5,
            image=self.entry_image_2
        )
        self.YourWord = Entry(
            self.SimpleModWindow,
            font=("Inter SemiBold", 50 * -1),
            justify="center",
            bd=0,
            bg="#6EB755",
            fg="#000716",
            highlightthickness=0
        )
        self.YourWord.place(
            x=44.0,
            y=45.0,
            width=604.0,
            height=135.0
        )

        def Find():
            """
            Функция нахождение слова
            """
            self.Explaining.delete(1.0, END)
            self.Explaining.insert(1.0, Explain(self.YourWord.get(), r"Interface/Words/"))

        self.button_image_1 = PhotoImage(
            file=f"{ASSETS_PATH}/button_1.png")
        self.FindButton = Button(
            self.SimpleModWindow,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=Find,
            relief="flat"
        )
        self.FindButton.place(
            x=690.0,
            y=37.0,
            width=551.6851196289062,
            height=152.0
        )

        self.SimpleModWindow.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
            self.SimpleModWindow.destroy()

    def run(self):
        self.SimpleModWindow.mainloop()
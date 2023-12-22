from tkinter import Canvas, Text, Button, PhotoImage, Tk, messagebox, END
import random
from gui.Interface.WordFind import random_word_with_explain, random_word_random_explain, Explain


class GameModMenu:
    def __init__(self):
        ASSETS_PATH = r"Interface/assets/frame2"
        self.GameModWindow = Tk()
        self.GameModWindow.geometry("1280x720")
        self.GameModWindow.configure(bg="#514D4D")
        self.GameModWindow.title("Игровой режим")
        self.GameModWindow.resizable(False, False)

        self.canvas = Canvas(
            self.GameModWindow,
            bg="#514D4D",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        def WordInText() -> str:
            """
            Функция для выделение слова из поля для вопроса
            :return: слово
            """
            ReturnText = ""
            index = 0
            text = self.Text_For_Description.get(1.0, END)
            while text[index] != "-":
                ReturnText += text[index]
                index += 1
            while ReturnText[len(ReturnText)-1] == " ":
                ReturnText = ReturnText[:-1]
            return ReturnText

        def game():
            """
            Функция игры(выводит в поле вопроса слово и определение)
            """
            if random.randint(1, 2) == 1:
                self.Text_For_Description.delete(1.0, END)
                self.Text_For_Description.insert(1.0, random_word_with_explain(r"Interface/Words/"))
                self.T = 1
            else:
                self.Text_For_Description.delete(1.0, END)
                self.Text_For_Description.insert(1.0, random_word_random_explain(r"Interface/Words/"))
                self.T = 0

        def checkT():
            """
            Проверка ответа
            """
            if self.T == 1:
                self.Explaining.delete(1.0, END)
                self.Explaining.insert(1.0, f"Правильный ответ!\n{Explain(WordInText(), "Interface/Words/")}")
                game()
            else:
                self.Explaining.delete(1.0, END)
                self.Explaining.delete(1.0, END)
                self.Explaining.insert(1.0, f"Неправильный ответ!\n{Explain(WordInText(), "Interface/Words/")}")
                game()

        def checkF():
            """
            проверка ответа
            """
            if self.T == 0:
                self.Explaining.delete(1.0, END)
                self.Explaining.insert(1.0, f"Правильный ответ!\n{Explain(WordInText(), "Interface/Words/")}")
                game()

            else:
                self.Explaining.delete(1.0, END)
                self.Explaining.delete(1.0, END)
                self.Explaining.insert(1.0, f"Неправильный ответ!\n{Explain(WordInText(), "Interface/Words/")}")
                game()

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(
            file=f"{ASSETS_PATH}/button_1.png")
        self.F_Button = Button(
            self.GameModWindow,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=checkF,
            relief="flat"
        )

        self.F_Button.place(
            x=19.0,
            y=533.0,
            width=350.0,
            height=82.0
        )

        self.button_image_2 = PhotoImage(
            file=f"{ASSETS_PATH}/button_2.png")
        self.T_Button = Button(
            self.GameModWindow,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=checkT,
            relief="flat"
        )

        self.T_Button.place(
            x=911.0,
            y=533.0,
            width=350.0,
            height=82.0
        )
        self.entry_image_2 = PhotoImage(
            file=f"{ASSETS_PATH}/entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            645,
            215,
            image=self.entry_image_2
        )

        self.Text_For_Description = Text(
            self.GameModWindow,
            font=("Inter SemiBold", 25 * -1),
            bd=0,
            bg="#6EB755",
            fg="#000716",
            highlightthickness=0,
            wrap="word"
        )

        self.Text_For_Description.place(
            x=39.0,
            y=8.0,
            width=1202.0,
            height=416.0
        )

        self.entry_image_3 = PhotoImage(
            file=f"{ASSETS_PATH}/entry_3.png")
        self.entry_bg_3 = self.canvas.create_image(
            640.5,
            580.0,
            image=self.entry_image_3
        )

        self.Explaining = Text(
            self.GameModWindow,
            font=("Inter SemiBold", 20 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            wrap="word"
        )

        self.Explaining.place(
            x=465.0,
            y=460.0,
            width=351.0,
            height=238.0
        )

        self.GameModWindow.protocol("WM_DELETE_WINDOW", self.on_closing)

        if random.randint(1, 2) == 1:
            self.Text_For_Description.delete(1.0, END)
            self.Text_For_Description.insert(1.0, random_word_with_explain(r"Interface/Words/"))
            self.T = 1
        else:
            self.Text_For_Description.delete(1.0, END)
            self.Text_For_Description.insert(1.0, random_word_random_explain(r"Interface/Words/"))
            self.T = 0

    def run(self):
        self.GameModWindow.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
            self.GameModWindow.destroy()

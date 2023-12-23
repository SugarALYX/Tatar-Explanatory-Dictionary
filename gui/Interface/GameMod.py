import customtkinter as ctk
import random
from gui.Interface.WordFind import random_word_with_explain, random_word_random_explain, Explain


class GameModMenu:
    def __init__(self, parent):
        self.GameModWindow = ctk.CTkToplevel(parent)
        self.GameModWindow.geometry("1920x1080")
        self.GameModWindow.configure(bg="#504D4D")
        self.GameModWindow.title("Игровой режим")
        self.GameModWindow.resizable(True, True)
        self.GameModWindow.attributes("-fullscreen", True)

        def leave():
            self.GameModWindow.destroy()

        def WordInText() -> str:
            """
            Функция для выделение слова из поля для вопроса
            :return: слово
            """
            ReturnText = ""
            index = 0
            text = self.Text_For_Description.get(1.0, ctk.END)
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
                self.Text_For_Description.delete(1.0, ctk.END)
                self.Text_For_Description.insert(1.0, random_word_with_explain(r"Interface/Words/"))
                self.T = 1
            else:
                self.Text_For_Description.delete(1.0, ctk.END)
                self.Text_For_Description.insert(1.0, random_word_random_explain(r"Interface/Words/"))
                self.T = 0

        def checkT():
            """
            Проверка ответа
            """
            if self.T == 1:
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.insert(1.0, f"Правильный ответ!\n{Explain(WordInText(), "Interface/Words/")}")
                game()
            else:
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.insert(1.0, f"Неправильный ответ!\n{Explain(WordInText(), "Interface/Words/")}")
                game()

        def checkF():
            """
            проверка ответа
            """
            if self.T == 0:
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.insert(1.0, f"Правильный ответ!\n{Explain(WordInText(), "Interface/Words/")}")
                game()

            else:
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.insert(1.0, f"Неправильный ответ!\n{Explain(WordInText(), "Interface/Words/")}")
                game()

        self.TButton = ctk.CTkButton(
            self.GameModWindow,
            fg_color="green",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 40 * -1),
            text="Истина",
            text_color="black",
            command=checkT,
            width=316,
            height=120
        )
        self.TButton.place(
            x=417.0,
            y=697.0
        )
        self.FButton = ctk.CTkButton(
            self.GameModWindow,
            fg_color="#CC3343",
            hover_color="#E71321",
            corner_radius=16,
            font=("Century Gothic", 40 * -1),
            text="Ложь",
            text_color="black",
            command=checkF,
            width=316,
            height=120
        )
        self.FButton.place(
            x=58.0,
            y=697.0
        )

        self.Explaining = ctk.CTkTextbox(
            self.GameModWindow,
            width=675,
            height=567,
            corner_radius=16,
            fg_color="#42C24B",
            text_color="black",
            font=("Inter SemiBold", 30 * -1),
            wrap="word"
        )
        self.Explaining.place(
            x=58,
            y=33
        )

        self.Text_For_Description = ctk.CTkTextbox(
            self.GameModWindow,
            width=1049,
            height=1000,
            corner_radius=16,
            fg_color="#42C24B",
            text_color="black",
            font=("Inter SemiBold", 30 * -1),
            wrap="word"
        )
        self.Text_For_Description.place(
            x=824.0,
            y=33
        )

        self.LeaveButton = ctk.CTkButton(
            self.GameModWindow,
            fg_color="#42C24B",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 40 * -1),
            text="Выход",
            text_color="black",
            command=leave,
            width=675,
            height=91
        )
        self.LeaveButton.place(
            x=58,
            y=914
        )

        if random.randint(1, 2) == 1:
            self.Text_For_Description.delete(1.0, ctk.END)
            self.Text_For_Description.insert(1.0, random_word_with_explain(r"Interface/Words/"))
            self.T = 1
        else:
            self.Text_For_Description.delete(1.0, ctk.END)
            self.Text_For_Description.insert(1.0, random_word_random_explain(r"Interface/Words/"))
            self.T = 0

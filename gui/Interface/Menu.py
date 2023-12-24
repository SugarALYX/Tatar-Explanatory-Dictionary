import customtkinter as ctk
import random
from gui.Interface.WordFind import random_word_with_explain, Explain, random_word_random_explain


class MenuOfDictionary:
    def __init__(self):
        self.Menu = ctk.CTk()
        self.Menu.title("Татарский толковый словарь")
        self.Menu.geometry("1920x1080")
        self.Menu.configure(bg="#504D4D")
        self.Menu.resizable(True, True)
        self.Menu.attributes("-fullscreen", True)

        def CreatSimpleModWindow():
            SimpleModMenu(self.Menu)
            self.Menu.withdraw()

        def CreatRandomModWindow():
            RandomModMenu(self.Menu)
            self.Menu.withdraw()

        def CreatGameModWindow():
            GameModMenu(self.Menu)
            self.Menu.withdraw()

        def leave():
            self.Menu.destroy()

        self.MenuSimpleModButton = ctk.CTkButton(
            self.Menu,
            fg_color="#42C24B",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text="Обычный режим",
            text_color="black",
            command=CreatSimpleModWindow,
            width=756,
            height=173,
        )
        self.MenuSimpleModButton.place(
            x=43.0,
            y=226.0
        )

        self.RandomModButton = ctk.CTkButton(
            self.Menu,
            fg_color="#42C24B",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text="\"Случайный\" режим",
            text_color="black",
            command=CreatRandomModWindow,
            width=756,
            height=173,
        )

        self.RandomModButton.place(
            x=43.0,
            y=439.0,
        )

        self.GameModButton = ctk.CTkButton(
            self.Menu,
            fg_color="#42C24B",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text="Игровой режим",
            text_color="black",
            command=CreatGameModWindow,
            width=756,
            height=173
        )
        self.GameModButton.place(
            x=43.0,
            y=652.0,
        )

        self.LeaveButton = ctk.CTkButton(
            self.Menu,
            fg_color="#42C24B",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text="Выход",
            text_color="black",
            command=leave,
            width=756,
            height=173
        )
        self.LeaveButton.place(
            x=43.0,
            y=865.0,
        )

        self.TheTitle = ctk.CTkLabel(
            self.Menu,
            fg_color="#42C24B",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text="Татарский толковый словарь",
            text_color="black",
            width=1298,
            height=138
        )
        self.TheTitle.place(
            x=331.0,
            y=48.0
        )

        self.TheDescription = ctk.CTkLabel(
            self.Menu,
            fg_color="#42C24B",
            corner_radius=16,
            font=("Century Gothic", 40 * -1),
            justify="left",
            text='Простой режим: вы вводите слово, программа \nнаходит этому слову определение\n\nСлучайный режим: вы '
                 'нажимаете на кнопку и\nполучаете случайное слово с определением\n\nИгровой режим: вам даётся '
                 'случайное\n слово и '
                 'случайное определение, вы должны\n ответить, правильно ли подобрано определение\n\n'
                 'Автор: Шайхутдинов Абу Бакр Ильгамович,\nученик 10 класса МБОУ "Нурминская СОШ"',
            text_color="black",
            width=1049,
            height=812

        )
        self.TheDescription.place(
            x=824.0,
            y=226.0
        )

    def run(self):
        self.Menu.mainloop()

    def dei(self):
        self.Menu.deiconify()


class RandomModMenu:
    def __init__(self, parent):
        self.RandomModWindow = ctk.CTkToplevel(parent)
        self.RandomModWindow.geometry("1920x1080")
        self.RandomModWindow.configure(bg="#504D4D")
        self.RandomModWindow.title("Режим случайного слова")
        self.RandomModWindow.resizable(True, True)
        self.RandomModWindow.attributes("-fullscreen", True)

        def Random():
            """
            Функция нахождения случайного слова с определение(которое принадлежит этому слову)
            """
            self.Explaining.delete(1.0, ctk.END)
            self.Explaining.insert(1.0, random_word_with_explain(r"Interface/Words/"))

        def leave():
            menu = MenuOfDictionary()
            menu.dei()
            self.RandomModWindow.destroy()

        self.WordEntry = ctk.CTkLabel(
            self.RandomModWindow,
            width=675,
            height=109,
            corner_radius=16,
            justify="center",
            fg_color="white",
            text_color="black",
            font=("Century Gothic", 30 * -1),
            text="Случайное слово"
        )
        self.WordEntry.place(
            x=69.0,
            y=33.0
        )

        self.FindButton = ctk.CTkButton(
            self.RandomModWindow,
            width=402,
            height=74,
            corner_radius=20,
            fg_color="#42C24B",
            hover_color="#0AE617",
            font=("Century Gothic", 35 * -1),
            text="Найти",
            text_color="black",
            command=Random
        )
        self.FindButton.place(
            x=205.0,
            y=178.0
        )

        self.Explaining = ctk.CTkTextbox(
            self.RandomModWindow,
            width=1049,
            height=1000,
            corner_radius=16,
            fg_color="#42C24B",
            text_color="black",
            font=("Inter SemiBold", 30 * -1),
            wrap="word"
        )
        self.Explaining.place(
            x=824.0,
            y=33
        )

        self.LeaveButton = ctk.CTkButton(
            self.RandomModWindow,
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
            x=69,
            y=920
        )


class SimpleModMenu:
    def __init__(self, parent):
        self.SimpleModWindow = ctk.CTkToplevel(parent)
        self.SimpleModWindow.geometry("1920x1080")
        self.SimpleModWindow.configure(bg="#504D4D")
        self.SimpleModWindow.title("Простой режим")
        self.SimpleModWindow.resizable(True, True)
        self.SimpleModWindow.attributes("-fullscreen", True)

        def Find():
            """
            Функция нахождение слова
            """
            pass
            self.Explaining.delete(1.0, ctk.END)
            self.Explaining.insert(1.0, Explain(self.WordEntry.get(), r"Interface/Words/"))

        def leave():
            menu = MenuOfDictionary()
            menu.dei()
            self.SimpleModWindow.destroy()

        self.WordEntry = ctk.CTkEntry(
            self.SimpleModWindow,
            width=675,
            height=109,
            corner_radius=16,
            justify="center",
            fg_color="white",
            text_color="black",
            font=("Century Gothic", 30 * -1)
        )
        self.WordEntry.place(
            x=69.0,
            y=33.0
        )

        self.FindButton = ctk.CTkButton(
            self.SimpleModWindow,
            width=402,
            height=74,
            corner_radius=20,
            fg_color="#42C24B",
            hover_color="#0AE617",
            font=("Century Gothic", 35 * -1),
            text="Найти",
            text_color="black",
            command=Find
        )
        self.FindButton.place(
            x=205.0,
            y=178.0
        )

        self.Explaining = ctk.CTkTextbox(
            self.SimpleModWindow,
            width=1049,
            height=1000,
            corner_radius=16,
            fg_color="#42C24B",
            text_color="black",
            font=("Inter SemiBold", 30 * -1),
            wrap="word"
        )
        self.Explaining.place(
            x=824.0,
            y=33
        )

        self.LeaveButton = ctk.CTkButton(
            self.SimpleModWindow,
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
            x=69,
            y=920
        )


class GameModMenu:
    def __init__(self, parent):
        self.GameModWindow = ctk.CTkToplevel(parent)
        self.GameModWindow.geometry("1920x1080")
        self.GameModWindow.configure(bg="#504D4D")
        self.GameModWindow.title("Игровой режим")
        self.GameModWindow.resizable(True, True)
        self.GameModWindow.attributes("-fullscreen", True)

        def leave():
            menu = MenuOfDictionary()
            menu.dei()
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
            while ReturnText[len(ReturnText) - 1] == " ":
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

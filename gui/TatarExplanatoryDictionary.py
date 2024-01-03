import customtkinter as ctk
import random
from gui.Assets.WordFind import random_word_with_explain, Explain, random_word_random_explain, WordAdd, WordDelete


class MenuOfDictionary:
    def __init__(self):
        self.Menu = ctk.CTk()
        self.Menu.title("Татарский толковый словарь")
        self.Menu.geometry("1920x1080")
        self.Menu.configure(bg="#504D4D")
        self.Menu.resizable(True, True)
        self.Menu.attributes("-fullscreen", True)

        def CreatAdditionWindow():
            Addition(self.Menu)
            self.Menu.withdraw()

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
            self.Menu.quit()

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
            y=28.0
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
            y=236.0,
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
            y=444.0,
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
            y=860.0,
        )

        self.AdditionButton = ctk.CTkButton(
            self.Menu,
            fg_color="#42C24B",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text="Дополнительно",
            text_color="black",
            command=CreatAdditionWindow,
            width=756,
            height=173
        )
        self.AdditionButton.place(
            x=43.0,
            y=652.0
        )

        self.TheTitle = ctk.CTkLabel(
            self.Menu,
            fg_color="#42C24B",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text="Татарский толковый словарь",
            text_color="black",
            width=1049,
            height=173
        )
        self.TheTitle.place(
            x=824.0,
            y=28.0
        )

        self.TheDescription = ctk.CTkLabel(
            self.Menu,
            fg_color="#42C24B",
            corner_radius=16,
            font=("Century Gothic", 40 * -1),
            justify="left",
            text='Обычный режим: вы вводите слово, программа \nнаходит этому слову определение\n\nСлучайный режим: вы '
                 'нажимаете на кнопку и\nполучаете случайное слово с определением\n\nИгровой режим: вам даётся '
                 'случайное\nслово и '
                 'случайное определение, вы должны\nответить, правильно ли подобрано определение\n\n'
                 'Автор: Шайхутдинов Абу Бакр Ильгамович,\nученик 10 класса МБОУ "Нурминская СОШ"',
            text_color="black",
            width=1049,
            height=797
        )
        self.TheDescription.place(
            x=824.0,
            y=236.0
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
            self.Explaining.insert(1.0, random_word_with_explain(r"Assets/Words/"))

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
            y=942
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
            self.Explaining.insert(1.0, Explain(self.WordEntry.get(), r"Assets/Words/"))

        def Word1():
            self.WordEntry.insert(len(self.WordEntry.get()), "ә")

        def Word2():
            self.WordEntry.insert(len(self.WordEntry.get()), "җ")

        def Word3():
            self.WordEntry.insert(len(self.WordEntry.get()), "ң")

        def Word4():
            self.WordEntry.insert(len(self.WordEntry.get()), "ө")

        def Word5():
            self.WordEntry.insert(len(self.WordEntry.get()), "ү")

        def Word6():
            self.WordEntry.insert(len(self.WordEntry.get()), "һ")

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
            font=("Inter SemiBold", 30 * -1),
            placeholder_text="Введите слово"
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
            y=303.0
        )

        self.W1Button = ctk.CTkButton(
            self.SimpleModWindow,
            width=78,
            height=75,
            corner_radius=20,
            fg_color="#42C24B",
            hover_color="#0AE617",
            font=("Century Gothic", 35 * -1),
            text="ә",
            text_color="black",
            command=Word1
        )
        self.W1Button.place(
            x=69.0,
            y=185.0
        )

        self.W2Button = ctk.CTkButton(
            self.SimpleModWindow,
            width=78,
            height=75,
            corner_radius=20,
            fg_color="#42C24B",
            hover_color="#0AE617",
            font=("Century Gothic", 35 * -1),
            text="җ",
            text_color="black",
            command=Word2
        )
        self.W2Button.place(
            x=187.0,
            y=185.0
        )

        self.W3Button = ctk.CTkButton(
            self.SimpleModWindow,
            width=78,
            height=75,
            corner_radius=20,
            fg_color="#42C24B",
            hover_color="#0AE617",
            font=("Century Gothic", 35 * -1),
            text="ң",
            text_color="black",
            command=Word3
        )
        self.W3Button.place(
            x=306.0,
            y=185.0
        )

        self.W4Button = ctk.CTkButton(
            self.SimpleModWindow,
            width=78,
            height=75,
            corner_radius=20,
            fg_color="#42C24B",
            hover_color="#0AE617",
            font=("Century Gothic", 35 * -1),
            text="ө",
            text_color="black",
            command=Word4
        )
        self.W4Button.place(
            x=426.0,
            y=185.0
        )

        self.W5Button = ctk.CTkButton(
            self.SimpleModWindow,
            width=78,
            height=75,
            corner_radius=20,
            fg_color="#42C24B",
            hover_color="#0AE617",
            font=("Century Gothic", 35 * -1),
            text="ү",
            text_color="black",
            command=Word5
        )
        self.W5Button.place(
            x=546.0,
            y=185.0
        )

        self.W6Button = ctk.CTkButton(
            self.SimpleModWindow,
            width=78,
            height=75,
            corner_radius=20,
            fg_color="#42C24B",
            hover_color="#0AE617",
            font=("Century Gothic", 35 * -1),
            text="һ",
            text_color="black",
            command=Word6
        )
        self.W6Button.place(
            x=666.0,
            y=185.0
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
            y=942
        )


class GameModMenu:
    def __init__(self, parent):
        self.GameModWindow = ctk.CTkToplevel(parent)
        self.GameModWindow.geometry("1920x1080")
        self.GameModWindow.configure(bg="#504D4D")
        self.GameModWindow.title("Игровой режим")
        self.GameModWindow.resizable(True, True)
        self.GameModWindow.attributes("-fullscreen", True)

        self.Tcount = 0
        self.Fcount = 0

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
                self.Text_For_Description.insert(1.0, random_word_with_explain(r"Assets/Words/"))
                self.T = 1
            else:
                self.Text_For_Description.delete(1.0, ctk.END)
                self.Text_For_Description.insert(1.0, random_word_random_explain(r"Assets/Words/"))
                self.T = 0

        def checkT():
            """
            Проверка ответа
            """
            if self.T == 1:
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.insert(1.0, f"Правильный ответ!\n{Explain(WordInText(), "Assets/Words/")}")
                self.Explaining.configure(fg_color="#42C24B")
                self.Tcount += 1
                self.Tcounter.delete(1.0, ctk.END)
                self.Tcounter.insert(1.0, self.Tcount)
                game()
            else:
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.insert(1.0, f"Неправильный ответ!\n{Explain(WordInText(), "Assets/Words/")}")
                self.Explaining.configure(fg_color="red")
                self.Fcount += 1
                self.Fcounter.delete(1.0, ctk.END)
                self.Fcounter.insert(1.0, self.Fcount)
                game()

        def checkF():
            """
            проверка ответа
            """
            if self.T == 0:
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.insert(1.0, f"Правильный ответ!\n{Explain(WordInText(), "Assets/Words/")}")
                self.Explaining.configure(fg_color="#42C24B")
                self.Tcount += 1
                self.Tcounter.delete(1.0, ctk.END)
                self.Tcounter.insert(1.0, self.Tcount)
                game()

            else:
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.delete(1.0, ctk.END)
                self.Explaining.insert(1.0, f"Неправильный ответ!\n{Explain(WordInText(), "Assets/Words/")}")
                self.Explaining.configure(fg_color="red")
                self.Fcount += 1
                self.Fcounter.delete(1.0, ctk.END)
                self.Fcounter.insert(1.0, self.Fcount)
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
            y=646.0
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
            y=646.0
        )

        self.Explaining = ctk.CTkTextbox(
            self.GameModWindow,
            width=675,
            height=567,
            corner_radius=16,
            fg_color="white",
            text_color="black",
            font=("Inter SemiBold", 25 * -1),
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
            y=942
        )

        self.Fcounter = ctk.CTkTextbox(
            self.GameModWindow,
            fg_color="#CC3343",
            corner_radius=16,
            font=("Century Gothic", 40 * -1),
            text_color="black",
            width=316,
            height=91
        )
        self.Fcounter.place(
            x=58.0,
            y=811.0
        )
        self.Fcounter.insert(1.0, self.Fcount)

        self.Tcounter = ctk.CTkTextbox(
            self.GameModWindow,
            fg_color="#42C24B",
            corner_radius=16,
            font=("Century Gothic", 40 * -1),
            text_color="black",
            width=308,
            height=93
        )
        self.Tcounter.place(
            x=428.0,
            y=811.0
        )
        self.Tcounter.insert(1.0, self.Tcount)

        if random.randint(1, 2) == 1:
            self.Text_For_Description.delete(1.0, ctk.END)
            self.Text_For_Description.insert(1.0, random_word_with_explain(r"Assets/Words/"))
            self.T = 1
        else:
            self.Text_For_Description.delete(1.0, ctk.END)
            self.Text_For_Description.insert(1.0, random_word_random_explain(r"Assets/Words/"))
            self.T = 0


class Addition:
    def __init__(self, parent):
        self.AdditionWindow = ctk.CTkToplevel(parent)
        self.AdditionWindow.geometry("1920x1080")
        self.AdditionWindow.configure(bg="#504D4D")
        self.AdditionWindow.title("Игровой режим")
        self.AdditionWindow.resizable(True, True)
        self.AdditionWindow.attributes("-fullscreen", True)

        def leave():
            menu = MenuOfDictionary()
            menu.dei()
            self.AdditionWindow.destroy()

        def operation():
            if "Добавить" == self.Control.get():
                WordAdd(self.WordEntry.get(), self.ExplainEntry.get(), "Assets/Words/")
            if "Удалить" == self.Control.get():
                WordDelete(self.WordEntry.get(), "Assets/Words/")
            if "Изменить" == self.Control.get():
                word = self.WordEntry.get()
                explain = self.ExplainEntry.get()
                WordDelete(word, "Assets/Words/")
                WordAdd(word, explain, "Assets/Words/")

        self.LeaveButton = ctk.CTkButton(
            self.AdditionWindow,
            fg_color="#42C24B",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text="Выход",
            text_color="black",
            command=leave,
            width=548,
            height=173
        )
        self.LeaveButton.place(
            x=1329.0,
            y=28.0,
        )

        self.OperationButton = ctk.CTkButton(
            self.AdditionWindow,
            fg_color="#42C24B",
            hover_color="#0AE617",
            corner_radius=16,
            font=("Century Gothic", 35 * -1),
            text="Совершить операцию",
            text_color="black",
            command=operation,
            width=548,
            height=173
        )
        self.OperationButton.place(
            x=686.0,
            y=28.0,
        )

        self.Control = ctk.CTkComboBox(
            self.AdditionWindow,
            values=["Добавить", "Изменить", "Удалить"],
            fg_color="#42C24B",
            corner_radius=16,
            font=("Century Gothic", 60 * -1),
            text_color="black",
            hover=True,
            dropdown_fg_color="#42C24B",
            button_hover_color="green",
            dropdown_hover_color="green",
            justify="center",
            border_color="#42C24B",
            dropdown_font=("Century Gothic", 60 * -1),
            dropdown_text_color="black",
            width=548,
            height=173
        )
        self.Control.place(
            x=43.0,
            y=28.0
        )

        self.WordEntry = ctk.CTkEntry(
            self.AdditionWindow,
            width=553,
            height=180,
            corner_radius=16,
            justify="center",
            fg_color="white",
            text_color="black",
            font=("Inter SemiBold", 30 * -1),
            placeholder_text="Введите слово"
        )
        self.WordEntry.place(
            x=38.0,
            y=579.0
        )

        self.ExplainEntry = ctk.CTkEntry(
            self.AdditionWindow,
            width=1191,
            height=723,
            corner_radius=16,
            justify="center",
            fg_color="white",
            text_color="black",
            font=("Inter SemiBold", 30 * -1),
            placeholder_text="Введите определение(при удалении не обязательно)"
        )
        self.ExplainEntry.place(
            x=686.0,
            y=302.0
        )


if __name__ == '__main__':
    main = MenuOfDictionary()
    main.run()

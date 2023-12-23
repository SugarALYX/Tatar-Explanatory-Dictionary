from gui.Interface.Simplemod import SimpleModMenu
from gui.Interface.RandomMod import RandomModMenu
from gui.Interface.GameMod import GameModMenu
import customtkinter as ctk


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
            text="Простой режим: вы вводите слово, программа \nнаходит этому слову определение\n\nСлучайный режим: вы "
                 "нажимаете на кнопку и\nполучаете случайное слово с определением\n\nИгра: вам даётся случайное слово и"
                 "случайное\nопределение, вы должны ответить правильно\nли подобрано определение\n\n"
                 "Авто: Шайхутдинов Абу Бакр Ильгамович,\nученик 10 класса МБОУ \"Нурминская СОШ\"",
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
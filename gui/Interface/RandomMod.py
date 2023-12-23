import customtkinter as ctk
from gui.Interface.WordFind import random_word_with_explain


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
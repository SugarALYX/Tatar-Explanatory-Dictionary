import customtkinter as ctk
from gui.Interface.WordFind import Explain


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
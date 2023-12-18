from tkinter import Canvas, Text, Button, PhotoImage, Toplevel


class GameModMenu:
    def __init__(self, parent):
        ASSETS_PATH = r"assets\frame2"
        self.GameModWindow = Toplevel(parent)
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

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(
            file=f"{ASSETS_PATH}/button_1.png")
        self.F_Button = Button(
            self.GameModWindow,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
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
            command=lambda: print("button_2 clicked"),
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
            font=("Inter SemiBold", 35 * -1),
            bd=0,
            bg="#6EB755",
            fg="#000716",
            highlightthickness=0
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

        self.entry_3 = Text(
            self.GameModWindow,
            font=("Inter SemiBold", 20 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        self.entry_3.place(
            x=465.0,
            y=460.0,
            width=351.0,
            height=238.0
        )

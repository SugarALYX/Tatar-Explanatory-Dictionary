from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Simplemod import SimpleModMenu


class MenuOfDictionary:
    def __init__(self):
        ASSETS_PATH = r"assets/frame0"
        self.Menu = Tk()
        self.Menu.title("Татарский толковый словарь")
        self.Menu.geometry("1280x720")
        self.Menu.configure(bg="#504D4D")
        self.Menu.resizable(False, False)

        def CreatSimpleModWindow():
            SimpleModMenu(self.Menu)

        self.canvas = Canvas(
            self.Menu,
            bg="#504D4D",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=f"{ASSETS_PATH}/image_1.png")
        self.image_1 = self.canvas.create_image(
            665.0,
            59.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            295.0,
            29.0,
            anchor="nw",
            text="  Татарский толковый словарь",
            fill="#010101",
            font=("Inter SemiBold", 50 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=f"{ASSETS_PATH}/button_1.png")
        self.MenuSimpleModButton = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=CreatSimpleModWindow,
            relief="flat"
        )
        self.MenuSimpleModButton.place(
            x=46.0,
            y=185.0,
            width=524.0,
            height=105.0
        )

        self.button_image_2 = PhotoImage(
            file=f"{ASSETS_PATH}/button_2.png")
        self.GameModButton = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.GameModButton.place(
            x=46.0,
            y=541.0,
            width=524.0,
            height=105.0
        )

        self.button_image_3 = PhotoImage(
            file=f"{ASSETS_PATH}/button_3.png")
        self.RandomModButton = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.RandomModButton.place(
            x=46.0,
            y=371.0,
            width=524.0,
            height=105.0
        )

        self.image_image_2 = PhotoImage(
            file=f"{ASSETS_PATH}/image_2.png")
        self.image_2 = self.canvas.create_image(
            939.0,
            415.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            655.0,
            576.0,
            anchor="nw",
            text="""Приложение сделал ученик 10 класса
МБОУ “Нурминская СОШ”,Шайхутдинов Абу Бакр Ильгамович""",
            fill="#171717",
            font=("Inter SemiBold", 20 * -1)
        )

        self.canvas.create_text(
            655.0,
            267.0,
            anchor="nw",
            text="Простой режим: вы вводите слово, программа \nнаходит этому слову определение\n\nСлучайный режим: вы "
                 "нажимаете на кнопку и\nполучаете случайное слово с определением\n\nИгра: вам даётся случайное слово и"
                 "случайное\nопределение, вы должны ответить правильно\nли подобрано определение",
            fill="#0B0B0B",
            font=("Inter SemiBold", 20 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=f"{ASSETS_PATH}/image_3.png")
        self.image_3 = self.canvas.create_image(
            145.0,
            80.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=f"{ASSETS_PATH}/image_4.png")
        self.image_4 = self.canvas.create_image(
            1176.0,
            86.0,
            image=self.image_image_4
        )

    def run(self):
        self.Menu.mainloop()


if __name__ == "__main__":
    app = MenuOfDictionary()
    app.run()

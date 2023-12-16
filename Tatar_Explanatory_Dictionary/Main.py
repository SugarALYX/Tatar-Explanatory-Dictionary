import tkinter as tk
import tkinter.font as tkFont


def file_txt(Your_word: str) -> str:
    """
    Находит подходящий файл по слову
    :return: подходящий файл
    """
    Files = {
        "А": "Aa.txt",
        "Ә": "A`a`.txt",
        "Б": "Bb.txt",
        "В": "Vv.txt",
        "Г": "Gg.txt",
        "Д": "Dd.txt",
        "Җ": "Zhzh.txt",
        "Ж": "Zhzh.txt",
        "З": "Zz.txt",
        "И": "Ii.txt",
        "Й": "Jj.txt",
        "К": "Kk.txt",
        "Л": "Ll.txt",
        "М": "Mm.txt",
        "Н": "Nn.txt",
        "О": "Oo.txt",
        "Ө": "O`o`.txt",
        "П": "Pp.txt",
        "Р": "Rr.txt",
        "С": "Ss.txt",
        "Т": "Tt.txt",
        "У": "Uu.txt",
        "Ү": "U`u`.txt",
        "Ф": "Ff.txt",
        "Х": "Hh.txt",
        "Һ": "H`h`.txt",
        "Ч": "Chch.txt",
        "Ш": "Shsh.txt",
        "Ы": "Yy.txt",
        "Э": "Ee.txt",
        "Ю": "Juju.txt",
        "Я": "Jaja.txt"
    }
    return Files[Your_word[0]]


def Explain(Your_word: str) -> str:
    """
    Функция находит слова(param word) и даёт ему объяснение, найдя его в тестовом файле
    :param Your_word: Искомое слово
    :return: текст объяснения
    """
    try:
        Your_word = Your_word.capitalize()
        wordEX = Your_word + " -"

        ReturnText = ""
        fileo = open(file_txt(Your_word), "r", encoding="utf-8")
        fileText = fileo.read()
        if wordEX in fileText:
            index = fileText.find(wordEX)
            while fileText[index] != "\n":
                ReturnText += fileText[index]
                index += 1
            for i in range(120, len(ReturnText), 120):
                char = i
                if char <= len(ReturnText):
                    while char < len(ReturnText) and ReturnText[char] != " ":
                        char += 1
                    else:
                        ReturnText = ReturnText[:char] + "\n" + ReturnText[char + 1:]
            return ReturnText
        else:
            return "Слово не найдено"
    except TypeError or FileNotFoundError:
        return "Слово не найдено"


def WordAdd(New_word: str):
    """
    Функция для добавления слов в словарь
    :param New_word: Новое слово
    :return: Записывает новое слово для дальнейшего использования
    """
    pass


# Ә ә, Ө ө, Ү ү, Җ җ, Ң ң, Һ һ


class App:
    def __init__(self, root):
        root.title("Татарский толковый словарь")
        width = 1280
        height = 720
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_583 = tk.Entry(root)
        GLabel_583["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times', size=25)
        GLabel_583["font"] = ft
        GLabel_583["fg"] = "#000000"
        GLabel_583["justify"] = "center"
        GLabel_583["text"] = ""
        GLabel_583.place(x=350, y=90, width=578, height=60)

        GButton_703 = tk.Button(root)
        GButton_703["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=20)
        GButton_703["font"] = ft
        GButton_703["fg"] = "#000000"
        GButton_703["justify"] = "center"
        GButton_703["text"] = "Найти слово"
        GButton_703["relief"] = "groove"
        GButton_703.place(x=1010, y=90, width=206, height=57)
        GButton_703["command"] = self.Command

        GLabel_137 = tk.Label(root)
        GLabel_137["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times', size=20)
        GLabel_137["font"] = ft
        GLabel_137["fg"] = "#000000"
        GLabel_137["justify"] = "center"
        GLabel_137["text"] = ""
        GLabel_137.place(x=10, y=170, width=1258, height=537)

        GLabel_631 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=26)
        GLabel_631["font"] = ft
        GLabel_631["fg"] = "#000000"
        GLabel_631["justify"] = "center"
        GLabel_631["text"] = "Татарский толковый словарь"
        GLabel_631["relief"] = "flat"
        GLabel_631.place(x=380, y=10, width=516, height=59)

        GLabel_55 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=23)
        GLabel_55["font"] = ft
        GLabel_55["fg"] = "#333333"
        GLabel_55["justify"] = "center"
        GLabel_55["text"] = "Введите слово:"
        GLabel_55["relief"] = "groove"
        GLabel_55.place(x=30, y=90, width=275, height=60)

        GLabel_720 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_720["font"] = ft
        GLabel_720["fg"] = "#333333"
        GLabel_720["justify"] = "center"
        GLabel_720["text"] = "Автор: Шайхутдинов Абу Бакр Ильгамович"
        GLabel_720.place(x=1000, y=670, width=252, height=30)

    def Command(self):
        print(Explain("Алма"))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
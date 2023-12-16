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


import random as r


def random_file(way: str) -> str:
    """
    Функция выбирает случайный файл из словаря
    :param way: путь к словарю
    :return: текст словаря(одной буквы)
    """
    files = ["Aa.txt", "A`a`.txt", "Bb.txt", "Vv.txt", "Gg.txt", "Dd.txt", "Zhzh.txt", "Zhzh.txt", "Zz.txt", "Ii.txt",
             "Jj.txt", "Kk.txt", "Ll.txt", "Mm.txt", "Nn.txt", "Oo.txt", "O`o`.txt", "Pp.txt", "Ss.txt", "Tt.txt",
             "Uu.txt", "U`u`.txt", "Ff.txt", "Hh.txt", "H`h`.txt", "Chch.txt", "Shsh.txt", "Yy.txt", "Ee.txt",
             "Juju.txt", "Jaja.txt"]
    fileo = open(f"{way}{files[r.randint(0, len(files)) - 1]}", "r", encoding="utf-8")
    fileText = fileo.read()
    return fileText


def path(Your_word: str, way: str) -> str:
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
    return way + Files[Your_word[0]]


def Explain(Your_word: str, way: str) -> str:
    """
    Функция находит слова(param word) и даёт ему объяснение, найдя его в тестовом файле
    :param way: путь к словарю
    :param Your_word: Искомое слово
    :return: текст объяснения
    """
    try:
        Your_word = Your_word.capitalize()
        wordEX = Your_word + " -"

        ReturnText = ""
        fileo = open(path(Your_word, way), "r", encoding="utf-8")
        fileText = fileo.read()
        if wordEX in fileText:
            index = fileText.find(wordEX)
            while fileText[index] != "\n":
                ReturnText += fileText[index]
                index += 1
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


def random_word_with_explain(way: str) -> str:
    """
    Функция находит случайное слово и её определение
    :param way: путь к репозиторию
    :return:
    """
    fileText = random_file(way)
    ReturnWord = ""
    index = r.randint(0, len(fileText))
    while True:
        try:
            while fileText[index] != "\n":
                index += 1
            while fileText[index] == "\n":
                index += 1
            while fileText[index] != "\n":
                ReturnWord += fileText[index]
                index += 1
            if index == "\n":
                break
        except IndexError:
            index = r.randint(0, len(fileText))
        return ReturnWord


def random_word_random_explain(way: str) -> str:
    ReturnWord = ""
    ForWordWay = random_file(way)
    index = r.randint(0, len(ForWordWay))
    while True:
        try:
            while ForWordWay[index] != "\n":
                index += 1
            while ForWordWay[index] == "\n":
                index += 1
            while ForWordWay[index] != "-":
                ReturnWord += ForWordWay[index]
                index += 1
            if ForWordWay[index] == "-":
                break
        except IndexError:
            index = r.randint(0, len(ForWordWay))
    ForWordExplainWay = random_file(way)
    index = r.randint(0, len(ForWordExplainWay))
    while True:
        try:
            while ForWordExplainWay[index] != "\n":
                index += 1
            while ForWordExplainWay[index] == "\n":
                index += 1
            while ForWordExplainWay[index] != " ":
                index += 1
            while ForWordExplainWay[index] != "\n":
                ReturnWord += ForWordExplainWay[index]
                index += 1
            if ForWordExplainWay[index] == "\n":
                break
        except IndexError:
            index = r.randint(0, len(ForWordExplainWay))
    return ReturnWord

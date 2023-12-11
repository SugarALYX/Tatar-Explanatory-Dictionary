def Explain(Your_word: str) -> str:
    """
    Функция находит слова(param word) и даёт ему объяснение, найдя его в тестовом файле
    :param Your_word: Искомое слово
    :return: текст объяснения
    """

    def file_Txt() -> str:
        """
        Находит подходящий файл по слову
        :return: подходящий файл
        """
        match Your_word[0]:
            case "А":
                return "Aa.txt"
            case "Ә":
                return "A`a`.txt"
            case "Б":
                return "Bb.txt"
            case "В":
                return "Vv.txt"
            case "Г":
                return "Gg.txt"
            case "Д":
                return "Dd.txt"
            case "Җ" | "Ж":
                return "Zhzh.txt"
            case "З":
                return "Zz.txt"
            case "И":
                return "Ii.txt"
            case "Й":
                return "Jj.txt"
            case "К":
                return "Kk.txt"
            case "Л":
                return "Ll.txt"
            case "М":
                return "Mm.txt"
            case "Н":
                return "Nn.txt"
            case "О":
                return "Oo.txt"
            case "Ө":
                return "O`o`.txt"
            case "П":
                return "Pp.txt"
            case "Р":
                return "Rr.txt"
            case "С":
                return "Ss.txt"
            case "Т":
                return "Tt.txt"
            case "У":
                return "Uu.txt"
            case "Ү":
                return "U`u`.txt"
            case "Ф":
                return "Ff.txt"
            case "Х":
                return "Hh.txt"
            case "Һ":
                return "H`h`.txt"
            case "Ч":
                return "Chch.txt"
            case "Ш":
                return "Shsh.txt"
            case "Ы":
                return "Yy.txt"
            case "Э":
                return "Ee.txt"
            case "Ю":
                return "Juju.txt"
            case "Я":
                return "Jaja.txt"

    wordEX = Your_word + " -"

    ReturnText = ""
    fileo = open(file_Txt(), "r", encoding="utf-8")
    fileText = fileo.read()
    if word in fileText:
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
                    ReturnText = ReturnText[:char] + "\n" + ReturnText[char+1:]
        return ReturnText
    else:
        return "Слово не найдено"


try:
    word = input("Введите слово:  ")
    word = word.capitalize()
    print(Explain(word))
except TypeError:
    print("Слово не найдено")

# Ә ә, Ө ө, Ү ү, Җ җ, Ң ң, Һ һ

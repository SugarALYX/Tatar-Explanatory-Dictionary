def Explain(word: str) -> str | int:
    """
    Функция находит слова(param word) и даёт ему объяснение, найдя его в тестовом файле
    :param word: Искомое слово
    :return: текст объяснения
    """
    def file_Txt() -> str:
        """
        Находит подходящий файл по слову
        :return: подходящий файл
        """
        match word[0]:
            case "A" | "a":
                return "Aa.txt"
            case "Ә" | "ә":
                return "A`a`.txt"
            case "Б" | "б":
                return "Bb.txt"
            case "В" | "в":
                return "Vv.txt"
            case "Г" | "г":
                return "Gg.txt"
            case "Д" | "д":
                return "Dd.txt"
            case "Җ" | "Җ" | "Ж" | "ж":
                return "Jeje.txt"
            case "З" | "з":
                return "Zz.txt"
            case "И" | "и":
                return "Ii.txt"
            case "Й" | "й":
                return "Jj.txt"
            case "К" | "к":
                return "Kk.txt"
            case "Л" | "л":
                return "Ll.txt"
            case "М" | "м":
                return "Mm.txt"
            case "Н" | "н":
                return "Nn.txt"
            case "О" | "о":
                return "Oo.txt"
            case "Ө" | "ө":
                return "O`o`.txt"
            case "П" | "п":
                return "Pp.txt"
            case "Р" | "р":
                return "Rr.txt"
            case "С" | "с":
                return "Ss.txt"
            case "Т" | "т":
                return "Tt.txt"
            case "У" | "У":
                return "Uu.txt"
            case "Ү" | "ү":
                return "U`u`.txt"
            case "Ф" | "ф":
                return "Ff.txt"
            case "Х" | "х":
                return "Hh.txt"
            case "Һ" | "һ":
                return "H`h`.txt"
            case "Ч" | "ч":
                return "Chch.txt"
            case "Ш" | "ш":
                return "Shsh.txt"
            case "Ы" | "ы":
                return "Yy.txt"
            case "Э" | "э":
                return "Ee.txt"
            case "Ю" | "ю":
                return "Juju.txt"
            case "Я" | "я":
                return "Jaja.txt"
    wordEX = word + " -"

    ReturnText = ""
    fileo = open(file_Txt(), "r", encoding="utf-8")
    fileText = fileo.read()
    index = fileText.find(wordEX)
    while fileText[index] != "\n":
        ReturnText += fileText[index]
        index += 1
    return ReturnText


try:
    word = input()
    print(Explain(word))
except TypeError:
    print("Слово не найдено")
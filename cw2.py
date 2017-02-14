## 1. (5 баллов) Посчитать число строк заголовка XML (то есть от начала файла до строки, которая содержит "</teiHeader>"), открыть другой файл для записи, записать туда число.
## 2. (8 баллов) Создать словарь, в котором ключами являются строки с морфологическим разбором слов (то есть значения атрибута type для строк, в которых имеется "<w lemma="), а значениями - количество их вхождений в файле. Распечатать пары ключ-значение из словаря в открытый для записи файл таким образом, чтобы каждая пара располагалась на одной строке.
## 3. (10 баллов) С помощью регулярных выражений найти все вхождения местоимений среднего года (то есть таких разборов, в которых type=" начинается с "f" и содержит "h" на третьей позиции, например: type="fohfþ"). Соответствующие этим характеристикам словоформы распечатать в том же файле для записи в одну строку через запятую.
    # Преобразуйте содержимое корпуса в формат csv. Возьмите строки внутри тэга <body> и очистите их от тэгов.
    # Запишите результат в новый файл следующим образом: на одной строке должны находиться лемма, разбор, словоформа, разделенные запятыми.
    # Пунктацию и служебную информацию можно удалить.


def counting():
    with open('isl.txt', 'r', encoding='utf-8') as islen:
        islen.read()
        str = islen.readline().replace('\n', '')
        islenlines = []
        islencount = 0
        for line in islen:
            islenlines.append
            islencount = 0
            if '</teiHHeader>' in line:
                break
        print(islencount)
    #with open('islcw2.txt', 'w') as cw:
    #    cw.write(int[islencount])
    #cw.close
    #islen.close
counting()

def dictionary():
    lemmas = []
    alsolemmas = []
    str = islen.readline
    for i in range(str):
        if '<w lemma=")' in line:
            lemmas.append(line)
            if line not in alsolemmas:
                alsolemmas.append(line)
    for line in alsolemmas:
        freq = []
        n = lemmas.count(line)
        freq.append(n)
        print(line)
           
dictionary()

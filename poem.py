import random
def w1():
    a = open('опять.txt', 'r', encoding = 'utf-8')
    for text in a:
        str = text.split()
        return random.choice(str)
    a.close

def w2():
    b = open('тупим.txt', 'r', encoding = 'utf-8')
    for text in b:
        str = text.split()
        return random.choice(str)
    b.close

def w3():
    c = open('тобой.txt', 'r', encoding = 'utf-8')
    for text in c:
        str = text.split()
        return random.choice(str)
    c.close

def prep():
    prep = ['на', 'сквозь', 'под', 'за']
    return random.choice(prep)

def w4():
    d = open('груды.txt', 'r', encoding = 'utf-8')
    for text in d:
        str = text.split()
        return random.choice(str)
    d.close

def w5():
    e = open('розовея.txt', 'r', encoding = 'utf-8')
    for text in e:
        str = text.split()
        return random.choice(str)
    e.close

def w6():
    e = open('вдалеке.txt', 'r', encoding = 'utf-8')
    for text in e:
        str = text.split()
        return random.choice(str)
    e.close

def w7():
    e = open('танцуют.txt', 'r', encoding = 'utf-8')
    for text in e:
        str = text.split()
        return random.choice(str)
    e.close

def w8():
    e = open('острыми.txt', 'r', encoding = 'utf-8')
    for text in e:
        str = text.split()
        return random.choice(str)
    e.close

def w9():
    e = open('когтями.txt', 'r', encoding = 'utf-8')
    for text in e:
        str = text.split()
        return random.choice(str)
    e.close

def w10():
    e = open('твои.txt', 'r', encoding = 'utf-8')
    for text in e:
        str = text.split()
        return random.choice(str)
    e.close

def w11():
    e = open('жестокие.txt', 'r', encoding = 'utf-8')
    for text in e:
        str = text.split()
        return random.choice(str)
    e.close

def w12():
    e = open('слова.txt', 'r', encoding = 'utf-8')
    for text in e:
        str = text.split()
        return random.choice(str)
    e.close
    
def verse1():
    return w1() + " " + w2() + " c " + w3() + " " + prep() + " " + w4()

def verse2():
    return 'и ' + w5() + ' ' + w6()

def verse3():
    return w7() + " " + w8() + " " + w9()

def verse4():
    return w10() + " " + w11() + " " + w12()

for n in range(1):
    print(verse1())
    print(verse2())
    print(verse3())
    print(verse4())

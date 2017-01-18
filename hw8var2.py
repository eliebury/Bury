# 2. сколько в тексте разных существительных с суффиксом -ness и какое существительное из них имеет максимальную частотность.

def opentext():
    words = []
    with open ('гип.txt', 'r', encoding='utf-8') as f:
        for line in f.read().replace('\n', ' ').split():
            words.append(line.lower())
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?()«»;:-')
    return words

def aff(words):
    count_ness = 0
    nesses = []
    nesses_words = []
    for i in range((len(words))):
        if words[i].endswith('ness'):
            nesses.append(words[i])
            if words[i] not in nesses_words:
                nesses_words.append(words[i])
                count_ness += 1
    print('Слов с суффиксом -ness ', count_ness, ' штук(и):')
    for word in nesses_words:
        freq = []
        n = nesses.count(word)
        freq.append(n)
        print(word)
    for n in freq:
        if n is max(freq):
            print('Самое частотное слово: ', word, '; количество вхождений: ', n, sep='')

aff(opentext())

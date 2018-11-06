"""Case-study #4 Text analysis
Developers:
Bliznyak Anastasia, Vdovidskaya Valeria,Manko Andrei.

"""
from ru_local import *

text = input(INPUTTEXT)
count_sentences = 0
count_words = 1 + text.count(' ')
for i in range(len(text)):
    if text[i] == '—':
        count_words -= 1
count_syllables = 0
for i in range(len(text)):
    if text[i] == '.':
        count_sentences += 1

for i in range(len(text)):
    if text[i] == 'а' or text[i] == 'у' or text[i] == 'о' or text[i] == 'ы' or text[i] == 'и' or text[i] == 'э' or text[
        i] == 'ю' or text[i] == 'я' or text[i] == 'е' or text[i] == 'ё' or text[i] == 'А' or text[i] == 'У' or text[
        i] == 'О' or text[i] == 'Ы' or text[i] == 'И' or text[i] == 'Э' or text[i] == 'Ю' or text[i] == 'Я' or text[
        i] == 'Е' or text[i] == 'Ё':
        count_syllables += 1
ASL = count_words / count_sentences
ASW = count_syllables / count_words
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)

print(SENTENCES, count_sentences)
print(WORDS, count_words)
print(SYLLABLE, count_syllables)
print(AVERAGEWORDS, ASL)
print(AVERAGESYLLABLE, ASW)
print(INDEX, FRE)
if FRE <= 25:
    print(HARD)
elif 25 <= FRE <= 50:
    print(DIFFICULT)
elif 50 <= FRE <= 80:
    print(EAZY)
elif FRE >= 80:
    print(VERYEAZY)



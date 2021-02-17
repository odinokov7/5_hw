# pip install translate

from translate import Translator

translator = Translator(from_lang='en', to_lang='ru')
c = []
stroka = ''

f_1 = open("ex4.txt")
content_1 = f_1.readlines()
f_1.close()

for el in content_1:
    a = el
    b = a.split(' ')
    b[0] = translator.translate(b[0])
    c.append(b)

f_2 = open("ex4_1.txt", "w", encoding='utf-8')
for el in c:
    for each in el:
        stroka += ' ' + str(each)
    f_2.write(stroka[1:])
    stroka = ''
f_2.close()

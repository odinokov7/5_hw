f = open('ex2.txt', encoding='utf-8')
str_count = 0
c = []
str_count_print = 0
content = f.readlines()

for el in content:
    str_count += 1
    a = str(el)
    b = a.split(' ')
    word_count = 0
    for each in b:
        word_count += 1
    c.append(word_count)

print('Кол-во строк:', str_count)
for el in c:
    str_count_print += 1
    print(f'Строка № {str_count_print}: кол-во слов - {el}')

f.close()

d = []
k = []
summa = []

dict_final = {}

h = 0

f = open('ex6.txt', encoding='utf-8')
a = f.read().splitlines()
f.close()

for el in a:
    b = el
    c = b.split(' ')
    d.append(c)
    k.append(c[0][:len(c[0]) - 1])  # Удаляем ":" и заносим в список предметов
print(k)

for el in d:  # Считаем сумму часов
    suma = 0
    for each in el:
        if each.isnumeric():
            suma += int(each)
    summa.append(suma)
print(summa)

for h in range(len(k)):
    di = {}
    di = dict.fromkeys([k[h]], summa[h])
    dict_final = {**dict_final, **di}
    h += 1

print(dict_final)

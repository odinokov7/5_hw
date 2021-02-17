import json

with open('ex7.txt', encoding='utf-8') as f:
    a = f.read().splitlines()

d = []
k_1 = []
k_2 = []
result = []

inc = 0
summa = 0
index = 0

dict_final = {}
di = {}
di_avg = {}

for el in a:
    b = el
    c = b.split(' ')
    d.append(c[0])
    d.append((int(c[2]) - int(c[3])))

k_1 = d[::2].copy()
k_2 = d[1::2].copy()

for el in k_2:
    int_el = int(el)
    if int_el > 0:
        inc += 1
        summa += int_el

for index in range(len(k_1)):
    di = dict.fromkeys([k_1[index]], k_2[index])
    dict_final = {**dict_final, **di}
    index += 1

avg_value = summa / inc
di_avg = dict.fromkeys(['average_profit'], avg_value)
result.append(dict_final)
result.append(di_avg)

print(result)

with open('my_json.json', 'w') as f_json:
    json.dump(result, f_json)

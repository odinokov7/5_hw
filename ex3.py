f = open('ex3.txt', encoding='utf-8')
content = f.readlines()
f.close()

people_count = 0
summar = 0

for el in content:
    people_count += 1
    a = str(el)
    b = a.split(' ')
    summar += int(b[1])
    if int(b[1]) < 20000:
        print(b[0])

print('Средний заработок: ', summar / people_count)


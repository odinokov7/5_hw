a = input('Введите числа через пробел: ')
summar = 0

f_1 = open('ex5_1.txt', 'w')
f_1.write(a)
f_1.close()

f_2 = open('ex5_1.txt')
b = f_2.readline()
f_2.close()

c = b.split(' ')
for el in c:
    summar += int(el)
print(summar)

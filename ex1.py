f = open("user_file.txt", "w")
while True:
    a = input('Введите строку: ')
    if a != '':
        f.write(a + "\n")
    else:
        break
f.close()

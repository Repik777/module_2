number = int(input('Введите число от 3 до 20: '))
result = ''

for i in range(1, number):
    for k in range(1+i, number + 1):
        if number % (i + k) == 0:
            result += str(i) +str(k)
print(result)



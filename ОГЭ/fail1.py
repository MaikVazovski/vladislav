sum = 0
value = 1
while value != 0:
    value = int(input('Введите число:'))
    if value % 6 == 0 and value % 10 == 4:
        sum += value
print(sum)
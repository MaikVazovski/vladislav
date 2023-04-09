import numpy as np
a = int(input('Введите основание: '))
b = int(input('Введите степень: '))
c = a**b
print(f'Число = {c}')
x = [int(d) for d in str(c)]
sum = np.sum(x)
print(f'Сумма цифр степени = {sum}')

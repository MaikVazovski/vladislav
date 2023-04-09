import numpy as np
a = int(input('Введите основание: '))
b = int(input('Введите степень: '))
result = a**b
print(f'Число = {result}')
x = [int(d) for d in str(result)]
sum = np.sum(x)
print(f'Сумма цифр степени = {sum}')

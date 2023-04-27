A = []
n = int(input('Введите кол-во итераций: '))
for i in range(n):
    a = int(input('>'))
    if a % 10 == 1:
        A.append(a)
if len(A) > 0:
    print(f'Максимальное значение: {max(A)}')
else:
    print("Нет")
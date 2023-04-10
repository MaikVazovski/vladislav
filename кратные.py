one_value = int(input('Введи число, которое будем проверять на делимость: '))
two_value = int(input('Введите первый делитель: '))
three_value = int(input('Введите второе делитель: '))
if one_value % two_value == 0 and one_value % three_value == 0:
    print(f'Число кратно {two_value} и {three_value}')
elif one_value % two_value == 0:
    print(f'Число кратно только {two_value}')
elif one_value % three_value == 0:
    print(f'Число кратно только {three_value}')
else:
    print(f'Число не кратно {two_value} и {three_value}')
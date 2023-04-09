from colorama import init
init()
from colorama import Fore, Back, Style
sum = 0
print(Fore.CYAN)
cost = float(input('Стоимость товара в рублях: '))
while sum < cost:
    print(Fore.MAGENTA)
    payment = float(input('Заплатите: '))
    if payment <= 0:
        print(Fore.CYAN)
        print('Такого не бывает')
        continue
    sum += payment
    if sum < cost:
        print(Fore.GREEN)
        print(f'Маловато будет. Заплатите еще {cost - sum:.2f} рублей')
    else:
        print(Fore.YELLOW)
        print(f'Вы заплатили достаточно, товар куплен. Ваша сдача: {sum-cost:.2f} рублей')
        
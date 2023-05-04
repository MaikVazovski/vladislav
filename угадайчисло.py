import random
from colorama import init
init()
from colorama import Fore
a = random.randint(1,100)

def random_value(input_value):
    print(Fore.LIGHTRED_EX)
    b = int(input('Угадай число от 1 до 100: '))

    if b > input_value:
        print(Fore.LIGHTYELLOW_EX)
        print(f'Много ты взял. Число меньше, чем {b}')
        random_value(input_value)
    elif b == a:
        print(Fore.LIGHTMAGENTA_EX)
        print(f'Ты угадал! Это число {b}')
    else:
        print(Fore.LIGHTCYAN_EX)
        print(f'Слишком мало взял. Число больше, чем {b}')
        random_value(input_value)

random_value(a)
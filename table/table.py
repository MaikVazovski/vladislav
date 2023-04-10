# pip install prettytable (Устанавливаем модуль)

# Импортируем его
from prettytable import PrettyTable
from colorama import init
init()
from colorama import Fore
# Пишем код
table = PrettyTable()
# мой пример
table.field_names = ['Имя', 'Значение'] # шапка таблицы
# добавляем ряды
print(Fore.LIGHTCYAN_EX)
table.add_row(['Cаша', 'Лoх'])  
table.add_row(['Настя', 'Лох'])
table.add_row(['Соня', 'Лох'])
table.add_row(['Даша', 'Лох'])

# выводим таблицу

print(Fore.CYAN)
print('---------Имя---------') #сам подбирай длину названия
print(table)


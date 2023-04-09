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
table.add_row(['Ссяша', 'Лoх'])  
table.add_row(['Снастя', 'Лох'])
table.add_row(['Стоня', 'Лох'])
table.add_row(['Сдача', 'Лох'])

# выводим таблицу

print(Fore.CYAN)
print('---------Имя---------') #сам подбирай длину названия
print(table)


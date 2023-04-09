from prettytable import PrettyTable
from colorama import init
init()
from colorama import Fore

table = PrettyTable()


table.field_names = ['Название', 'Время']
print('')
def get_table(tab, key, value):
    while key != 'stop':
        tab.add_row([key, value])
    return tab

get_table(table, 'Ура', "10:10")
print(table)

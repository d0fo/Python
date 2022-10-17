import Funcktions
import Logger
def menu ():
    print('\nМЕНЮ')
    print('1. Показать все записи.')
    print('2. Найти номер по фамилии.')
    print('3. Добавить новую запись.')
    menu_point = int(input())
    if menu_point == 1:
        Funcktions.contact_list()
    elif menu_point == 2:
        Funcktions.search_contact()
    elif menu_point == 3:
        Logger.add_contact()
menu()
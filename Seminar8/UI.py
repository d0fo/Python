import Funcktions
import Logger
def menu ():
    print('\nMENU')
    print('1. Show all data')
    print('2. Surname based searching')
    print('3. Add new employer.')
    print('4. Edit employer salary')
    menu_point = int(input())
    if menu_point == 1:
        Funcktions.employees_list()
    elif menu_point == 2:
        Funcktions.search_employer()
    elif menu_point == 3:
        Logger.add_employer()
    elif menu_point == 4:
        Funcktions.edit_employer()
menu()
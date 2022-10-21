import csv
from unicodedata import name
def search_employer():
    str_surname = input('Enter searching surname: ')
    with open ("employees.csv", mode="r", encoding='utf-8') as read_file:
        file_reader = csv.reader(read_file, delimiter=",")
        for row in file_reader:
            if row[2] == str_surname:
                print(row[0], row[1], row[2], row[3],row[4])
    
def employees_list():
    with open("employees.csv", mode = "r", encoding="utf-8") as list:
        list_reader = csv.reader(list, delimiter=",")
        for row in list_reader:
            print(row[0], row[1], row[2], row[3],row[4])

def edit_employer():
    with open("employees.csv", mode = "r") as in_data:
        employers = []
        list_in = csv.reader(in_data, delimiter=",")
        for row in list_in:
            employers.append(row)
        # print(employers)
        ediited_info = edit_employer_data(employers)
    with open("employees.csv", mode = "w") as out_data:
        list_out = csv.writer(out_data)
        for i in ediited_info:
            list_out.writerow(i)


def edit_employer_data(mass):
    salary_searching = input('Searching surname: ')
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            if mass[i][j].find(salary_searching) != -1:
                mass[i][j] = input('New salary: ')
    return mass


    # searching_surnam  e = input('Enter searching surname: ')
    # with open ("employees.csv", mode="wb") as out_data:
    #     list_out = csv.writer(out_data, delimiter=",")
    #     for row in list_in:
    #         # if row[2] == searching_surname:
    #         #     print(row[0], row[1], row[2], row[3],row[4])
    #         #     editing_name = input('Enter name: ')
    #         #     editing_position = input('Enter position: ')
    #         #     editing_salary = input('Enter salary: ')
    #         #     row[1] = editing_name
    #         #     row[3] = editing_position
    #         #     row[4] = editing_salary
    #         #     print(row[0], row[1], row[2], row[3],row[4])
    #         print(row)
    #         row[0]=0
    #         list_out.writerow(row)

            
    
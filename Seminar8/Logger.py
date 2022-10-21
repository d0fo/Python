import csv

def auto_id():
     with open("employees.csv", mode = "r", encoding="utf-8") as list:
        list_reader = csv.reader(list, delimiter=",")
        for row in list_reader:
            last_id = row[0]
        return str(int(last_id) + 1)

def add_employer ():
    # id = input ('Enter ID: ')
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    position = input('Enter position: ')
    salary = input ('Enter salary: ')
    with open("employees.csv", mode="a", encoding='utf-8') as w_file:
        contact = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        contact.writerow([auto_id(), name, surname, position, salary])



import csv
def search_contact():
    str_surname = input('Enter searching surname: ')
    with open ("phone_book.csv", mode="r", encoding='utf-8') as read_file:
        file_reader = csv.reader(read_file, delimiter=",")
        for row in file_reader:
            if row[1] == str_surname:
                print(row[0], row[1], row[2])

def contact_list():
    with open("phone_book.csv", mode = "r", encoding="utf-8") as list:
        list_reader = csv.reader(list, delimiter=",")
        for row in list_reader:
            print(row[0], row[1], row[2])
contact_list()






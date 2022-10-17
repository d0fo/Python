import csv
def add_contact ():
    str_name = input('Enter name: ')
    str_surname = input('Enter surname: ')
    str_phone_number = input('Enter phone number: ')
    with open("phone_book.csv", mode="a", encoding='utf-8') as w_file:
        contact = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        # contact.writerow(["Name", "Surname", "Phone_number"])
        contact.writerow([str_name, str_surname, str_phone_number])
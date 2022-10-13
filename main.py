import re
from pprint import pprint
from patterns import person_pattern, phone_pattern, phone_update, added_phone_update, added_phone
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

temp_list = []
contacts_list_fixed = []

for person in contacts_list:
    for data in person:
        if re.findall(phone_pattern, data):
            res = phone_pattern.sub(phone_update, data)
            temp_list.append(res)
        elif re.findall(person_pattern, data):
            i = person.index(data)
            temp_list[i:i + 1] = person[i].split()
        else:
            temp_list.append(data)
    while len(temp_list) != 7:
        temp_list.remove("")
        if len(temp_list) == 7:
            break
    contacts_list_fixed.append(temp_list)
    temp_list = []
contacts_list = contacts_list_fixed
contacts_list_fixed = []

for person in contacts_list:
    for data in person:
        if re.findall(added_phone, data):
            res = added_phone.sub(added_phone_update, data)
            temp_list.append(res)
        else:
            temp_list.append(data)
    contacts_list_fixed.append(temp_list)
    temp_list = []
contacts_list = contacts_list_fixed
contacts_list_fixed = []

for person in contacts_list:
    for person2 in contacts_list:
        if person[0] == person2[0] and person[1] == person2[1]:
            i = 0
            for elem in person2:
                if person[i] == '':
                    person[i] = person2[i]
                    i += 1
                else:
                    i += 1

for person in contacts_list:
    if person not in contacts_list_fixed:
        contacts_list_fixed.append(person)

pprint(contacts_list_fixed)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook_fixed.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_fixed)

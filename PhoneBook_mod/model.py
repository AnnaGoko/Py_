import text
phone_book = []
path = 'phones.txt'


#Открыть справочник
def open_pb():
    global phone_book
    with open(path, 'r', encoding = 'UTF-8') as file:
        main_list = file.readlines()
    print(main_list)
    for contact in main_list:
        contact = contact.strip().split(':')
        new = {'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
        phone_book.append(new)

#Изменить контакт
def edit_contact():
    name = input('Имя')
    new_data = input('Новое Имя')
    with open('r', encoding = 'UTF-8') as f:
        contacts = f.readlines()

    new_contacts = []
    for contact in contacts:
        if name in contact:
            new_contacts.append(new_data + '\n')
        else:
            new_contacts.append(contact)
    with open('phones.txt', 'w') as f:
        f.writelines(new_contacts)

#Удалить Контакт
def delete_contact():
    name = input('Имя')
    with open('phones.txt', 'r') as f:
        contacts = f.readlines()

    new_contacts = []
    for contact in contacts:
        if name not in contact:
            new_contacts.append(contact)

    with open('phones.txt', 'w') as f:
        f.writelines(new_contacts)

#Добавить контакт
def add_contact():
    name = input("Введите имя: ")
    surname = input ("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    comment = input('Введите комментарий: ')
    new_contacts = [name + ' :', surname + ' :', phone + ' :', comment + ' :']
    with open('phones.txt', 'w') as f:
      f.writelines(new_contacts)

#Найти
def find_contact():
    name = input('Введите имя: ')
    with open('phones.txt', 'r') as f:
        contacts = f.readlines()
        for contact in contacts:
            if name in contact:
                print (contact)
            else:
                 return None
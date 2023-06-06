#Вывод контактов
def open_file_read(path):
    with open (path, 'r') as file:
        main_list=(file.readlines())
        main_list_str=[x.rstrip().split(':') for x in main_list]
    return main_list_str



#Изменения контакта

def edit_contact(name, new_data):
    with open('phones.txt', 'r') as f:
        contacts = f.readlines()

    new_contacts = []
    for contact in contacts:
        if name in contact:
            new_contacts.append(new_data + '\n')
        else:
            new_contacts.append(contact)

    with open('phones.txt', 'w') as f:
        f.writelines(new_contacts)
        
#Удаления контакта
        
def delete_contact(name):
    with open('phones.txt', 'r') as f:
        contacts = f.readlines()

    new_contacts = []
    for contact in contacts:
        if name not in contact:
            new_contacts.append(contact)

    with open('phones.txt', 'w') as f:
        f.writelines(new_contacts)

#main
print ("Добро пожадовать в справочник ver:68352.4432308! \n Вы можете: \n 1. Вывести список всех контактов \n 2. Удалить контакт \n 3. Изменить контакт \n Введите цисло, что бы выполнить действие: ")
match_ = int(input())
match match_:

    case 1:
        print (open_file_read('phones.txt'))

    case 2:
        name = input("Введите Имя контакт: ")
        print (delete_contact(name))
    case 3:
        name, new_data = input("Введите Имя контакт: "), input(" Введите новые данные контакт: ")
        print (edit_contact(name, new_data))
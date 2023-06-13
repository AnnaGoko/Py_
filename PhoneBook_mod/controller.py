import view
import model
import text

def start():
    while True:
        choice = view.txt_menu()
        
        match choice:
            case 1: # Открыть
                view.print_messages(text.contacts)
                model.open_pb()
            case 2: # Сохранить
                pass
            case 3: # Показать
                pass
            case 4: # Добавить
                model.add_contact()
            case 5: # Найти
                model.find_contact()
            case 6: # Изменить
                model.edit_contact()
                #print (text.change)
            case 7: # Удалить
                model.delete_contact()
            case 8: # Выйти
                break
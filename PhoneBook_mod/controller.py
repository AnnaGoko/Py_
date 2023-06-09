import view
import model
import text

def start():
    while True:
        choice = view.txt_menu()
        
        match choice:
            case 1:
                view.print_messages(text.contacts)
                model.open_pb()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                model.edit_contact()
                #print (text.change)
            case 7:
                model.delete_contact()
            case 8:
                break
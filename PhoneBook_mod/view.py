import text

def txt_menu() -> int:
    print (text.txt_menu)
    while True:
        choice = input(text.txt_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def print_messages(message: str):
    print ('\n' + '='*len(message))
    print (message)
    print ('='*len(message) + '\n')

def print_contacts(book: list[dict[str,str]]):
    if book:
      for i, contact in enumerate (book, 1):
          print (f'{i:>3}. {contact.get("name"):<20} | {contact.get("phone"):<20} | {contact.get("comment"):<20} ')
    else:
        print_messages(text.null)
#------------------------------------------------------------------------------
# Бот-aсистент повинен вміти:
#   зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям
#   змінювати номер, і виводити всі записи
# Додати декоратор input_error, який обробляє винятки
#   KeyError, ValueError, IndexError у функціях handler
#------------------------------------------------------------------------------

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Give me name and phone please'
        except KeyError:
            return 'There\'s no such name in the list'
        except IndexError:
            return 'Give the name please'
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added'

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact changed'

@input_error
def get_number(args, contacts):
    name = args[0]
    return contacts[name]

def get_contacts(contacts):
    user_list = ['---- List of Users ----']
    for key, value in contacts.items():
        user_list.append(f'{key}: {value}')
    return '\n'.join(user_list)

def main():
    contacts = {}
    print('Welcome to the assistant bot')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(get_number(args, contacts))
        elif command == 'all':
            print(get_contacts(contacts))
        else:
            print('Invalid command')
if __name__ == '__main__':
    main()


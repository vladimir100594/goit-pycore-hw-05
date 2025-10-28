import json
import os

# Декоратор для обработки ошибок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Введіть аргумент для команди."
        except ValueError:
            return "Введіть ім'я та номер телефону, будь ласка."
        except KeyError:
            return "Введіть ім'я контакту."
    return inner


def load_contacts(filename="Контакти.json"):
    """Завантаження контактів з файлу"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return {}
    except (json.JSONDecodeError, IOError):
        return {}


def save_contacts(contacts, filename="Контакти.json"):
    """Збереження контактів у файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(contacts, file, ensure_ascii=False, indent=2)
        return True
    except IOError:
        return False


def parse_input(user_input):
    """
    Функція для розбору користувацького вводу.
    
    Приймає рядок вводу і розділяє його на команду та аргументи.
    Команда приводиться до нижнього регістру для уніфікації.
    
    Args:
        user_input (str): Рядок, введений користувачем
        
    Returns:
        tuple: Кортеж де перший елемент - команда, інші - аргументи
    """
    # Якщо рядок порожній, повертаємо порожню команду і порожній список аргументів
    if not user_input.strip():
        return "", []
    # Розділяємо рядок по пробілах. Перше слово - команда, інші - аргументи
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

@input_error
def add_contact(args, contacts):
    """Додавання нового контакту"""
    if len(args) < 2:
        raise IndexError
    if len(args) == 0:
        raise IndexError
    if len(args) == 1:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    save_contacts(contacts)
    return "Контакт додано."

@input_error
def change_contact(args, contacts):
    """Зміна існуючого контакту"""
    if len(args) < 2:
        raise IndexError
    if len(args) == 0:
        raise IndexError
    if len(args) == 1:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        save_contacts(contacts)
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

@input_error
def show_phone(args, contacts):
    """Показ номера телефону контакту"""
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."


def show_all(contacts):
    """Показ всіх контактів"""
    if not contacts:
        return "Контакти не знайдено."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    
    return "\n".join(result)

@input_error
def delete_contact(args, contacts):
    """Видалення контакту"""
    name = args[0]
    if name in contacts:
        deleted_phone = contacts[name]
        del contacts[name]
        save_contacts(contacts)
        return f"Контакт '{name}' ({deleted_phone}) видалено."
    else:
        return "Контакт не знайдено."


def main():
    """Головна функція програми"""
    contacts = load_contacts()  # Завантажуємо збережені контакти
    print("Ласкаво просимо до бота-помічника!")
    
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["закрити", "вихід", "close", "exit"]:
            print("До побачення!")
            break

        elif command in ["привіт", "hello"]:
            print("Як я можу вам допомогти?")
            
        elif command in ["додати", "add"]:
            print(add_contact(args, contacts))
            
        elif command in ["змінити", "change"]:
            print(change_contact(args, contacts))
            
        elif command in ["телефон", "phone"]:
            print(show_phone(args, contacts))
            
        elif command in ["всі", "all"]:
            print(show_all(contacts))
            
        elif command in ["видалити", "delete"]:
            print(delete_contact(args, contacts))
            
        else:
            print("Невідома команда.")


# Перевіряємо
if __name__ == "__main__":
    # Запускаємо головну функцію
    main()
# Saved favorite number

import json

filename = 'numbers.json'

def get_stored_number():
    """Проверяет наличие сохраненного числа."""
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_number():
    """Показывает/Сохраняет число"""
    number = get_stored_number()
    if number:
        print(f"Ваше любимое число - {number}")
    else:
        try:
            number = int(input("Введите свое любимое число: "))
        except ValueError:
            print("Извините, но Вы должны ввести число!") 
        else: 
            with open(filename, 'w') as f:
                json.dump(number, f)
                print(f"В следующий раз я отображу Ваше число!")

get_stored_number()
get_number()
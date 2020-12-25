# Favorite number

import json

filename = 'numbers.json'

def get_number():
    try:
        number = int(input("Введите свое любимое число: "))
    except ValueError:
        print("Извините, но Вы должны ввести число!") 
    else: 
        with open(filename, 'w') as f:
            json.dump(number, f)

def show_number():
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        print(f"Ваше любимое число - {favorite_number}")

get_number()
show_number()





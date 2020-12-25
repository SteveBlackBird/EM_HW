# Check username

import json

def get_stored_username():
    """Получает хранимое имя, если оно существует"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя"""
    username = input("Введите свое имя: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Приветствует пользователя по имени"""
    username = get_stored_username()
    if username:
        print(f"Your name is {username}?")
        answer = input("Yes/No: ")
        if answer == 'Yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We will remember you next time, {username}!")
    else:
        username = get_new_username()
        print(f"We will remember you next time, {username}!")

greet_user()
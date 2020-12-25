# Questioning

active = True
filename = "questioning.txt"

def clear_file():
    with open(filename, 'w') as clear_file:
        clear_file.write('')

while active:
    message = str(input("Почему Вам нравится программировать?: "))

    if message == "No":
        print("Bye-bye!")
        active = False
    elif message == "clear":
        clear_file()
    else:
        with open(filename, 'a') as file:
            file.write(f"{message}\n")




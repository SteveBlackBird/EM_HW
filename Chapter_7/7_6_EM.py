# Three ways

message = input("\nВведите Ваш возраст\n(Для выхода введите: 'quit'):")
active = True

while (message != 'quit') and active:
    age = int(message)
    if age < 3:
        print("Ваш билет бесплатный!")
        break
    elif (age < 12) and (age >= 3):
        print("Ваш билет стоит 10$")
        active = False
        break
    else:
        print("Ваш билет стоит 15$")
        break
# Cinema tickets

message = "Введите Ваш возраст:"

while True:
    age = int(input(message))
    if age < 3:
        print("Ваш билет бесплатный!")
    elif (age < 12) and (age > 3):
        print("Ваш билет стоит 10$")
    else:
        print("Ваш билет стоит 15$")
# Pizza's topping

message = "\nДобрый день! введите топпинг для пиццы"
message += "\n(Для выхода введите: 'quit'):"

while True:
    topping = input(message)
    if topping == 'quit':
        break
    else:
        print(f"Топпинг {topping} добавлен к пицце!")
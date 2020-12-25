# Adding

try:
    num_one = int(input("Введите число: "))
    num_two = int(input("Введите второе число: "))
except ValueError:
    print("Извините, но Вы должны ввести число!")
else:
    result = num_one + num_two
    print(result)


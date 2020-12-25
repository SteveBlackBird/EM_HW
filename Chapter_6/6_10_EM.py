# Favorite numbers 2

favorite_numbers = {
    'steve': [10, 22, 21],
    'john': [9, 12, 13],
    'lena': [0, 1, 3],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} have this favorite numbers:")
    for number in numbers:
        print(f"\t{number}")
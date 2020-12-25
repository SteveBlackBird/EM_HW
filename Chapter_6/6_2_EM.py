# Favorite numbers

favorite_numbers = {
    'steve': 10,
    'john': 9,
    'lena': 0,
}

number1 = favorite_numbers.get('steve', 'No values')
number2 = favorite_numbers.get('john', 'No values')
number3 = favorite_numbers.get('lena', 'No values')

print(f"Steve - {number1} John - {number2} \nLena - {number3}")
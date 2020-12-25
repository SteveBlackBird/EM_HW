# More cycles

my_foods = ['pizza', 'pasta', 'borsch']
friend_foods = my_foods[:]

friend_foods.remove('borsch')
friend_foods.append('ice cream')

print('My favorite foods:')
for food in my_foods:
    print(food)

print('\n')

print("My friend's favorite foods:")
for food in friend_foods:
    print(food)
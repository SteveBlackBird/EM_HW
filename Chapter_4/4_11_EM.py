# My pizza, your pizza

my_pizzas = ['pepperoni', 'chicken ranch', 'ten cheese']
friend_pizzas = my_pizzas[:]

my_pizzas.insert(0, 'bbq')
friend_pizzas.append('vegan')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
# Sandwiches

def make_sandwich(*toppings):
    """   Make sandwich with toppings   """
    print("You want a sandwich with:")
    for topping in toppings:
        print(f"-{topping}")
    return topping

make_sandwich('tuna', 'lime', 'butter')
make_sandwich('meat', 'bbq', 'cheese')
make_sandwich('chicken', 'cheese', 'paprika')

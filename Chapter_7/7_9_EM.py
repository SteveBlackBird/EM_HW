# Without pastarami

sandwich_orders = ['tuna', 'pastarami', 'bbq', 'chicken', 'pastarami', 'pastarami']
finished_sandwiches = []

print("Sorry, but we don't have pastarami")

while 'pastarami' in sandwich_orders:
    sandwich_orders.remove('pastarami')

print(sandwich_orders)

while sandwich_orders:
        order = sandwich_orders.pop()
        print(f"I make your {order} sandwich!")
        finished_sandwiches.append(order)

print("\nHere's all our finished sandwiches:\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")


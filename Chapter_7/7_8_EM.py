# Sandwiches

sandwich_orders = ['tuna', 'bbq', 'chicken']
finished_sandwiches = []

while sandwich_orders:
        order = sandwich_orders.pop()
        print(f"I make your {order} sandwich!")
        finished_sandwiches.append(order)

print("\nHere's all our finished sandwiches:\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")


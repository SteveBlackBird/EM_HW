# Dream vacation

vacation_poll = {}
active = True

while active:
    name = input("\nWhat is your name?:\n")
    responce = input(f"What is you dream vacation, {name.title()}?\n")

    vacation_poll[name] = responce

    repeat = input("Any one else? 'Y/N':")
    if repeat == 'N':
        active = False

print("_____Dream vacation poll results_____")
for key, value in vacation_poll.items():
    print(f"{key.title()} dream about {value}")
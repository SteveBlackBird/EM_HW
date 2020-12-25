# The guest list
names = ['Kirill', 'Sergey', 'Evgeni', 'Victor', 'Lenya']
message = f"I would like to invite you to supper, {names[4].title()}"

print(message)

for name in names:
    print(f"I would like to invite you to dinner, {name.title()}")
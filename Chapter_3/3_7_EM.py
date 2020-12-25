# Changing the guest list 3
names = ['Kirill', 'Sergey', 'Evgeni', 'Victor', 'Lenya']

missing_guest = 'Victor'
names.remove(missing_guest)

print(f"{missing_guest.title()} willn't be able to attend the dinner")

names.append('Vasiliy')

for name in names:
    print(f"You're invited to my dinner, dear {name.title()}")

print("Sorry, but we have more guests!")

names.insert(0, 'Petya')
names.insert(3, 'Kostik')
names.append('Harry')

for name in names:
    print(f"You're invited to my dinner, dear {name.title()}")

print("Sorry, we only have space for two guests :(")

deleted_guest = names.pop()
print(f"Sorry, we cant invite you {deleted_guest.title()}")
deleted_guest = names.pop()
print(f"Sorry, we cant invite you {deleted_guest.title()}")
deleted_guest = names.pop()
print(f"Sorry, we cant invite you {deleted_guest.title()}")
deleted_guest = names.pop()
print(f"Sorry, we cant invite you {deleted_guest.title()}")
deleted_guest = names.pop()
print(f"Sorry, we cant invite you {deleted_guest.title()}")
deleted_guest = names.pop()
print(f"Sorry, we cant invite you {deleted_guest.title()}")

print(f"{names[0].title()} and {names[1].title()}, early invitations are valid")

del names[0:2]
print(names)

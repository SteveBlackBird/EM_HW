# Ordinals

ordinals = [value for value in range(1,9+1)]

if ordinals:
    for number in ordinals:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number == 3:
            print(f"{number}rd")
        else:
            print(f"{number}th")
else:
    print("Empty list")
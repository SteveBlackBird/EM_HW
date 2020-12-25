# Cats & dogs

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print("File didn't exist!")
    else:
        print(content)

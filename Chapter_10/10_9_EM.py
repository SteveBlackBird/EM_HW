# Errors without notification

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        print(content)
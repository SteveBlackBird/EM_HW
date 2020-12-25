# Guest book

prompt = 'Enter your name, please: '

filename = 'guestbook.txt'
active = True

while active:
    message = str(input(prompt))
    if message == 'N':
        print('Bye-bye!')
        active = False
    else:
        print(f"Dear {message.title()} now you're our guest! Take a rest!")
        with open(filename, 'a') as file:
            file.write(f"{message.title()} - is our guest now\n")
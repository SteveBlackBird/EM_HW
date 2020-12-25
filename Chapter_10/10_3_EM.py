# Guest

filename = 'guest.txt'

prompt = "Enter your name: "
message = input(prompt)

with open(filename, 'a') as file:
    file.write(f"{message.title()}\n")
    file.close()


# Learning C

with open('learning_python.txt') as file:
    lines = file.readlines()

for line in lines:
    mod = line.replace('Python', 'C')
    print(mod)


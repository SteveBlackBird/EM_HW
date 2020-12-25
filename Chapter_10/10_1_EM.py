with open('learning_python.txt') as file:
    content = file.read()

string = ""
for line in content:
    string += line.rstrip('\n')

print(string)

with open('learning_python.txt') as file01:
    lines = file01.readlines()

python_list = []
for line in lines:
    print(line)
    python_list.append(line)

print(python_list)



# Frequent words

filename = 'the_book.txt'

with open(filename) as f:
    line = f.read()

variable = line.lower().count('the')

print(variable)
# Glossary

glossary = {
    'tuple': "collection of objects which ordered and immutable",
    'list': "collection of objects",
    'dictionary': "Python's efficient key/value hash table structure is called",
}

glossary01 = glossary.get('tuple', 'No values')
glossary02 = glossary.get('list', 'No values')
number3 = glossary.get('dictionary', 'No values')

print(f"tuple - {glossary01}\nlist - {glossary02} \ndictionary - {number3}")
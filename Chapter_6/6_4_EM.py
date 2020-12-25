# Glossary 2

glossary = {
    'tuple': "collection of objects which ordered and immutable",
    'list': "collection of objects",
    'dictionary': "Python's efficient key/value hash table structure is called",
}

for key, value in sorted(glossary.items()):
    print(f"\n{key.title()}:\n{value}")

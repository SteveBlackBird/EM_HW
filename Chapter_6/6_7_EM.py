# People

person01 = {'first_name': 'tom', 'last_name': 'pitt', 'age': 23, 'city': 'london'}
person02 = {'first_name': 'bret', 'last_name': 'cruz', 'age': 22, 'city': 'paris'}
person03 = {'first_name': 'jane', 'last_name': 'foster', 'age': 22, 'city': 'moscow'}

persons = [person01, person02, person03]

for person in persons:
    name = person['first_name'].title() + ' ' + person['last_name'].title()
    age = person['age']
    city = person['city'].title()
    print(f"{name} is {age} years old and live in {city}")
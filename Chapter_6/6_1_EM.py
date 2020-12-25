# Person

person01 = {'first_name': 'tom', 'last_name': 'pitt', 'age': 22, 'city': 'london'}

print(person01)

first_name = person01['first_name'].title()
last_name = person01['last_name'].title()
age = person01['age']
city = person01['city'].title()
print(f"{first_name} {last_name}? He live in {city} and his age is {age}")
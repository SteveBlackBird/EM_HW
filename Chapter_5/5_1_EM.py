# Conditional tests №1

car = 'subaru'
age = 28

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print("Is age == 28? I predict True.")
print(age == 28)

print("Is age == 20? I predict False.")
print(age == 20)

print("Is age > 20? I predict True.")
print(age > 20)

print("Is age > 30? I predict False.")
print(age > 30)

print("Is (age == 28) and (age != 20)? I predict True.")
print((age == 28) and (age != 20))

print("Is (age == 28) and (age < 25)? I predict False.")
print((age == 28) and (age < 25))

print("Is (age == 28) or (age > 30)? I predict True.")
print((age == 28) or (age > 30))

print("Is (age < 25) or (age > 30)? I predict False.")
print((age < 25) or (age > 30))
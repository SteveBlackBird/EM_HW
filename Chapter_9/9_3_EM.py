# Users

class User():

    def __init__(self, first_name, last_name, age, city):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        msg = f"Hello {self.first.title()} {self.last.title()}"
        print(f'{msg}\n Your age is - {self.age} and city iiis - {self.city.upper()}')


user = User('danila', 'badrov', 20, 'vladivostok')

user.describe_user()
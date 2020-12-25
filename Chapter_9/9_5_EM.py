# Login attempts

class User():

    def __init__(self, first_name, last_name, age, city):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(f"{self.login_attempts}")

    def describe_user(self):
        msg = f"Hello {self.first.title()} {self.last.title()}"
        print(f'{msg}\n Your age is - {self.age} and city iiis - {self.city.upper()}')


user = User('danila', 'badrov', 20, 'vladivostok')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.show_login_attempts()
user.reset_login_attempts()
user.show_login_attempts()

user.describe_user()
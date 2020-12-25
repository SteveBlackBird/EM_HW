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

class Privileges():

    def __init__(self, privileges=[
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей",
        ]):
        self.privileges = privileges
    
    def show_privileges(self):
        """   Выводит список привелегий Администратора   """
        print('\nHere is the list of admins privileges:')
        for privelege in self.privileges:
            print(f"\t{privelege.title()}")

class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()

    def show_user_name(self):
        print(f"{self.first.title()} {self.last.title()} - we are greetings You!")
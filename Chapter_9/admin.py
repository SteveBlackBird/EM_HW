from user import User

class Privileges():
    """   Класс привелегий.   """

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
    """   Класс администратора   """

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()

    def show_user_name(self):
        """  Приветствие пользователя   """
        print(f"{self.first.title()} {self.last.title()} - we are greetings You!")
# Empoloyee

class Employee():
    """Класс, представляющий работника."""

    def __init__(self, first_name, last_name, salary):
        self.f_name = first_name
        self.l_name = last_name
        self.salary = salary

    def give_raise(self, salary=0):
        """Увеличивает ежегодный оклад на 5000$ или больше."""
        if salary:
            self.salary += salary
        else:
            self.salary += 5000
    
    def show_employee(self):
        """Отображение экземпляра работника."""
        print(f"{self.f_name} {self.l_name} have year salary - {self.salary}")

worker = Employee('Sergey', 'Ivanov', 100000)
worker.show_employee()
worker.give_raise()
worker.show_employee()
worker.give_raise(33000)
worker.show_employee()
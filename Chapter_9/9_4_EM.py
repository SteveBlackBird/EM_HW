# Visitors

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name.title()}")

    def open_restaurant(self):
        print(f"The {self.name.title()} of {self.type} is open!")

    def read_served(self):
        """   Выводит количество обслуженных посетителей   """
        print(f"{self.number_served}")
    
    def set_number_served(self):
        number = int(input("Введите кол-во обслуженных посетителей: "))
        self.number_served = number

    def increment_number_served(self):
        """   икнкремент на указанное количество пользователем   """
        number = int(input("Введите кол-во обслуженных посетителей: "))
        self.number_served += number

restaurant = Restaurant('heelby', 'mexic food')
restaurant.read_served()
restaurant.set_number_served()
restaurant.read_served()
restaurant.increment_number_served()
restaurant.read_served()
restaurant.set_number_served()
restaurant.read_served()
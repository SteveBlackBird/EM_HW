class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name.title()}")

    def open_restaurant(self):
        print(f"The {self.name.title()} of {self.type} is open!")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cousine_type):
        super().__init__(restaurant_name, cousine_type)
        self.flavors = 'vanila', 'chocolate', 'strawberry'

    def show_list_flavors(self):
        print(f"{self.flavors}")
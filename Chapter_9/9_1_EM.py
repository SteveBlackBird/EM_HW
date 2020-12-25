# Restaurant

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name}")

    def open_restaurant(self):
        print(f"The {self.name.title()} of {self.type} is open!")

restik = Restaurant('Albus', 'BBQ')

restik.describe_restaurant()
restik.open_restaurant()
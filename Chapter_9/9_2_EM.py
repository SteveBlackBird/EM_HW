# Three restaurants

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name}")

    def open_restaurant(self):
        print(f"The {self.name.title()} of {self.type} is open!")

restik01 = Restaurant('Albus', 'BBQ')
restik02 = Restaurant('Nagasaki', 'susi')
restik03 = Restaurant('il-patio', 'italian')

restik01.describe_restaurant()
restik02.describe_restaurant()
restik03.describe_restaurant()

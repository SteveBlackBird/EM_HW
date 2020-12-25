# electric_car.py

class Car():
    """Simple car model."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometr(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back odometer!")

    def increment_odometr(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"This car has a Gas-tank!")

class Battery():
    """Simple car power battery model"""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Show the power of battery"""
        print(f"The power of battery is - {self.battery_size}-kWh")

    def get_range(self):
        """Show approximate battery power reserve"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """Chek and set the battery size"""
        if self.battery_size <= 75:
            self.battery_size = 100


class ElectricCar(Car):
    """Show the aspects specific for an electro car."""

    def __init__(self, make, model, year):
        """Initialising attributes of parent-class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"This type of car hasn't a Gas tank, sorry :)")


my_tesla = ElectricCar('tesla', 'i', 2020)
my_cadillac = Car('cadillac', 'gts', 2019)
print(my_tesla.get_descriptive_name())
print(my_cadillac.get_descriptive_name())
my_tesla.fill_gas_tank()
my_cadillac.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

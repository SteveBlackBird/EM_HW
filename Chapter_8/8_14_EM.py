# Cars

from car_functions import make_car_list, make_car_dict

i = 1

while i < 3:
    car = make_car_list('suzuki', 'legacy', color='blue', tow_package=True)
    i += 1

car02 = make_car_dict('bmw', 'x5', color='black', tow_package=True)

print(car)
print(car02)
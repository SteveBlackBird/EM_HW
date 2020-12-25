# For 8_14_EM.py

def make_car_list(brand, model, **car_info):
    """   Return list  of new cars   """
    car_info['brand'] = brand
    car_info['model'] = model
    # cars.append(car_info)
    return car_info


def make_car_dict(brand, model, **car_info):
    """   Return a dict of new cars   """
    car_info['brand'] = brand
    car_info['model'] = model
    car_id = brand[0:2] + model[0:3]
    # cars_dict[car_id] = car_info
    return car_info
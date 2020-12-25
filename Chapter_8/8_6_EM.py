# City names

def city_countries(city, country):
    if len(country) <= 3:
        message = f"{city.title()}, {country.upper()}"
    else:
        message = f"{city.title()}, {country.title()}"
    return message

city01 = city_countries('moscow', 'russia')
city02 = city_countries('vladivostok', 'russia')
city03 = city_countries('london', 'uk')
print(city01)
print(city02)
print(city03)


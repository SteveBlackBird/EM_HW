# Cities

cities = {
    'moscow': {
        'country': 'russia',
        'poppulation': 900,
        'fact': 'nice country'
    },
    'seol': {
        'country': 'korea',
        'poppulation': 800,
        'fact': 'top country'
    },
    'sidney': {
        'country': 'australia',
        'poppulation': 700,
        'fact': 'kenguru'
    }
}

for city, information in cities.items():
    print(f"\n{city.title()}:")
    for key, value in information.items():
        if key == 'poppulation':
            print(f"\t{key.title()}: {value}")
        else:
            print(f"\t{key.title()}: {value.title()}")
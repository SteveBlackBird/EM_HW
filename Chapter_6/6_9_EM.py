# Favorite places

favorite_places = {
    'steve': ['vladivostok', 'moscow', 'london'],
    'john': ['moscow', 'paris'],
    'july': ['moscow', 'vladivostok'],
    'sergey': ['seul', 'singapore', 'london'],
    'cyrill': ['mytishi'],
}

for name, places in favorite_places.items():
    if len(places) >= 2:
        print(f"\n{name.title()} like this places:")
    else:
        print(f"\n{name.title()} like this place:")
    for place in places:
        print(f"\t{place.title()}")

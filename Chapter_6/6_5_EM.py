# Rivers

rivers = {
    'neil': 'egypt',
    'yenisei': 'russia',
    'amazon': 'ecuador',
    'mississippi': 'united states',
    'yangtze': 'china',
}

for keys, values in rivers.items():
    print(f"The {keys.title()} runs through {values.title()}")

for river_name in rivers.keys():
    print(f"{river_name.title()}")

for river_city in rivers.values():
    print(f"{river_city.title()}")
# Pets

muhtar = {
    'kind': 'dog',
    'master': 'jake harper',
}

bolto = {
    'kind': 'wolf',
    'master': 'clif spacer',
}

soleniye = {
    'kind': 'pickle',
    'master': 'rick sanchez'
}

pets = [muhtar, bolto, soleniye]

for pet in pets:
    master = pet['master'].title()
    print(f"{master} have a {pet['kind']}")
# Periods of life

age = 28

if age < 2:
    period = 'младенец'
elif (age >= 2) and (age < 4):
    period = 'малыш'
elif (age >= 4) and (age < 13):
    period = 'ребенок'
elif (age >= 13) and (age < 20):
    period = 'подросток'
elif (age >= 20) and (age < 65):
    period = 'взрослый'
else:
    period = 'пожилой человек'

print(f"Ваш период жизни - {period}")
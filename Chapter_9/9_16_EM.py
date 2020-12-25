# Module of the week

from random import sample

lottery_list = ['1', '5', '2', '6', '7', '13', '15', '3', '20', '11', 'a', 'v', 'd', 'c', 'j']

numbers = ""
for number in sample(lottery_list, 4):
    numbers += number

print(numbers)
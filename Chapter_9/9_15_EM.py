# Lottery analysis

from random import choice

lottery_list = ['1', '5', '2', '6', '7', '13', '15', '3', '20', '11', 'a', 'v', 'd', 'c', 'j']
i = 1

def make_lucky_ticket():
    lucky_ticket = []
    i = 1
    while i <= 4:
        lucky_number = choice(lottery_list)
        lucky_ticket.append(lucky_number)
        i += 1
    return lucky_ticket

lucky_ticket = make_lucky_ticket()

while True:
    my_ticket = make_lucky_ticket()
    if my_ticket != lucky_ticket:
        my_ticket = make_lucky_ticket()
        i += 1
    else:
        print("Your ticket is a lucky ticket!")
        print(f"\n{my_ticket}\n")
        break

print(i)
print(lucky_ticket)
print(f"This combination is bingo! - {' '.join(lucky_ticket)}")
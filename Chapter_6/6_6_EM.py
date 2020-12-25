# Poll

poll = {
    'jen': 'passed',
    'steve': 'passed',
    'cyrill': 'passed',
    'roman': 'not passed',
    'sergey': 'passed',
    'mark': 'not passed'
}

for key, value in poll.items():
    if value == 'passed':
        print(f"THX a lot, dear {key.title()} you are passed the poll!")
    elif value == 'not passed':
        print(f"Dear {key.title()}! Do you want to take a survey?")
# Messages

messages = ['hi', 'how are you?', 'what is your name',]

def show_messages(messages):
    """   Print every message in a list   """
    for msg in messages:
        print(f"{msg.title()}")

show_messages(messages[:])


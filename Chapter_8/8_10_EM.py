# Send messages

messages = ['hi', 'how are you?', 'what is your name',]
sent_messages = []

def send_messages(messages):
    """   Send message from 1 to another   """
    while messages:
        msg = messages.pop()
        sent_messages.append(msg)

send_messages(messages)

print(messages)
print(sent_messages)



import re
import random


responses = {
    "hello": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you."
    ],
    "how are you": [
        "I am fine! How are you?",
        "I am doing great. Thanks for asking!"
    ],
    "your name": [
        "I am a simple Python chatbot.",
        "You can call me ChatBot."
    ],
    "help": [
        "Sure! Tell me what you need help with.",
        "I am here to assist you."
    ],
    "bye": [
        "Goodbye! Have a nice day!",
        "See you again!"
    ]
}


def chatbot(user_input):


    user_input = user_input.lower()


    user_input = re.sub(r'[^\w\s]', '', user_input)


    if re.search(r'\b(hello|hi|hey)\b', user_input):
        return random.choice(responses["hello"])

    elif re.search(r'how are you', user_input):
        return random.choice(responses["how are you"])

    elif re.search(r'(your name|who are you)', user_input):
        return random.choice(responses["your name"])

    elif re.search(r'\b(help|support)\b', user_input):
        return random.choice(responses["help"])

    elif re.search(r'\b(bye|goodbye|exit)\b', user_input):
        return random.choice(responses["bye"])

    else:
        return "Sorry, I don't understand. Can you ask something else?"


print("ChatBot: Hello! Welcome to Python ChatBot.")
print("Type 'bye' to exit the conversation.\n")

while True:

    user = input("You: ")

    reply = chatbot(user)

    print("ChatBot:", reply)

    if re.search(r'\b(bye|goodbye|exit)\b', user.lower()):
        break

import random
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm good, thank you!", "I'm doing well, how about you?"],
    "what's your name?": ["I'm a chatbot.", "I don't have a name."],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
}

def get_response(user_input):
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I don't understand that."

def main():
    print("Chatbot: Hello! I'm a chatbot. How can I help you today?")
    while True:
        user_input = input("You: ").lower()
        response = get_response(user_input)
        print("Chatbot:", response)
        if user_input == 'bye':
            break

if __name__ == "__main__":
    main()

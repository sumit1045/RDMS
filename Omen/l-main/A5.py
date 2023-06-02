# Dictionary of predefined responses
responses = {
    "hello": "Hi there!",
    "how are you?": "I'm doing well, thank you!",
    "what's your name?": "I'm a chatbot.",
    "default": "I'm sorry, I didn't understand that."
}

# Function to generate a response to user input
def generate_response(user_input):
    user_input = user_input.lower()

    # Check if user input matches any predefined response
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

# Chat loop
while True:
    user_input = input("User: ")
    response = generate_response(user_input)
    print("Chatbot:", response)

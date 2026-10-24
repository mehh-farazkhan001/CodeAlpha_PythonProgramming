
# TASK 4: Basic Rule-Based Chatbot

def chatbot_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif "how are you" in message:
        return "I'm fine, thanks!"

    elif "your name" in message:
        return "I am a simple Python chatbot."

    elif "help" in message:
        return "You can say hello, ask how I am, or say bye."

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."

# Main program
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Chatbot:", response)

    if user_input.lower().strip() in [
        "bye", "goodbye", "exit", "quit"
    ]:
        break

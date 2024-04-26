import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking. How about you?']),
    (r'i\'m (.*)', ['Nice to hear that. How can I assist you today?']),
    (r'(.*) your name?', ['My name is ChatBot.']),
    (r'(.*) help (.*)', ['Sure, I can help you with that.']),
    (r'(.*) (weather|temperature) (.*)', ['You can check the weather online.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
]

# Create a Chat instance
chatbot = Chat(patterns, reflections)

def chat_with_user():
    print("Hello! I'm ChatBot. How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    nltk.download('punkt')  # Download necessary NLTK data
    chat_with_user()

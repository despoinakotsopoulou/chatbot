import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses for the chatbot using the Chat class
responses = {
    (r'hi', 'hello', 'hey',): ['Hello!', 'Hey!', 'Hi!'],
    (r'how are you',): ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    (r'what is your name',): ["My name is Chatbot!", "I'm Chatbot!"],
    (r'what do you do',): ["I'm a chatbot designed to help you learn more about Despoina Kotsopoulou, a Data Scientist, AI Engineer, and Researcher."],
    (r'how can I contact her',): ["You can contact her by email at: despoinakotsopoulou@gmail.com"],
    (r'quit',): ["Goodbye!", "Bye!", "See you later!"],
}

# Create a chatbot instance
chatbot = Chat(responses, reflections)

# Define a function to start the chatbot
def main():
    print("Chatbot: Hi! I'm Despoina's assitant! You can ask me about her skills and experience, education and certificates! If you want to exit, just type 'quit'.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        if not response:
            print("Chatbot: I'm sorry, I didn't understand that.")
        else:
            print("Chatbot:", response[0])
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break

if __name__ == "__main__":
    main()

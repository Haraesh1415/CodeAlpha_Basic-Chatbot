# Basic Chatbot

def chatbot():
    print("Chatbot: Hello! How can I help you?")

    while True:
        user = input("You: ")

        if user == "Hello":
            print("Chatbot: Hi!")

        elif user == "How are you":
            print("Chatbot: I'm Fine!")

        elif user == "Bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: I don't understand.")

chatbot()

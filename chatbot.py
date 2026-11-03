import datetime

def chatbot():
    print("\n===== Welcome to Basic Chatbot =====")
    print("You can chat with me!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif user == "how are you":
            print("Bot: I am fine. Thank you!")

        elif user == "what is your name":
            print("Bot: I am your Python Chatbot.")

        elif user == "date":
            today = datetime.date.today()
            print("Bot: Today's date is", today)

        elif user == "help":
            print("Bot: You can ask me hello, how are you, or date.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
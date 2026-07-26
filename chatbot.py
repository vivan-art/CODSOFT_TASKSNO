print("🤖 Welcome to CodSoft Rule-Based Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")
    elif "name" in user:
        print("Bot: My name is CodSoft AI Chatbot.")
    elif "college" in user:
        print("Bot: I am a virtual chatbot, so I don't attend college.")
    elif "course" in user:
        print("Bot: I can help you with AI, Python, and programming basics.")
    elif "time" in user:
        from datetime import datetime
        print("Bot: Current time is", datetime.now().strftime("%H:%M:%S"))
    elif "thanks" in user or "thank you" in user:
        print("Bot: You're welcome!")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")

while True:   # This creates the continuous loop
    user_input = input("You: ")   # Ask user for input
    
    # Greetings
    if user_input.lower() in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I assist you today?")
    
    # Exit commands
    elif user_input.lower() in ["bye", "exit", "quit", "goodbye"]:
        print("Bot: Goodbye! Have a great day!")
        break   # This breaks the loop and ends the program
    
    # Ask about name
    elif user_input.lower() in ["what's your name?", "your name?"]:
        print("Bot: I'm ChatBot 1.0, your rule-based friend!")
    
    # Ask how bot is
    elif user_input.lower() in ["how are you?", "how are you doing?"]:
        print("Bot: I'm just a bot, but I'm doing great! 😊")
    
    # Help
    elif user_input.lower() in ["help"]:
        print("Bot: You can ask me about my name, how I am, or just say hello!")
    
    # Fallback for anything else
    else:
        print("Bot: Sorry, I don't understand that. Try saying 'Hello' or 'Help'!")

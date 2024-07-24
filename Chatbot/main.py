from tkinter import *
from chatbot import Chatbot
from ui import ChatApplication

if __name__ == "__main__":
    # Create a Chatbot instance
    chatbot = Chatbot()

    # Create a Tkinter GUI application
    app = ChatApplication(chatbot)
    
    # Run the application
    app.run()

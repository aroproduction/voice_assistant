import tkinter as tk
from tkinter import Scrollbar, Text, Button
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyBot')

# Create a new instance of a Tkinter window
window = tk.Tk()
window.title("AI Chatbot")

# Create a Text widget to display chat history
chat_history = Text(window, wrap=tk.WORD)
chat_history.pack()

# Create a Scrollbar for the Text widget
scrollbar = Scrollbar(window, command=chat_history.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_history.config(yscrollcommand=scrollbar.set)

# Create an Entry widget for user input
user_input = tk.Entry(window)
user_input.pack()

# Function to handle user input and display responses
def send_message():
    user_message = user_input.get()
    user_input.delete(0, tk.END)  # Clear the user input field
    chat_history.insert(tk.END, "You: " + user_message + "\n")
    response = chatbot.get_response(user_message)
    chat_history.insert(tk.END, "Bot: " + str(response) + "\n")
    chat_history.see(tk.END)  # Scroll to the end of the chat

# Create a Send button to send messages
send_button = Button(window, text="Send", command=send_message)
send_button.pack()

# Initialize the chatbot with some training data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Start the Tkinter main loop
window.mainloop()

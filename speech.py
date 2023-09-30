import tkinter as tk
import speech_recognition as sr
import threading
import os
import urllib.parse

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to listen to voice commands and execute actions
def listen_and_execute():
    while listening:
        with sr.Microphone() as source:
            print("Listening for a command...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command recognized: {command}")

            if "search" in command:
                # Extract the search query from the command
                query = command.replace("search", "").strip()

                # Encode the query for a URL
                encoded_query = urllib.parse.quote(query)

                # Open a web browser and perform a Google search
                os.system(f'start https://www.google.com/search?q={encoded_query}')

            elif "open youtube" in command:
                # Open YouTube in the default web browser
                os.system('start https://www.youtube.com')

            elif "open notepad" in command:
                # Open Notepad
                os.system('start notepad.exe')

            elif "exit" in command:
                print("Goodbye!")
                exit()

            # Add more commands and actions as needed

            else:
                print("Command not recognized.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

def start_listening():
    global listening
    listening = True
    listening_thread = threading.Thread(target=listen_and_execute)
    listening_thread.start()

def stop_listening():
    global listening
    listening = False

# Create the main window
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("500x250")

# Create a button to start listening
start_button = tk.Button(window, text="Start Listening", width="12", height="3", font=('Times New Roman', 12), bg='gold', command=start_listening)
start_button.pack(pady=30)

# Create a button to stop listening
stop_button = tk.Button(window, text="Stop Listening", width="12", height="3", font=('Times New Roman', 12), bg='gold', command=stop_listening)
stop_button.pack()

# Initialize the listening variable
listening = False

# Start the GUI main loop
window.mainloop()

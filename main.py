# Rule based AI ChatBot

import datetime
import difflib
import time
import tkinter as tk
from tkinter import simpledialog

responses = {
    "hi": " Hi!, how can i help you?",
    "hello": "Hi, what's on your mind?",
    "how are you": "I am fine, thanks for asking!",
    "who are you": "I am a smart ChatBot created by Vishesh, You can ask me basic questions related to Python",
    "what can you do": "I can answer your basic questions",
    "motivate me": "You are actually very motivated but for formality i will say, Remember the journey of thousand miles begins with single step!",
    "what is python": "Python is a high-level, general-purpose programming language",
    "is python interpreted": " Yes, Python is an interpreted language",
    "what are data types": "Data types define the type of value a variable holds , for instance: integers (int), floating-point numbers (float), strings (str), booleans (bool) etc.",
    "what is string": "A string is a sequence of characters enclosed inside single or double quotes. It is Immutable",
    "what is string concatenation": " String concatenation is the process of joining two or more strings together using the '+' operator.",
    "what is list": "A list is an ordered, mutable (changeable) collection of items defined using square brackets[].",
    "what is tuple": "A tuple is an immutable (unchangeable) collection of items defined using parentheses ().",
    "difference between list and tuple": "Lists are mutable (can be changed after creation) and use square brackets [] & Tuples are immutable (cannot be modified) and use parentheses ().",
    "what is dictionary": "A dictionary is an unordered, mutable collection of key-value pairs written with curly braces{}.",
    "what is set": "A set is an unordered collection of unique elements written with curly braces{}.",
    "what is if statement": "An if statement evaluates a condition. If the condition is True, it executes the indented code block below it.",
    "what is for loop": "A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item.",
    "what is while loop": "A while loop repeatedly executes a block of code as long as its condition remains True.",
    "what is break and continue": "break exits the nearest loop immediately. continue skips the current iteration and moves directly to the next iteration of the loop.",
    "what is function": "A function is a reusable block of code that performs a specific task. It is defined using the `def` keyword.",
    "what is variable": "A variable is a named box or container used to store data values in memory.",
    "what is print": "The print() function displays output or text messages on the screen.",
    "what is input": "The input() function takes input from the user as a string.",
    "what is comment": "A comment starts with a '#' symbol and is ignored by Python. It is used to explain code to humans.",
    "what is integer": "An integer (int) is a whole number without decimal points, like 5, -12, or 0.",
    "what is float": "A float is a number that contains decimal points, like 3.14, -0.5, or 2.0.",
    "what is boolean": "A boolean (bool) represents one of two logical values: True or False.",
    "what is type casting": "Type casting means converting a variable from one data type to another, like converting a string '5' to integer 5 using int().",
    "what is modulo operator": "The modulo operator (%) returns the remainder of a division. For example, 5 % 2 returns 1.",
    "what is indentation": "Indentation refers to the spaces at the start of a code line. Python uses indentation to group code blocks together.",
    "what is elif": "elif stands for 'else if'. It lets you check another condition if the previous 'if' condition was False.",
    "what is else": "The else statement executes a block of code if all previous 'if' and 'elif' conditions were False.",
    "what is len function": "The len() function returns the total number of items or characters in a string, list, or tuple.",
    "what is indexing": "Indexing means accessing an item in a list or string by its position, starting at index 0.",
    "what is syntax error": "A syntax error happens when you write code that violates Python grammar rules, like a missing parenthesis or colon.",
    "Thankyou": "You are welcome!",
}


def getresponseOfBot(UserQuestion):
    UserQuestion = UserQuestion.lower()
    for eachkey in responses:
        if eachkey in UserQuestion:
            return responses[eachkey]

    closest_match = difflib.get_close_matches(
        UserQuestion, responses.keys(), n=1, cutoff=0.5
    )

    if closest_match:
        matched_keys = closest_match[0]
        print(f"DEBUG: Auto-corrected to {matched_keys}")

        return f"(Did you mean '{matched_keys}'?)\n +  {responses[matched_keys]}"

    return " I am not able to tell that , i am still in learning phase"


def send_message(event=None):
    userInput = entry_box.get()

    if userInput == "":
        return

    chat_box.insert(tk.END, "You: " + userInput + "\n")

    entry_box.delete(0, tk.END)

    if "bye" in userInput.lower() or "exit" in userInput.lower():
        chat_box.insert(tk.END, "Bot: GoodBye! Happy learning!\n\n")
        return

    bot_reply = getresponseOfBot(userInput)

    chat_box.insert(tk.END, f"Bot: {bot_reply} \n")


window = tk.Tk()
window.title("Python Chatbot")
window.geometry("400x500")

hour = datetime.datetime.now().hour


if 5 <= hour < 12:
    greeting = "Good Morning!"
elif 12 <= hour < 18:
    greeting = "Good Afternoon!"
else:
    greeting = "Good Evening!"


name = simpledialog.askstring("Name Entry", "Please mention your name:", parent=window)

if not name:
    print("Guest")


window.attributes("-topmost", True)
window.attributes("-topmost", False)
header = tk.Label(
    window, text=f"Welcome {name.title()}, {greeting}", font=("Arial", 12, "bold")
)
header.pack(pady=10)

chat_box = tk.Text(window, width=45, height=20)
chat_box.pack(pady=5)
chat_box.insert(tk.END, "Bot: Hello! Ask me basic Python questions.\n")


entry_box = tk.Entry(window, width=35, font=("Arial", 11))
entry_box.pack(side=tk.LEFT, padx=10, pady=10)

entry_box.bind("<Return>", send_message)

send_button = tk.Button(window, text="Send", command=send_message, bg="red")
send_button.pack(side=tk.LEFT, pady=10)

window.mainloop()

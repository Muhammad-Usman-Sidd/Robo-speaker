import pyttsx3
import tkinter as tk
from tkinter import messagebox

engine = pyttsx3.init()


def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error occurred while speaking:", str(e))


def display_alert(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()  # Close the hidden Tkinter window after showing the message


def repeat_task():
    a = input(
        "Enter the word you want the robot speaker to say for you (or 'exit' to quit): ").strip()
    if a.lower() == 'exit':
        return
    elif not a:
        print("Please enter a valid word.")
    else:
        speak(a)

        # display_alert("You have entered the word", a)

    # # Schedule the next execution of repeat_task after 1000 milliseconds (1 second)
    root.after(1000, repeat_task)


root = tk.Tk()
root.withdraw()
repeat_task()
root.mainloop()

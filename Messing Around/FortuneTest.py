import random

wantit = input("Do you want to know a random quote? (y/n): " ).strip().lower()

fortunes = [
    "This is written in python",
    "Hello, World!",
    "Im going insane",
    "To be or not to be, that is the question",
    "A person who thinks all the time, has nothing to think about except thoughts",
    "Typing anything other than y makes the program sad",
    "No, you dont",
    "I forgot what I wanted to say"
]

if wantit == "y":
    print(random.choice(fortunes))
else:
    print(":(")
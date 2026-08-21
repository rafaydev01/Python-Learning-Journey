import time

lines = [
    "We are choosing to walk away from each other",
    "Our story remains unfinished",
    "I pray you always stay happy",
    "You won, I lost"
]

while True:
    for line in lines:
        for letter in line:
            print(letter, end="", flush=True)
            time.sleep(0.1)
        print("\n")
        time.sleep(1)
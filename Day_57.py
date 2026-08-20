import random

def guess_the_number():
    print("=== WELCOME TO THE NUMBER GUESSING GAME ===")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    # Loop until the user guesses correctly
    while True:
        try:
            # Take input from the user
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check conditions
            if user_guess < secret_number:
                print("Too low! 📉 Try a higher number.")
            elif user_guess > secret_number:
                print("Too high! 📈 Try a lower number.")
            else:
                print(f"🎉 CONGRATULATIONS! You found it in {attempts} attempts!")
                break
                
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Run the game
guess_the_number()

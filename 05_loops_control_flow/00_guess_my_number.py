# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48


import random

def main():
    secret_number = random.randint(1, 99)
    
    message_show = ("I am thinking of a number between 1 to 99:")
    print(message_show)
    # Get the first guess from the user
    guess = int(input("Enter the guess number: "))
    
    # Loop until the correct number is guessed
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        # Ask the user for a new guess
        guess = int(input("Enter a new guess number: "))
    
    # Print the success message when the correct number is guessed
    print("Congrats! The number was: " + str(secret_number))

# Call the main function
if __name__ == '__main__':
    main()



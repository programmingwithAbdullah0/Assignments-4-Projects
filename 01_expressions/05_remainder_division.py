# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

# Starter Code

def main():
    # Ask the user to enter the number they want to divide
    dividend: int = int(input("Enter the number you want to divide: "))
    
    # Ask the user to enter the number to divide by
    divisor: int = int(input("Enter the number you want to divide by: "))

    # Divide and get the whole number result (no decimal)
    quotient: int = dividend // divisor
    
    # Get the leftover part after division
    remainder: int = dividend % divisor

    # Show the result with both quotient and remainder
    print(f"When you divide {dividend} by {divisor}, the quotient is {quotient} and the remainder is {remainder}.")


# This line runs the main function when the program starts
if __name__ == '__main__':
    main()

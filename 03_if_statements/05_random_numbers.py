# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)


import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    for _ in range(10):  # Loop to generate 10 random numbers
        random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(random_number, end=" ")  # Print the random number on the same line with space separator

if __name__ == '__main__':
    main()
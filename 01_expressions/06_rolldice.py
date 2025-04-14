# Simulate rolling two dice, and prints results of each roll as well as the total.

"""
Simulates rolling two dice and shows each roll's result and the total.
"""
import random  # Import the random module to use random number generation

# Total sides on each die
NUM_SIDES: int = 6

def main():
    # You can set a seed for repeatable results during testing (remove the comment to use)
    # random.seed(1)
    
    # Roll the first die
    die1: int = random.randint(1, NUM_SIDES)
    
    # Roll the second die
    die2: int = random.randint(1, NUM_SIDES)
    
    # Add both dice values to get the total
    total: int = die1 + die2
    
    # Show the number of sides and the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# This part runs the main function when the program starts
if __name__ == '__main__':
    main()

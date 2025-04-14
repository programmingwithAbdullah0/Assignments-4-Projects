# Write a function that takes a list of numbers and returns the sum of those numbers.


def add_many_numbers(numbers) -> int:
    """
    This function takes a list of numbers and returns the total sum.
    """

    total_so_far: int = 0  # Start with a total of 0
    for number in numbers:  # Go through each number in the list
        total_so_far += number  # Add each number to the total

    return total_so_far  # Return the final sum

# No need to change anything below this

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # List of numbers we want to add up
    sum_of_numbers: int = add_many_numbers(numbers)  # Call the function to get the sum
    print(sum_of_numbers)  # Print the result

if __name__ == '__main__':
    main()

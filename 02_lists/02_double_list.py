# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def main():
    numbers: list[int] = [1, 2, 3, 4]  # Initial list of numbers

    for i in range(len(numbers)):  # Loop through each index of the list
        elem_at_index = numbers[i]  # Get the value at the current index
        numbers[i] = elem_at_index * 2  # Double the value and store it back in the list

    print(numbers)  # Print the updated list where each number is doubled


# This part runs the main function when the program starts
if __name__ == '__main__':
    main()

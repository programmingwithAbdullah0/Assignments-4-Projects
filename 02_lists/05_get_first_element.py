
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.



def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])  # This prints the first element in the list

def main():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []  # Initialize the list to hold user input
    elem = input("Please enter an element of the list or press enter to stop: ")  # Get first element
    while elem != "":
        lst.append(elem)  # Add element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")  # Keep asking for next element

    get_first_element(lst)  # Call the function to print the first element

if __name__ == '__main__':
    main()  # This will run the main function when the script is executed


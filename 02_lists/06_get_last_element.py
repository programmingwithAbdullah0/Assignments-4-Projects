from os import name  # Unused import - this can be removed

def get_last_element(lst):
    """ 
    Prints the last element of the provided list. 
    """
    print(lst[len(lst) - 1])  # Correct way to print last element
    # Alternative approach:
    # print(lst[-1])  # This also works for printing the last element


def get_lst():
    """ 
    Prompts the user to enter one element of the list at a time and returns the resulting list. 
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")  # Ask for more elements
    return lst  # Return the list after user stops entering


def main(): 
    lst = get_lst()  # Get list from user input
    get_last_element(lst)  # Print the last element of the list


if __name__ == '__main__':  # Corrected this line to check for the script being run
    main()  # This runs the main function

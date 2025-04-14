# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

INCHES_IN_FOOT = 12 #int


def main():
    feet: float = float(input("Enter number of feet: ")) #Get
    inches: float = feet * INCHES_IN_FOOT #perform the convert
    print("That is", inches, " inches!")

      
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
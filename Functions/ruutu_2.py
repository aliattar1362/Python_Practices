
def read_input(text):
    """
    This function reads the number entered by the user,
    checks that it is larger than zero, and returns it
    to the caller of the function.
    """
    value = int(input(text))
    while value < 1:
        int(input(text))
    return value 
            
def print_box(width, height, mark):
    """
    This function operates the 'print_box' by inserting
    the height, width and the sign of mark to be print.
    """
    print()
    for h in range(height):
        for w in range(width):
            print(mark, end='')
        print()
        
#def print_box(width, height, mark):
    #for x in range(height):
        #print(width * mark)
        
        
def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)

if __name__ == "__main__":
    main()
